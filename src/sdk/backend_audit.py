"""
backend_audit automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
import datetime
from .backend_app import BackendApp
from .backend_user import BackendUser
from .backend_audit_object import BackendAuditObject
@dataclass_json
@dataclass
class BackendAudit:
    id: int = field(default=None, metadata=config(field_name="id"))
    app: BackendApp = field(default=None, metadata=config(field_name="app"))
    user: BackendUser = field(default=None, metadata=config(field_name="user"))
    event: str = field(default=None, metadata=config(field_name="event"))
    ip: str = field(default=None, metadata=config(field_name="ip"))
    message: str = field(default=None, metadata=config(field_name="message"))
    content: BackendAuditObject = field(default=None, metadata=config(field_name="content"))
    date: datetime.datetime = field(default=None, metadata=config(field_name="date"))
