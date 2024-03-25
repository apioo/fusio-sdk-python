"""
backend_app automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from common_metadata import CommonMetadata
from backend_token import BackendToken
@dataclass_json
@dataclass
class BackendApp:
    id: int
    user_id: int
    status: int
    name: str
    url: str
    parameters: str
    app_key: str
    app_secret: str
    metadata: CommonMetadata
    date: datetime.datetime
    scopes: List[str]
    tokens: List[BackendToken]