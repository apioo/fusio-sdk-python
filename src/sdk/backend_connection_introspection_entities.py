"""
backend_connection_introspection_entities automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, UserList, UserDict


class BackendConnectionIntrospectionEntities(BaseModel):
    entities: Optional[List[str]] = Field(default=None, alias="entities")
    pass


