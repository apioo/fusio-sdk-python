"""
backend_rate_collection automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, UserList, UserDict
from .common_collection import CommonCollection
from .backend_rate import BackendRate


class BackendRateCollection(CommonCollection[BackendRate]):
    pass


