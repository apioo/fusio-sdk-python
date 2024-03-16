"""
consumer_webhook automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from consumer_webhook_response import ConsumerWebhookResponse
@dataclass_json
@dataclass
class ConsumerWebhook:
    id: int
    status: int
    event: str
    name: str
    endpoint: str
    responses: List[ConsumerWebhookResponse]
