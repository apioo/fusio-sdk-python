"""
backend_connection_redirect_response automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, UserList, UserDict


class BackendConnectionRedirectResponse(BaseModel):
    redirect_uri: Optional[str] = Field(default=None, alias="redirectUri")
    pass


