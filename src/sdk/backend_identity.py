"""
backend_identity automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from .backend_identity_config import BackendIdentityConfig
@dataclass_json
@dataclass
class BackendIdentity:
    id: int = field(default=None, metadata=config(field_name="id"))
    app_id: int = field(default=None, metadata=config(field_name="appId"))
    role_id: int = field(default=None, metadata=config(field_name="roleId"))
    name: str = field(default=None, metadata=config(field_name="name"))
    icon: str = field(default=None, metadata=config(field_name="icon"))
    _class: str = field(default=None, metadata=config(field_name="class"))
    config: BackendIdentityConfig = field(default=None, metadata=config(field_name="config"))
    allow_create: bool = field(default=None, metadata=config(field_name="allowCreate"))
