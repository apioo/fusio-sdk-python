"""
backend_log automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, UserList, UserDict
import datetime
from .backend_log_error import BackendLogError


class BackendLog(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    ip: Optional[str] = Field(default=None, alias="ip")
    user_agent: Optional[str] = Field(default=None, alias="userAgent")
    method: Optional[str] = Field(default=None, alias="method")
    path: Optional[str] = Field(default=None, alias="path")
    header: Optional[str] = Field(default=None, alias="header")
    body: Optional[str] = Field(default=None, alias="body")
    date: Optional[datetime.datetime] = Field(default=None, alias="date")
    errors: Optional[List[BackendLogError]] = Field(default=None, alias="errors")
    pass


