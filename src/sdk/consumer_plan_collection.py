"""
consumer_plan_collection automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from common_collection import CommonCollection
from consumer_plan import ConsumerPlan
@dataclass_json
@dataclass
class ConsumerPlanCollection(CommonCollection[ConsumerPlan]):
    pass