"""
backend_connection_introspection_entities automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import List
@dataclass_json
@dataclass
class BackendConnectionIntrospectionEntities:
    entities: List[str] = field(default=None, metadata=config(field_name="entities"))
