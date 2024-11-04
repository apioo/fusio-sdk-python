"""
system_o_auth_configuration automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, UserList, UserDict


class SystemOAuthConfiguration(BaseModel):
    issuer: Optional[str] = Field(default=None, alias="issuer")
    token_endpoint: Optional[str] = Field(default=None, alias="token_endpoint")
    token_endpoint_auth_methods_supported: Optional[List[str]] = Field(default=None, alias="token_endpoint_auth_methods_supported")
    userinfo_endpoint: Optional[str] = Field(default=None, alias="userinfo_endpoint")
    scopes_supported: Optional[List[str]] = Field(default=None, alias="scopes_supported")
    claims_supported: Optional[List[str]] = Field(default=None, alias="claims_supported")
    pass


