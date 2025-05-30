"""
marketplace_app automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .marketplace_object import MarketplaceObject


class MarketplaceApp(MarketplaceObject):
    scopes: Optional[List[str]] = Field(default=None, alias="scopes")
    download_url: Optional[str] = Field(default=None, alias="downloadUrl")
    hash: Optional[str] = Field(default=None, alias="hash")
    pass


