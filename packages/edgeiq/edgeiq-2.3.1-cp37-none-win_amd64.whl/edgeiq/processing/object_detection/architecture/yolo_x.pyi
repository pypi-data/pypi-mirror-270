import numpy as np
from ..types import ObjectDetectionPostProcessParams as ObjectDetectionPostProcessParams, ObjectDetectionPreProcessParams as ObjectDetectionPreProcessParams
from edgeiq.bounding_box import BoundingBox as BoundingBox

def nms(boxes, scores, nms_thr): ...
def multiclass_nms(boxes, scores, nms_thr, score_thr): ...
def yolox_pre_process(params: ObjectDetectionPreProcessParams) -> np.ndarray: ...
def yolox_pre_process_trt(params: ObjectDetectionPreProcessParams) -> np.ndarray: ...
def yolox_post_process(params: ObjectDetectionPostProcessParams): ...
