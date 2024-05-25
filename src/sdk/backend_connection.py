"""
backend_connection automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
from .backend_connection_config import BackendConnectionConfig
from .common_metadata import CommonMetadata
class BackendConnection(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    class_: Optional[str] = Field(default=None, alias="class")
    oauth_: Optional[bool] = Field(default=None, alias="oauth2")
    config: Optional[BackendConnectionConfig] = Field(default=None, alias="config")
    metadata: Optional[CommonMetadata] = Field(default=None, alias="metadata")
    pass
