import numpy as np
from _typeshed import Incomplete
from edgeiq import bounding_box as bounding_box
from edgeiq._production_client import PRODUCTION_CLIENT as PRODUCTION_CLIENT
from edgeiq.base_service import BaseService as BaseService
from edgeiq.engine_accelerator import Engine as Engine
from edgeiq.model_config import ModelConfig as ModelConfig
from edgeiq.object_detection import markup_image as markup_image
from edgeiq.processing import InstanceSegmentationProcessor as InstanceSegmentationProcessor
from edgeiq.tools import to_json_serializable as to_json_serializable
from typing import Any, List, Tuple

SUPPORTED_ENGINES: Incomplete

class InstanceSegmentationPrediction(bounding_box.BoundingBoxPrediction):
    def __init__(self, box: bounding_box.BoundingBox, mask: np.ndarray, contours: list, hierarchy: list, confidence: float, label: str, index: int) -> None: ...
    def __eq__(self, other) -> bool: ...
    @property
    def label(self) -> str: ...
    @label.setter
    def label(self, label: str): ...
    @property
    def index(self) -> int: ...
    @property
    def mask(self) -> np.ndarray: ...
    @property
    def contours(self) -> list: ...
    @property
    def hierarchy(self) -> list: ...

class InstanceSegmentationResults:
    def __init__(self, predictions: List[InstanceSegmentationPrediction], duration: float, image: np.ndarray, **kwargs) -> None: ...
    def __eq__(self, other) -> bool: ...
    @property
    def duration(self) -> float: ...
    @property
    def predictions(self) -> List[InstanceSegmentationPrediction]: ...
    @predictions.setter
    def predictions(self, predictions: List[InstanceSegmentationPrediction]): ...
    @property
    def image(self) -> np.ndarray: ...

RESULT_TYPE: Incomplete

class InstanceSegmentation(BaseService[InstanceSegmentationProcessor]):
    def __init__(self, model_id: str, model_config: ModelConfig | None = None) -> None: ...
    def segment_image(self, image: np.ndarray, confidence_level: float = 0.3) -> InstanceSegmentationResults: ...
    def markup_image(self, image: np.ndarray, predictions: List[InstanceSegmentationPrediction], show_labels: bool = True, show_confidences: bool = True, show_masks: bool = True, colors: List[Tuple[int, int, int]] | None = None, line_thickness: int = 2, font_size: float = 0.5, font_thickness: int = 2) -> np.ndarray: ...
    def publish_analytics(self, results: InstanceSegmentationResults, tag: Any = None): ...
