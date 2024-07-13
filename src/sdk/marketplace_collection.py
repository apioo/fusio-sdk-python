"""
marketplace_collection automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
T = TypeVar("T")
class MarketplaceCollection(BaseModel, Generic[T]):
    total_results: Optional[int] = Field(default=None, alias="totalResults")
    start_index: Optional[int] = Field(default=None, alias="startIndex")
    items_per_page: Optional[int] = Field(default=None, alias="itemsPerPage")
    entry: Optional[List[T]] = Field(default=None, alias="entry")
    pass