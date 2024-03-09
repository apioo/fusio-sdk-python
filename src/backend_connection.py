"""
backend_connection automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from backend_connection_config import BackendConnectionConfig
from common_metadata import CommonMetadata
@dataclass_json
@dataclass
class BackendConnection:
    id: int
    name: str
    _class: str
    config: BackendConnectionConfig
    metadata: CommonMetadata
