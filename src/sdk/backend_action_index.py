"""
backend_action_index automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import List
from backend_action_index_entry import BackendActionIndexEntry
@dataclass_json
@dataclass
class BackendActionIndex:
    actions: List[BackendActionIndexEntry] = field(default=None, metadata=config(field_name="actions"))
