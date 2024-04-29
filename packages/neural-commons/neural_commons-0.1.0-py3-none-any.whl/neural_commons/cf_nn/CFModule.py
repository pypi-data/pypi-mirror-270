import torch
from abc import abstractmethod
from torch import nn


class CFModule(nn.Module):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def cf_learn(self, inputs: tuple[torch.Tensor, ...], output: torch.Tensor, residual: torch.Tensor, **kwargs):
        pass
