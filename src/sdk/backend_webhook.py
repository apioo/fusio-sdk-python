"""
backend_webhook automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import List
from .backend_webhook_response import BackendWebhookResponse
@dataclass_json
@dataclass
class BackendWebhook:
    id: int = field(default=None, metadata=config(field_name="id"))
    event_id: int = field(default=None, metadata=config(field_name="eventId"))
    user_id: int = field(default=None, metadata=config(field_name="userId"))
    name: str = field(default=None, metadata=config(field_name="name"))
    endpoint: str = field(default=None, metadata=config(field_name="endpoint"))
    responses: List[BackendWebhookResponse] = field(default=None, metadata=config(field_name="responses"))
