"""
consumer_log_collection automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .common_collection import CommonCollection
from .consumer_log import ConsumerLog


class ConsumerLogCollection(CommonCollection[ConsumerLog]):
    pass


