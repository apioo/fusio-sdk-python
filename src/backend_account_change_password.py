"""
backend_account_change_password automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
@dataclass_json
@dataclass
class BackendAccountChangePassword:
    old_password: str
    new_password: str
    verify_password: str
