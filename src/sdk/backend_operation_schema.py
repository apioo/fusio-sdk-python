"""
backend_operation_schema automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union


class BackendOperationSchema(BaseModel):
    description: Optional[str] = Field(default=None, alias="description")
    type: Optional[str] = Field(default=None, alias="type")
    format: Optional[str] = Field(default=None, alias="format")
    enum: Optional[str] = Field(default=None, alias="enum")
    pass


