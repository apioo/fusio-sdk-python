"""
backend_cronjob automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from common_metadata import CommonMetadata
from backend_cronjob_error import BackendCronjobError
@dataclass_json
@dataclass
class BackendCronjob:
    id: int
    name: str
    cron: str
    action: str
    execute_date: datetime.datetime
    exit_code: int
    metadata: CommonMetadata
    errors: List[BackendCronjobError]