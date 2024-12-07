"""
backend_action_execute_response automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .backend_action_execute_response_headers import BackendActionExecuteResponseHeaders
from .backend_action_execute_response_body import BackendActionExecuteResponseBody


class BackendActionExecuteResponse(BaseModel):
    status_code: Optional[int] = Field(default=None, alias="statusCode")
    headers: Optional[BackendActionExecuteResponseHeaders] = Field(default=None, alias="headers")
    body: Optional[BackendActionExecuteResponseBody] = Field(default=None, alias="body")
    pass


