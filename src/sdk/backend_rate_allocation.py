"""
backend_rate_allocation automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
@dataclass_json
@dataclass
class BackendRateAllocation:
    id: int = field(metadata=config(field_name="id"))
    operation_id: int = field(metadata=config(field_name="operationId"))
    user_id: int = field(metadata=config(field_name="userId"))
    plan_id: int = field(metadata=config(field_name="planId"))
    app_id: int = field(metadata=config(field_name="appId"))
    authenticated: bool = field(metadata=config(field_name="authenticated"))
