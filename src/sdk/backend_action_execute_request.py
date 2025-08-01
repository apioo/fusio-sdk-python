"""
backend_action_execute_request automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .backend_action_execute_request_body import BackendActionExecuteRequestBody


# Represents a request to execute an action
class BackendActionExecuteRequest(BaseModel):
    method: Optional[str] = Field(default=None, alias="method")
    uri_fragments: Optional[str] = Field(default=None, alias="uriFragments")
    parameters: Optional[str] = Field(default=None, alias="parameters")
    headers: Optional[str] = Field(default=None, alias="headers")
    body: Optional[BackendActionExecuteRequestBody] = Field(default=None, alias="body")
    pass


