"""
consumer_user_register automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, UserList, UserDict


class ConsumerUserRegister(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    email: Optional[str] = Field(default=None, alias="email")
    password: Optional[str] = Field(default=None, alias="password")
    captcha: Optional[str] = Field(default=None, alias="captcha")
    pass


