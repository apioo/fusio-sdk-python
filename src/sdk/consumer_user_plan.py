"""
consumer_user_plan automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
@dataclass_json
@dataclass
class ConsumerUserPlan:
    id: int
    name: str
    price: int
    points: int
    period: int