"""
consumer_payment_portal_request automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
@dataclass_json
@dataclass
class ConsumerPaymentPortalRequest:
    return_url: str = field(default=None, metadata=config(field_name="returnUrl"))
