"""
backend_database_table automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, UserList, UserDict
from .backend_database_table_column import BackendDatabaseTableColumn
from .backend_database_table_index import BackendDatabaseTableIndex
from .backend_database_table_foreign_key_constraint import BackendDatabaseTableForeignKeyConstraint


class BackendDatabaseTable(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    columns: Optional[List[BackendDatabaseTableColumn]] = Field(default=None, alias="columns")
    primary_key: Optional[str] = Field(default=None, alias="primaryKey")
    indexes: Optional[List[BackendDatabaseTableIndex]] = Field(default=None, alias="indexes")
    foreign_keys: Optional[List[BackendDatabaseTableForeignKeyConstraint]] = Field(default=None, alias="foreignKeys")
    pass


