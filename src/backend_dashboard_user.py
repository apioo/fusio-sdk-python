"""
backend_dashboard_user automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
@dataclass_json
@dataclass
class BackendDashboardUser:
    id: int
    status: str
    name: str
    date: datetime.datetime
