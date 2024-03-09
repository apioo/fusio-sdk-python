"""
backend_schema automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from backend_schema_source import BackendSchemaSource
from backend_schema_form import BackendSchemaForm
from common_metadata import CommonMetadata
@dataclass_json
@dataclass
class BackendSchema:
    id: int
    status: int
    name: str
    source: BackendSchemaSource
    form: BackendSchemaForm
    metadata: CommonMetadata
