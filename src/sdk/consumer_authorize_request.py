"""
consumer_authorize_request automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union


class ConsumerAuthorizeRequest(BaseModel):
    response_type: Optional[str] = Field(default=None, alias="responseType")
    client_id: Optional[str] = Field(default=None, alias="clientId")
    redirect_uri: Optional[str] = Field(default=None, alias="redirectUri")
    scope: Optional[str] = Field(default=None, alias="scope")
    state: Optional[str] = Field(default=None, alias="state")
    allow: Optional[bool] = Field(default=None, alias="allow")
    pass


