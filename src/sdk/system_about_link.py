"""
system_about_link automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
class SystemAboutLink(BaseModel):
    rel: Optional[str] = Field(default=None, alias="rel")
    href: Optional[str] = Field(default=None, alias="href")
    pass
