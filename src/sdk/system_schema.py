"""
system_schema automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from system_schema_type_schema import SystemSchemaTypeSchema
from system_schema_form import SystemSchemaForm
@dataclass_json
@dataclass
class SystemSchema:
    schema: SystemSchemaTypeSchema
    form: SystemSchemaForm