"""
backend_generator_provider_changelog automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .backend_schema import BackendSchema
from .backend_action import BackendAction
from .backend_operation import BackendOperation


class BackendGeneratorProviderChangelog(BaseModel):
    schemas: Optional[List[BackendSchema]] = Field(default=None, alias="schemas")
    actions: Optional[List[BackendAction]] = Field(default=None, alias="actions")
    operations: Optional[List[BackendOperation]] = Field(default=None, alias="operations")
    pass


