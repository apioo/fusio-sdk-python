"""
backend_dashboard_app automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
import datetime
class BackendDashboardApp(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    date: Optional[datetime.datetime] = Field(default=None, alias="date")
    pass
