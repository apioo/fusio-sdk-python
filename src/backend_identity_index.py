"""
backend_identity_index automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from backend_identity_index_entry import BackendIdentityIndexEntry
@dataclass_json
@dataclass
class BackendIdentityIndex:
    providers: List[BackendIdentityIndexEntry]
