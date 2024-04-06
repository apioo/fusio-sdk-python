"""
backend_generator_provider automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import List
from backend_generator_provider_config import BackendGeneratorProviderConfig
@dataclass_json
@dataclass
class BackendGeneratorProvider:
    path: str = field(default=None, metadata=config(field_name="path"))
    scopes: List[str] = field(default=None, metadata=config(field_name="scopes"))
    public: bool = field(default=None, metadata=config(field_name="public"))
    config: BackendGeneratorProviderConfig = field(default=None, metadata=config(field_name="config"))
