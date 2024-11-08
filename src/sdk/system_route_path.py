"""
system_route_path automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, UserList, UserDict
from .system_route_method import SystemRouteMethod


class SystemRoutePath(UserDict[str, SystemRouteMethod]):
    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler: GetCoreSchemaHandler) -> CoreSchema:
        return core_schema.dict_schema(handler.generate_schema(str), handler.generate_schema(SystemRouteMethod))


