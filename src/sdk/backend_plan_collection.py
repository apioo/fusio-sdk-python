"""
backend_plan_collection automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .common_collection import CommonCollection
from .backend_plan import BackendPlan


class BackendPlanCollection(CommonCollection[BackendPlan]):
    pass


