"""
backend_config_collection automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from common_collection import CommonCollection
from backend_config import BackendConfig
@dataclass_json
@dataclass
class BackendConfigCollection(CommonCollection[BackendConfig]):
    pass
