"""
consumer_app_update automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union


class ConsumerAppUpdate(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    url: Optional[str] = Field(default=None, alias="url")
    scopes: Optional[List[str]] = Field(default=None, alias="scopes")
    pass


