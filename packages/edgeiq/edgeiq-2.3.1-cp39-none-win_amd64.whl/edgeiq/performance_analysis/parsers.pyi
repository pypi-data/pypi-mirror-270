from edgeiq.bounding_box import BoundingBox as BoundingBox
from edgeiq.object_detection import ObjectDetectionPrediction as ObjectDetectionPrediction

def parse_cvat_annotations(path: str, start_frame: int = 0, end_frame: int | None = None, new_id_for_occlusion: bool = False) -> tuple[dict, dict]: ...
