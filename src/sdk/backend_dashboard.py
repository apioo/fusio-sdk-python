"""
backend_dashboard automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
from .backend_statistic_chart import BackendStatisticChart
from .backend_dashboard_apps import BackendDashboardApps
from .backend_dashboard_requests import BackendDashboardRequests
from .backend_dashboard_users import BackendDashboardUsers
class BackendDashboard(BaseModel):
    errors_per_operation: Optional[BackendStatisticChart] = Field(default=None, alias="errorsPerOperation")
    incoming_requests: Optional[BackendStatisticChart] = Field(default=None, alias="incomingRequests")
    incoming_transactions: Optional[BackendStatisticChart] = Field(default=None, alias="incomingTransactions")
    most_used_operations: Optional[BackendStatisticChart] = Field(default=None, alias="mostUsedOperations")
    time_per_operation: Optional[BackendStatisticChart] = Field(default=None, alias="timePerOperation")
    test_coverage: Optional[BackendStatisticChart] = Field(default=None, alias="testCoverage")
    latest_apps: Optional[BackendDashboardApps] = Field(default=None, alias="latestApps")
    latest_requests: Optional[BackendDashboardRequests] = Field(default=None, alias="latestRequests")
    latest_users: Optional[BackendDashboardUsers] = Field(default=None, alias="latestUsers")
    pass
