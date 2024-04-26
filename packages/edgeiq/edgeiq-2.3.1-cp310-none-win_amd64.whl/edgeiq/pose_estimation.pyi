import numpy as np
from _typeshed import Incomplete
from edgeiq._production_client import PRODUCTION_CLIENT as PRODUCTION_CLIENT
from edgeiq._utils import gen_logger as gen_logger
from edgeiq.base_service import BaseService as BaseService
from edgeiq.model_config import ModelConfig as ModelConfig
from edgeiq.pose_estimation_pose import Pose as Pose
from edgeiq.processing import PoseEstimationProcessor as PoseEstimationProcessor
from edgeiq.tools import to_json_serializable as to_json_serializable
from edgeiq.tools.image_manipulation import pad_to_aspect_ratio as pad_to_aspect_ratio
from typing import Any, List, Tuple

class HumanPoseResult:
    def __init__(self, poses: List[Pose], duration: float, input_dimension: Tuple[int, int], image: np.ndarray, **kwargs) -> None: ...
    def __eq__(self, other): ...
    @property
    def duration(self) -> float: ...
    @property
    def poses(self) -> List[Pose]: ...
    @property
    def image(self) -> np.ndarray: ...
    def draw_poses_background(self, color: Tuple[int, int, int]) -> np.ndarray: ...
    def draw_poses(self, image: np.ndarray | None = None) -> np.ndarray: ...
    def draw_aliens(self) -> np.ndarray: ...

RESULT_TYPE: Incomplete

class PoseEstimation(BaseService[PoseEstimationProcessor]):
    def __init__(self, model_id: str, model_config: ModelConfig | None = None) -> None: ...
    def estimate(self, image: np.ndarray) -> HumanPoseResult: ...
    def publish_analytics(self, results: HumanPoseResult, tag: Any = None): ...
