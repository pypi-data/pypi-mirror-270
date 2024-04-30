import numpy as np
import numpy.typing as npt


class DummyCallable:
    def __init__(self) -> None:
        pass

    def __call__(self, X: npt.NDArray[np.float32]) -> npt.NDArray[np.bool_]:
        rs = np.random.RandomState(42)
        return rs.rand(len(X), 5) > 0.5
