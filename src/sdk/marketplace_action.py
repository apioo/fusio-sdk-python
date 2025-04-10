"""
marketplace_action automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .marketplace_object import MarketplaceObject
from .marketplace_action_config import MarketplaceActionConfig


class MarketplaceAction(MarketplaceObject):
    class_: Optional[str] = Field(default=None, alias="class")
    config: Optional[MarketplaceActionConfig] = Field(default=None, alias="config")
    pass


