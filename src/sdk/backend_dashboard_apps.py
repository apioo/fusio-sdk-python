"""
backend_dashboard_apps automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from .common_collection import CommonCollection
from .backend_dashboard_app import BackendDashboardApp
@dataclass_json
@dataclass
class BackendDashboardApps(CommonCollection[BackendDashboardApp]):
    pass
