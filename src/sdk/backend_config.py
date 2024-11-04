"""
backend_config automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, UserList, UserDict


class BackendConfig(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    type: Optional[int] = Field(default=None, alias="type")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    value: Optional[Any] = Field(default=None, alias="value")
    pass


