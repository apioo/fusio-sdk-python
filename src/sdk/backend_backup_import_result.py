"""
backend_backup_import_result automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
class BackendBackupImportResult(BaseModel):
    success: Optional[bool] = Field(default=None, alias="success")
    message: Optional[str] = Field(default=None, alias="message")
    logs: Optional[List[str]] = Field(default=None, alias="logs")
    pass
