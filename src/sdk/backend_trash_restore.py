"""
backend_trash_restore automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
class BackendTrashRestore(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    pass
