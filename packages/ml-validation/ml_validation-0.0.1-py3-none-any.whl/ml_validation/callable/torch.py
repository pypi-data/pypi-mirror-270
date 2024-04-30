import numpy as np
import numpy.typing as npt
import torch.nn as nn


class TorchCallable:
    def __init__(self, model: nn.Module) -> None:
        self._model = model

    def __call__(self, _: npt.NDArray[np.float32]) -> npt.NDArray[np.bool_]:
        raise NotImplementedError()
