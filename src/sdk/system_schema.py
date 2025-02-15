"""
system_schema automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .system_schema_type_schema import SystemSchemaTypeSchema
from .system_schema_form import SystemSchemaForm


class SystemSchema(BaseModel):
    schema_: Optional[SystemSchemaTypeSchema] = Field(default=None, alias="schema")
    form: Optional[SystemSchemaForm] = Field(default=None, alias="form")
    pass


