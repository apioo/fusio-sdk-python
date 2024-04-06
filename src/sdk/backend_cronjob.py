"""
backend_cronjob automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import List
from .common_metadata import CommonMetadata
from .backend_cronjob_error import BackendCronjobError
@dataclass_json
@dataclass
class BackendCronjob:
    id: int = field(default=None, metadata=config(field_name="id"))
    name: str = field(default=None, metadata=config(field_name="name"))
    cron: str = field(default=None, metadata=config(field_name="cron"))
    action: str = field(default=None, metadata=config(field_name="action"))
    execute_date: datetime.datetime = field(default=None, metadata=config(field_name="executeDate"))
    exit_code: int = field(default=None, metadata=config(field_name="exitCode"))
    metadata: CommonMetadata = field(default=None, metadata=config(field_name="metadata"))
    errors: List[BackendCronjobError] = field(default=None, metadata=config(field_name="errors"))
