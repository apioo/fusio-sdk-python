"""
backend_operation automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .backend_operation_parameters import BackendOperationParameters
from .backend_operation_throws import BackendOperationThrows
from .common_metadata import CommonMetadata


# This object represents an operation, an operation invokes an action in case a specific HTTP method and path was requested. It defines also schema information about the request and response payload
class BackendOperation(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    status: Optional[int] = Field(default=None, alias="status")
    active: Optional[bool] = Field(default=None, alias="active")
    public: Optional[bool] = Field(default=None, alias="public")
    stability: Optional[int] = Field(default=None, alias="stability")
    description: Optional[str] = Field(default=None, alias="description")
    http_method: Optional[str] = Field(default=None, alias="httpMethod")
    http_path: Optional[str] = Field(default=None, alias="httpPath")
    http_code: Optional[int] = Field(default=None, alias="httpCode")
    name: Optional[str] = Field(default=None, alias="name")
    parameters: Optional[BackendOperationParameters] = Field(default=None, alias="parameters")
    incoming: Optional[str] = Field(default=None, alias="incoming")
    outgoing: Optional[str] = Field(default=None, alias="outgoing")
    throws: Optional[BackendOperationThrows] = Field(default=None, alias="throws")
    action: Optional[str] = Field(default=None, alias="action")
    costs: Optional[int] = Field(default=None, alias="costs")
    scopes: Optional[List[str]] = Field(default=None, alias="scopes")
    metadata: Optional[CommonMetadata] = Field(default=None, alias="metadata")
    pass


