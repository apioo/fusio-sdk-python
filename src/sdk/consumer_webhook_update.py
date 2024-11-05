"""
consumer_webhook_update automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, UserList, UserDict


class ConsumerWebhookUpdate(BaseModel):
    event: Optional[str] = Field(default=None, alias="event")
    name: Optional[str] = Field(default=None, alias="name")
    endpoint: Optional[str] = Field(default=None, alias="endpoint")
    pass


