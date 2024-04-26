import numpy as np
from _typeshed import Incomplete
from edgeiq._production_client import PRODUCTION_CLIENT as PRODUCTION_CLIENT
from edgeiq.tools import to_json_serializable as to_json_serializable
from typing import Any

class QRCodeDetectionPrediction:
    def __init__(self, box: np.ndarray, info: str) -> None: ...
    def __eq__(self, other) -> bool: ...
    @property
    def box(self) -> np.ndarray: ...
    @property
    def info(self) -> str: ...

class QRCodeDetectionResults:
    def __init__(self, predictions: list[QRCodeDetectionPrediction], image: np.ndarray | None) -> None: ...
    def __eq__(self, other) -> bool: ...
    @property
    def predictions(self) -> list[QRCodeDetectionPrediction]: ...
    @property
    def image(self) -> np.ndarray | None: ...
    def markup_image(self) -> np.ndarray | None: ...

RESULT_TYPE: Incomplete

class QRCodeDetection:
    qrcode_reader: Incomplete
    def __init__(self) -> None: ...
    def localize_decode(self, image: np.ndarray) -> QRCodeDetectionResults: ...
    def publish_analytics(self, results: QRCodeDetectionResults, tag: Any = None): ...
