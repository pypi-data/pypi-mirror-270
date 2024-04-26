from edgeiq._utils import JsonFile
from typing import List

__all__ = ['AppConfig']

class AppFile(JsonFile):
    def __init__(self) -> None: ...
    @property
    def analytics_cfg(self): ...
    @property
    def qa_images_cfg(self): ...
    @property
    def device_agent_connection_cfg(self): ...
    @property
    def model_id_list(self): ...

class ProjectFile(JsonFile):
    def __init__(self) -> None: ...
    @property
    def project_id(self): ...

class AppConfig:
    def __init__(self) -> None: ...
    @property
    def model_id_list(self) -> List[str]: ...
    @property
    def analytics_cfg(self) -> dict | None: ...
    @property
    def qa_images_cfg(self) -> dict | None: ...
    @property
    def device_agent_connection_cfg(self) -> dict | None: ...
    @property
    def project_id(self) -> str: ...
