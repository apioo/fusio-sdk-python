"""
consumer_user_email automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union


class ConsumerUserEmail(BaseModel):
    email: Optional[str] = Field(default=None, alias="email")
    captcha: Optional[str] = Field(default=None, alias="captcha")
    pass


