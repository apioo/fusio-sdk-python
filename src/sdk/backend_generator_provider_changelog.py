"""
backend_generator_provider_changelog automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import List
from backend_schema import BackendSchema
from backend_action import BackendAction
from backend_operation import BackendOperation
@dataclass_json
@dataclass
class BackendGeneratorProviderChangelog:
    schemas: List[BackendSchema] = field(default=None, metadata=config(field_name="schemas"))
    actions: List[BackendAction] = field(default=None, metadata=config(field_name="actions"))
    operations: List[BackendOperation] = field(default=None, metadata=config(field_name="operations"))
