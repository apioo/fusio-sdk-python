"""
marketplace_app_collection automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, UserList, UserDict
from .marketplace_collection import MarketplaceCollection
from .marketplace_app import MarketplaceApp


class MarketplaceAppCollection(MarketplaceCollection[MarketplaceApp]):
    pass


