"""
consumer_webhook automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .consumer_webhook_response import ConsumerWebhookResponse


class ConsumerWebhook(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    status: Optional[int] = Field(default=None, alias="status")
    event: Optional[str] = Field(default=None, alias="event")
    name: Optional[str] = Field(default=None, alias="name")
    endpoint: Optional[str] = Field(default=None, alias="endpoint")
    responses: Optional[List[ConsumerWebhookResponse]] = Field(default=None, alias="responses")
    pass


