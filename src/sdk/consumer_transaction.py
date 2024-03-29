"""
consumer_transaction automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from consumer_plan import ConsumerPlan
@dataclass_json
@dataclass
class ConsumerTransaction:
    id: int
    user_id: int
    plan_id: int
    plan: ConsumerPlan
    transaction_id: str
    amount: float
    points: float
    period_start: datetime.datetime
    period_end: datetime.datetime
    insert_date: datetime.datetime
