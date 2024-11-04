"""
backend_scope automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, UserList, UserDict
from .backend_scope_operation import BackendScopeOperation
from .common_metadata import CommonMetadata


class BackendScope(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    operations: Optional[List[BackendScopeOperation]] = Field(default=None, alias="operations")
    metadata: Optional[CommonMetadata] = Field(default=None, alias="metadata")
    pass


