import numpy as np
from ._constants import HAILO_SUPPORTED_OS as HAILO_SUPPORTED_OS, QAIC_SUPPORTED_OS as QAIC_SUPPORTED_OS, SupportedDevices as SupportedDevices
from ._trt_support import is_trt_supported_system as is_trt_supported_system
from .engine_accelerator import Accelerator as Accelerator, Engine as Engine
from .model_config import ModelConfig as ModelConfig
from .processing import ProcessorT as ProcessorT, load_trt_plugin as load_trt_plugin
from .tools import is_jetson_agx_orin as is_jetson_agx_orin, is_jetson_agx_xavier as is_jetson_agx_xavier, is_jetson_nano as is_jetson_nano, is_jetson_orin_nx as is_jetson_orin_nx, is_jetson_xavier_nx as is_jetson_xavier_nx, is_opencv_cuda_available as is_opencv_cuda_available
from _typeshed import Incomplete
from edgeiq import runtime as runtime
from typing import Generic, List, Optional

def get_opencv_engine(engine: Engine): ...
def get_opencv_accelerator(accelerator: Accelerator): ...

SUPPORTED_ACCELERATOR: Incomplete
SUPPORTED_OPENCV_ENGINE: Incomplete
HAILO_SUPPORTED_ARCHITECTURES: Incomplete
QAIC_SUPPORTED_ARCHITECTURES: Incomplete

def validate_engine_accelerator(engine: Engine, accelerator: Accelerator, model_config: ModelConfig) -> Accelerator: ...
def get_inference_runtime(engine: Engine, accelerator: Accelerator, model_config: ModelConfig): ...

class BaseService(Generic[ProcessorT]):
    def __init__(self, model_config: ModelConfig, processor: ProcessorT) -> None: ...
    def load(self, engine: Engine = ..., accelerator: Accelerator = ...): ...
    @property
    def labels(self) -> Optional[List[str]]: ...
    @property
    def colors(self) -> Optional[np.ndarray]: ...
    @property
    def model_id(self) -> str: ...
    @property
    def model_purpose(self) -> str: ...
    @property
    def model_config(self) -> ModelConfig: ...
    @property
    def engine(self) -> Optional[Engine]: ...
    @property
    def accelerator(self) -> Optional[Accelerator]: ...
