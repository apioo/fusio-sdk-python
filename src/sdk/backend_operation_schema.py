"""
backend_operation_schema automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
@dataclass_json
@dataclass
class BackendOperationSchema:
    description: str
    type: str
    format: str
    enum: str
