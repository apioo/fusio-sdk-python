"""
backend_cronjob_error automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
@dataclass_json
@dataclass
class BackendCronjobError:
    message: str
    trace: str
    file: str
    line: int
