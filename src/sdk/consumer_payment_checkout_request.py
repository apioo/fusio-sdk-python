"""
consumer_payment_checkout_request automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
@dataclass_json
@dataclass
class ConsumerPaymentCheckoutRequest:
    plan_id: int
    return_url: str