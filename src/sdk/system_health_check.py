"""
system_health_check automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union


class SystemHealthCheck(BaseModel):
    healthy: Optional[bool] = Field(default=None, alias="healthy")
    error: Optional[str] = Field(default=None, alias="error")
    pass


