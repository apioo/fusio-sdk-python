"""
backend_audit automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from backend_app import BackendApp
from backend_user import BackendUser
from backend_audit_object import BackendAuditObject
@dataclass_json
@dataclass
class BackendAudit:
    id: int
    app: BackendApp
    user: BackendUser
    event: str
    ip: str
    message: str
    content: BackendAuditObject
    date: datetime.datetime
