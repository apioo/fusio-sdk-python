"""
backend_identity_collection automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from common_collection import CommonCollection
from backend_identity import BackendIdentity
@dataclass_json
@dataclass
class BackendIdentityCollection(CommonCollection[BackendIdentity]):
    pass
