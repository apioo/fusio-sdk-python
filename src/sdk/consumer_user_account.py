"""
consumer_user_account automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import List
from .consumer_user_plan import ConsumerUserPlan
from .common_metadata import CommonMetadata
@dataclass_json
@dataclass
class ConsumerUserAccount:
    id: int = field(default=None, metadata=config(field_name="id"))
    plan_id: int = field(default=None, metadata=config(field_name="planId"))
    status: int = field(default=None, metadata=config(field_name="status"))
    name: str = field(default=None, metadata=config(field_name="name"))
    email: str = field(default=None, metadata=config(field_name="email"))
    points: int = field(default=None, metadata=config(field_name="points"))
    scopes: List[str] = field(default=None, metadata=config(field_name="scopes"))
    plans: List[ConsumerUserPlan] = field(default=None, metadata=config(field_name="plans"))
    metadata: CommonMetadata = field(default=None, metadata=config(field_name="metadata"))
    date: datetime.datetime = field(default=None, metadata=config(field_name="date"))
