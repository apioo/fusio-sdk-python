"""
backend_sdk_response automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
from .backend_sdk_types import BackendSdkTypes
class BackendSdkResponse(BaseModel):
    types: Optional[BackendSdkTypes] = Field(default=None, alias="types")
    pass
