import numpy as np
import tensorrt as trt
from .runtime import Runtime
from _typeshed import Incomplete
from edgeiq.model_config.model_config import ModelConfig

__all__ = ['TensorRT']

class MyTRTLogger(trt.ILogger):
    def __init__(self) -> None: ...
    def log(self, severity, msg) -> None: ...

class TensorRT(Runtime):
    net: Incomplete
    batch_size: Incomplete
    context: Incomplete
    stream: Incomplete
    def __init__(self, model_config: ModelConfig, accelerator) -> None: ...
    def set_input(self, image: np.ndarray): ...
    def forward(self): ...

class CudaMemory:
    def __init__(self, host, device, shape, dtype) -> None: ...
    @property
    def host(self): ...
    @property
    def device(self): ...
    @property
    def shape(self): ...
    @property
    def dtype(self): ...
