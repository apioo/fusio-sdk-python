"""
backend_rate automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .backend_rate_allocation import BackendRateAllocation
from .common_metadata import CommonMetadata


# This object represents a rate limitation, which allows to limit the requests which a user can send
class BackendRate(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    priority: Optional[int] = Field(default=None, alias="priority")
    name: Optional[str] = Field(default=None, alias="name")
    rate_limit: Optional[int] = Field(default=None, alias="rateLimit")
    timespan: Optional[str] = Field(default=None, alias="timespan")
    allocation: Optional[List[BackendRateAllocation]] = Field(default=None, alias="allocation")
    metadata: Optional[CommonMetadata] = Field(default=None, alias="metadata")
    pass


