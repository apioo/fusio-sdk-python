"""
backend_database_table_foreign_key_constraint automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union


# This object represents a foreign key constraint on a relational database
class BackendDatabaseTableForeignKeyConstraint(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    foreign_table: Optional[str] = Field(default=None, alias="foreignTable")
    local_column_names: Optional[List[str]] = Field(default=None, alias="localColumnNames")
    foreign_column_names: Optional[List[str]] = Field(default=None, alias="foreignColumnNames")
    pass


