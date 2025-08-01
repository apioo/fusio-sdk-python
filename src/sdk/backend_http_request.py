"""
backend_http_request automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union


# This object represents a HTTP request
class BackendHttpRequest(BaseModel):
    method: Optional[str] = Field(default=None, alias="method")
    uri: Optional[str] = Field(default=None, alias="uri")
    headers: Optional[Dict[str, str]] = Field(default=None, alias="headers")
    body: Optional[str] = Field(default=None, alias="body")
    pass


