"""
consumer_scope_category automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .consumer_scope_category_scope import ConsumerScopeCategoryScope


class ConsumerScopeCategory(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    scopes: Optional[List[ConsumerScopeCategoryScope]] = Field(default=None, alias="scopes")
    pass


