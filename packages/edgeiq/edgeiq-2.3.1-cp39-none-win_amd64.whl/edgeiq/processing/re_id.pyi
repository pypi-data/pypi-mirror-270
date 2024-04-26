import numpy as np
from edgeiq.model_config.model_config import ModelConfig
from edgeiq.processing.processor import Processor

__all__ = ['ReIdentificationProcessor']

class ReIdentificationProcessor(Processor):
    def __init__(self, model_config: ModelConfig) -> None: ...
    def load(self) -> None: ...
    def pre_process(self, image: np.ndarray): ...
