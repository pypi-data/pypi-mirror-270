import numpy as np
from ..types import ObjectDetectionPostProcessParams as ObjectDetectionPostProcessParams, ObjectDetectionPreProcessParams as ObjectDetectionPreProcessParams
from _typeshed import Incomplete
from edgeiq.bounding_box import BoundingBox as BoundingBox

def sigmoid(x): ...
def numpy_gather(data, dim, index): ...
def numpy_topk(arr, k): ...
def max_pool2d_numpy(input_array, kernel_size, stride: Incomplete | None = ..., padding: int = ...): ...
def get_3rd_point(a, b): ...
def get_affine_transform(center, scale, rot, output_size, shift=..., inv: int = ...): ...
def get_dir(src_point, rot_rad): ...
def affine_transform(pt, t): ...
def transform_preds(coords, center, scale, output_size): ...
def ctdet_decode(heat, wh, reg: Incomplete | None = ..., K: int = ...): ...
def centernet_pre_process(params: ObjectDetectionPreProcessParams) -> np.ndarray: ...
def centernet_pre_process_trt(params: ObjectDetectionPreProcessParams) -> np.ndarray: ...
def centernet_post_process(params: ObjectDetectionPostProcessParams): ...
