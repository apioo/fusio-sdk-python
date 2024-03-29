"""
backend_dashboard automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from backend_statistic_chart import BackendStatisticChart
from backend_dashboard_apps import BackendDashboardApps
from backend_dashboard_requests import BackendDashboardRequests
from backend_dashboard_users import BackendDashboardUsers
from backend_dashboard_transactions import BackendDashboardTransactions
@dataclass_json
@dataclass
class BackendDashboard:
    errors_per_operation: BackendStatisticChart
    incoming_requests: BackendStatisticChart
    incoming_transactions: BackendStatisticChart
    most_used_operations: BackendStatisticChart
    time_per_operation: BackendStatisticChart
    latest_apps: BackendDashboardApps
    latest_requests: BackendDashboardRequests
    latest_users: BackendDashboardUsers
    latest_transactions: BackendDashboardTransactions
