"""
backend_scope_category automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from backend_scope_category_scope import BackendScopeCategoryScope
@dataclass_json
@dataclass
class BackendScopeCategory:
    id: int
    name: str
    scopes: List[BackendScopeCategoryScope]
