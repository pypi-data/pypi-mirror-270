import math
from typing import Callable, Any, Optional

import torch
from numpy import median
from torch import autograd, nn
from neural_commons.cf_nn import CFModule
from neural_commons.helpers.torch_helper import detach_tuple, concatenate_tensors

_T_lr_fn = Callable[[bool, int, int, int], float]


class InvalidCFStateException(BaseException):
    def __init__(self, msg: str):
        super().__init__(msg)


class _CFForwardContext:
    def __init__(self, trainer: 'CFTrainer'):
        self.trainer = trainer
        self.lr_fn = trainer.lr_fn
        self.visits: list[tuple[tuple[torch.Tensor, ...], torch.Tensor]] = list()

    @staticmethod
    def _get_final_output_size(outputs: tuple[torch.Tensor, ...]) -> int:
        sizes = [math.prod(x.shape[1:]) for x in outputs]
        if len(sizes) == 1:
            return sizes[0]
        elif len(sizes) == 0:
            raise InvalidCFStateException("Empty tuple. At least one output should be provided.")
        else:
            return int(median(sizes))

    @staticmethod
    def _ref_in_tuple(obj: Any, objects: tuple[Any, ...]) -> bool:
        for o in objects:
            if obj is o:
                return True
        return False

    def on_visit(self, inputs: tuple[torch.Tensor, ...], output: torch.Tensor):
        new_output = output.requires_grad_()
        self.visits.append((inputs, new_output,))

    def register_forward_pass(self, final_outputs: tuple[torch.Tensor, ...],
                              loss: torch.Tensor, pick_random_visit: bool = False,
                              update_rate: float = 1.0,
                              std_lambda: float = 0.03, max_displacement: float = 0.03):
        if update_rate > 1.0 or update_rate <= 0:
            raise ValueError("update_rate must be in ]0, 1].")
        picked_visits = self.visits
        if len(picked_visits) == 0:
            raise InvalidCFStateException("No CFModules registered any visits.")
        if pick_random_visit:
            index = torch.randint(0, len(picked_visits), size=(1,)).item()
            picked_visits = [picked_visits[index]]
        final_output_size = self._get_final_output_size(final_outputs)
        for inputs, output in picked_visits:
            is_final_output = self._ref_in_tuple(output, final_outputs)
            actual_loss = loss
            if not is_final_output:
                actual_loss += (torch.std(output) - 1.0).pow(2) * std_lambda
            grad1 = autograd.grad(actual_loss, output)[0]
            out_shape = output.shape
            batch_size = out_shape[0]
            output_size = math.prod(out_shape[1:])
            lr = self.lr_fn(is_final_output, batch_size, output_size, final_output_size)
            residual = -grad1 * lr * update_rate
            if not is_final_output:
                residual_mag = torch.sqrt(torch.mean(residual.pow(2))).item()
                if residual_mag > max_displacement:
                    residual = residual * max_displacement / residual_mag
            self.trainer.on_forward_pass(detach_tuple(inputs), output.detach(), residual.detach())


class _CFTrainContext:
    def __init__(self, trainer: 'CFTrainer', selected_module: CFModule):
        self.selected_module = selected_module
        self.trainer = trainer
        self.passes: list[tuple[tuple[torch.Tensor, ...], torch.Tensor, torch.Tensor]] = list()

    def register_pass(self, inputs: tuple[torch.Tensor, ...], output: torch.Tensor, residual: torch.Tensor):
        self.passes.append((inputs, output, residual))

    def get_data_batch(self):
        if len(self.passes) == 0:
            raise ValueError("No forward passes registered in current training context.")
        inputs_c, output_c, residual_c = zip(*self.passes)
        inputs = concatenate_tensors(inputs_c, dim=0)
        output = torch.cat(output_c, dim=0)
        residual = torch.cat(residual_c, dim=0)
        return inputs, output, residual,

    def train_step(self, **kwargs):
        with torch.no_grad():
            inputs, output, residual = self.get_data_batch()
            self.selected_module.cf_learn(inputs, output, residual, **kwargs)


class CFTrainer:
    def __init__(self, *root_modules: nn.Module, lr_fn: _T_lr_fn,
                 rnd_module_selection: bool = False):
        super().__init__()
        self.rnd_module_selection = rnd_module_selection
        self.lr_fn = lr_fn
        all_modules = list()
        for root in root_modules:
            modules = root.modules()
            modules = [m for m in modules if isinstance(m, CFModule)]
            all_modules.extend(modules)
        n = len(all_modules)
        if n <= 0:
            raise ValueError(f"No modules of type {CFModule.__name__} found!")
        self.modules = all_modules
        self.index = -1
        self.hooks = list()
        self._fwd_context: Optional[_CFForwardContext] = None
        self._train_context: Optional[_CFTrainContext] = None

    def __enter__(self):
        self._fwd_context = self._new_forward_context()
        self._train_context = self._new_train_context()
        self.hooks = list()
        for module in self.modules:
            h = module.register_forward_hook(self._post_hook)
            self.hooks.append(h)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for h in self.hooks:
            h.remove()

    @staticmethod
    def train_this_batch(batch_index: int, num_batches: int, train_every: int) -> bool:
        return (batch_index + 1) % train_every == 0

    def _post_hook(self, module: nn.Module, inputs: tuple[torch.Tensor, ...], output: torch.Tensor):
        if module is self._train_context.selected_module:
            self._fwd_context.on_visit(inputs, output)

    def _next_module(self) -> CFModule:
        if self.rnd_module_selection:
            next_index = torch.randint(0, len(self.modules), size=(1,)).item()
        else:
            next_index = self.index + 1
            if next_index >= len(self.modules):
                next_index = 0
        self.index = next_index
        return self.modules[next_index]

    def _new_forward_context(self) -> _CFForwardContext:
        return _CFForwardContext(self)

    def _new_train_context(self) -> _CFTrainContext:
        return _CFTrainContext(self, self._next_module())

    def _register_forward_pass_impl(self, outputs: tuple[torch.Tensor, ...], loss: torch.Tensor,
                                    update_rate: float, std_lambda: float, max_displacement: float):
        self._fwd_context.register_forward_pass(outputs, loss, update_rate=update_rate,
                                                std_lambda=std_lambda,
                                                max_displacement=max_displacement)

    def register_forward_pass(self, outputs: tuple[torch.Tensor, ...], loss: torch.Tensor,
                              update_rate: float = 1.0,
                              std_lambda: float = 0.001, max_displacement: float = 0.03):
        if self._fwd_context is None:
            raise InvalidCFStateException("Call to register_forward_pass() outside of CFTrainer context.")
        try:
            self._register_forward_pass_impl(outputs, loss, update_rate=update_rate, std_lambda=std_lambda,
                                             max_displacement=max_displacement)
        finally:
            self._fwd_context = self._new_forward_context()

    def on_forward_pass(self, inputs: tuple[torch.Tensor, ...], output: torch.Tensor, residual: torch.Tensor):
        if self._train_context is None:
            raise InvalidCFStateException("Call to on_forward_pass() outside of CFTrainer context.")
        self._train_context.register_pass(inputs, output, residual)

    def _train_step_impl(self, **kwargs):
        self._train_context.train_step(**kwargs)

    def train_step(self, **kwargs):
        if self._train_context is None:
            raise InvalidCFStateException("Call to train_step() outside of CFTrainer context.")
        try:
            self._train_step_impl(**kwargs)
        finally:
            self._train_context = self._new_train_context()
