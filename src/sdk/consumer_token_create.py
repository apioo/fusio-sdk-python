"""
consumer_token_create automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
import datetime


class ConsumerTokenCreate(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    scopes: Optional[List[str]] = Field(default=None, alias="scopes")
    expire: Optional[datetime.date] = Field(default=None, alias="expire")
    pass


