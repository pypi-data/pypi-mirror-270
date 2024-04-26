import numpy as np
from .tracking_results import TrackingResults as TrackingResults
from _typeshed import Incomplete
from edgeiq._utils import gen_logger as gen_logger
from edgeiq.bounding_box import BoundingBox as BoundingBox
from edgeiq.object_detection import ObjectDetectionPrediction as ObjectDetectionPrediction
from typing import Callable, Generic, List, Optional, Tuple, Type, TypeVar

DEFAULT_DEREGISTER_FRAMES: int
DEFAULT_MAX_DISTANCE: int
DEFAULT_MIN_INERTIA: int
DEFAULT_HISTORY_LENGTH: int
PredictionT = ObjectDetectionPrediction

class TrackablePrediction(PredictionT):
    tracker_init_id: int
    tracker_id: int
    prediction: Incomplete
    deregister_frames: Incomplete
    min_inertia: Incomplete
    tid: Incomplete
    inertia: int
    hits: int
    age: int
    disappeared_frames: int
    def __init__(self, prediction: PredictionT, deregister_frames: int, min_inertia: int, history_length: int, enter_cb: Optional['TrackerCbT'] = ..., exit_cb: Optional['TrackerCbT'] = ...) -> None: ...
    def step(self, **kwargs) -> None: ...
    def handle_found(self, prediction: PredictionT): ...
    def handle_disappeared(self) -> None: ...
    def handle_removed(self) -> None: ...
    @property
    def is_initialized(self) -> bool: ...
    @property
    def is_lost(self) -> bool: ...
    @property
    def history(self) -> List[PredictionT]: ...
    @property
    def label(self) -> str: ...
    @property
    def index(self) -> int: ...
    @property
    def box(self) -> BoundingBox: ...
    @property
    def confidence(self) -> float: ...
TrackablePredictionT = TypeVar('TrackablePredictionT', bound=TrackablePrediction)
TrackerCbT = Callable[[int, TrackablePredictionT], None]

class TrackerAlgorithm(Generic[TrackablePredictionT]):
    def __init__(self, deregister_frames: int, min_inertia: int, history_length: int, enter_cb: Optional[TrackerCbT], exit_cb: Optional[TrackerCbT], trackable: Type[TrackablePredictionT], distance_function: Callable[[TrackablePredictionT, PredictionT], float], match_optimizer: Callable[[np.ndarray], List[Tuple[int, int]]]) -> None: ...
    def update(self, predictions: List[PredictionT], **trackable_kwargs) -> TrackingResults[TrackablePredictionT]: ...
    def remove_id(self, id: int): ...
