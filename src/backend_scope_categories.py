"""
backend_scope_categories automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from backend_scope_category import BackendScopeCategory
@dataclass_json
@dataclass
class BackendScopeCategories:
    categories: List[BackendScopeCategory]
