import warnings

from .dummy import DummyCallable  # noqa: F401

try:
    from .torch import TorchCallable  # noqa: F401
except ImportError:
    warnings.warn("TorchCallable is disabled")
