import math

_ce_k = 4096


class LRFunctions:
    """
    Empirically derived learning-rate functions for use with `CFTrainer`.
    """

    @staticmethod
    def for_mse(is_final: bool, batch_size: int, output_size: int, final_output_size: int):
        if is_final:
            return 0.5 * batch_size * output_size
        else:
            return 0.5 * batch_size * final_output_size * output_size / (output_size + final_output_size)

    @staticmethod
    def for_ce(is_final: bool, batch_size: int, output_size: int, final_output_size: int):
        fos = output_size if is_final else final_output_size
        value1 = batch_size * fos
        value2 = 200
        select = _ce_k / (_ce_k + value1)
        base_result = value2 * select + value1 * (1 - select)
        if is_final:
            return base_result
        else:
            return 7 * base_result
