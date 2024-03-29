"""
backend_user automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from backend_app import BackendApp
from common_metadata import CommonMetadata
@dataclass_json
@dataclass
class BackendUser:
    id: int
    role_id: int
    plan_id: int
    status: int
    name: str
    email: str
    points: int
    scopes: List[str]
    apps: List[BackendApp]
    metadata: CommonMetadata
    date: datetime.datetime
