"""
consumer_user_password_reset automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
@dataclass_json
@dataclass
class ConsumerUserPasswordReset:
    token: str = field(metadata=config(field_name="token"))
    new_password: str = field(metadata=config(field_name="newPassword"))
