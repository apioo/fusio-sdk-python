"""
consumer_identity automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union


class ConsumerIdentity(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    icon: Optional[str] = Field(default=None, alias="icon")
    redirect: Optional[str] = Field(default=None, alias="redirect")
    pass


