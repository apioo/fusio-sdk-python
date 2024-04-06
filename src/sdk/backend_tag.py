"""
BackendTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException

from .backend_account_tag import BackendAccountTag
from .backend_action_tag import BackendActionTag
from .backend_app_tag import BackendAppTag
from .backend_audit_tag import BackendAuditTag
from .backend_backup_tag import BackendBackupTag
from .backend_category_tag import BackendCategoryTag
from .backend_config_tag import BackendConfigTag
from .backend_connection_tag import BackendConnectionTag
from .backend_cronjob_tag import BackendCronjobTag
from .backend_dashboard_tag import BackendDashboardTag
from .backend_event_tag import BackendEventTag
from .backend_generator_tag import BackendGeneratorTag
from .backend_identity_tag import BackendIdentityTag
from .backend_log_tag import BackendLogTag
from .backend_marketplace_tag import BackendMarketplaceTag
from .backend_operation_tag import BackendOperationTag
from .backend_page_tag import BackendPageTag
from .backend_plan_tag import BackendPlanTag
from .backend_rate_tag import BackendRateTag
from .backend_role_tag import BackendRoleTag
from .backend_schema_tag import BackendSchemaTag
from .backend_scope_tag import BackendScopeTag
from .backend_sdk_tag import BackendSdkTag
from .backend_statistic_tag import BackendStatisticTag
from .backend_tenant_tag import BackendTenantTag
from .backend_token_tag import BackendTokenTag
from .backend_transaction_tag import BackendTransactionTag
from .backend_trash_tag import BackendTrashTag
from .backend_user_tag import BackendUserTag
from .backend_webhook_tag import BackendWebhookTag

class BackendTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)

    pass

    def webhook(self) -> BackendWebhookTag:
        return BackendWebhookTag(
            this.http_client,
            this.parser
        )

    pass

    def user(self) -> BackendUserTag:
        return BackendUserTag(
            this.http_client,
            this.parser
        )

    pass

    def trash(self) -> BackendTrashTag:
        return BackendTrashTag(
            this.http_client,
            this.parser
        )

    pass

    def transaction(self) -> BackendTransactionTag:
        return BackendTransactionTag(
            this.http_client,
            this.parser
        )

    pass

    def token(self) -> BackendTokenTag:
        return BackendTokenTag(
            this.http_client,
            this.parser
        )

    pass

    def tenant(self) -> BackendTenantTag:
        return BackendTenantTag(
            this.http_client,
            this.parser
        )

    pass

    def statistic(self) -> BackendStatisticTag:
        return BackendStatisticTag(
            this.http_client,
            this.parser
        )

    pass

    def sdk(self) -> BackendSdkTag:
        return BackendSdkTag(
            this.http_client,
            this.parser
        )

    pass

    def scope(self) -> BackendScopeTag:
        return BackendScopeTag(
            this.http_client,
            this.parser
        )

    pass

    def schema(self) -> BackendSchemaTag:
        return BackendSchemaTag(
            this.http_client,
            this.parser
        )

    pass

    def operation(self) -> BackendOperationTag:
        return BackendOperationTag(
            this.http_client,
            this.parser
        )

    pass

    def role(self) -> BackendRoleTag:
        return BackendRoleTag(
            this.http_client,
            this.parser
        )

    pass

    def rate(self) -> BackendRateTag:
        return BackendRateTag(
            this.http_client,
            this.parser
        )

    pass

    def plan(self) -> BackendPlanTag:
        return BackendPlanTag(
            this.http_client,
            this.parser
        )

    pass

    def page(self) -> BackendPageTag:
        return BackendPageTag(
            this.http_client,
            this.parser
        )

    pass

    def marketplace(self) -> BackendMarketplaceTag:
        return BackendMarketplaceTag(
            this.http_client,
            this.parser
        )

    pass

    def log(self) -> BackendLogTag:
        return BackendLogTag(
            this.http_client,
            this.parser
        )

    pass

    def identity(self) -> BackendIdentityTag:
        return BackendIdentityTag(
            this.http_client,
            this.parser
        )

    pass

    def generator(self) -> BackendGeneratorTag:
        return BackendGeneratorTag(
            this.http_client,
            this.parser
        )

    pass

    def backup(self) -> BackendBackupTag:
        return BackendBackupTag(
            this.http_client,
            this.parser
        )

    pass

    def event(self) -> BackendEventTag:
        return BackendEventTag(
            this.http_client,
            this.parser
        )

    pass

    def dashboard(self) -> BackendDashboardTag:
        return BackendDashboardTag(
            this.http_client,
            this.parser
        )

    pass

    def cronjob(self) -> BackendCronjobTag:
        return BackendCronjobTag(
            this.http_client,
            this.parser
        )

    pass

    def connection(self) -> BackendConnectionTag:
        return BackendConnectionTag(
            this.http_client,
            this.parser
        )

    pass

    def config(self) -> BackendConfigTag:
        return BackendConfigTag(
            this.http_client,
            this.parser
        )

    pass

    def category(self) -> BackendCategoryTag:
        return BackendCategoryTag(
            this.http_client,
            this.parser
        )

    pass

    def audit(self) -> BackendAuditTag:
        return BackendAuditTag(
            this.http_client,
            this.parser
        )

    pass

    def app(self) -> BackendAppTag:
        return BackendAppTag(
            this.http_client,
            this.parser
        )

    pass

    def action(self) -> BackendActionTag:
        return BackendActionTag(
            this.http_client,
            this.parser
        )

    pass

    def account(self) -> BackendAccountTag:
        return BackendAccountTag(
            this.http_client,
            this.parser
        )

    pass


