
# fusio-sdk-python

This [SDK](https://github.com/apioo/fusio-sdk-python) is managed by the [SDK Fabric](https://sdk-fabric.org/) project, a global infrastructure to
automatically generate SDKs for every API.

You can find more information about this SDK at [TypeHub](https://typehub.cloud/):
https://app.typehub.cloud/d/fusio/sdk

## Usage

```python
from sdk.client import Client

client = Client.build("[access_token]")

# Returns user data of the current authenticated user.
response = client.authorization().get_whoami()

# Revoke the access token of the current authenticated user.
response = client.authorization().revoke()

# Changes the password of the authenticated user.
response = client.backend().account_change_password(BackendAccountchangepassword())

# Returns user data of the authenticated user.
response = client.backend().account_get()

# Updates user data of the authenticated user.
response = client.backend().account_update(BackendUserupdate())

# Creates a new action.
response = client.backend().action_create(BackendActioncreate())

# Deletes an existing action.
response = client.backend().action_delete("action_id")

# Executes a specific action.
response = client.backend().action_execute("action_id", BackendActionexecuterequest())

# Returns a specific action.
response = client.backend().action_get("action_id")

# Returns a paginated list of actions.
response = client.backend().action_get_all(1, 1, "search")

# Returns all available action classes.
response = client.backend().action_get_classes()

# Returns a paginated list of action commits.
response = client.backend().action_get_commits("action_id", 1, 1, "search")

# Returns the action config form.
response = client.backend().action_get_form("class")

# Updates an existing action.
response = client.backend().action_update("action_id", BackendActionupdate())

# Creates a new agent.
response = client.backend().agent_create(BackendAgentcreate())

# Deletes an existing agent.
response = client.backend().agent_delete("agent_id")

# Returns a specific agent.
response = client.backend().agent_get("agent_id")

# Returns a paginated list of agents.
response = client.backend().agent_get_all(1, 1, "search")

# Returns available tools for an agent.
response = client.backend().agent_get_tools()

# Returns a paginated list of agent messages.
response = client.backend().agent_message_get_all("agent_id", "chat_id")

# Submits a new agent message.
response = client.backend().agent_message_submit("agent_id", AgentInput())

# Updates an existing agent.
response = client.backend().agent_update("agent_id", BackendAgentupdate())

# Creates a new app.
response = client.backend().app_create(BackendAppcreate())

# Deletes an existing app.
response = client.backend().app_delete("app_id")

# Deletes an existing token from an app.
response = client.backend().app_delete_token("app_id", "token_id")

# Returns a specific app.
response = client.backend().app_get("app_id")

# Returns a paginated list of apps.
response = client.backend().app_get_all(1, 1, "search")

# Updates an existing app.
response = client.backend().app_update("app_id", BackendAppupdate())

# Returns a specific audit.
response = client.backend().audit_get("audit_id")

# Returns a paginated list of audits.
response = client.backend().audit_get_all(1, 1, "search", "from", "to", 1, 1, "event", "ip", "message")

# Generates an backup of the current system.
response = client.backend().backup_export()

# Imports an backup to the current system.
response = client.backend().backup_import(BackendBackupimport())

# Creates a new bundle.
response = client.backend().bundle_create(BackendBundlecreate())

# Deletes an existing bundle.
response = client.backend().bundle_delete("bundle_id")

# Returns a specific bundle.
response = client.backend().bundle_get("bundle_id")

# Returns a paginated list of bundles.
response = client.backend().bundle_get_all(1, 1, "search")

# Publish an existing bundle to the marketplace.
response = client.backend().bundle_publish("bundle_id")

# Updates an existing bundle.
response = client.backend().bundle_update("bundle_id", BackendBundleupdate())

# Creates a new category.
response = client.backend().category_create(BackendCategorycreate())

# Deletes an existing category.
response = client.backend().category_delete("category_id")

# Returns a specific category.
response = client.backend().category_get("category_id")

# Returns a paginated list of categories.
response = client.backend().category_get_all(1, 1, "search")

# Updates an existing category.
response = client.backend().category_update("category_id", BackendCategoryupdate())

# Returns a specific config.
response = client.backend().config_get("config_id")

# Returns a paginated list of configuration values.
response = client.backend().config_get_all(1, 1, "search")

# Updates an existing config value.
response = client.backend().config_update("config_id", BackendConfigupdate())

# Sends a message to an agent.
response = client.backend().connection_agent_send("connection_id", AgentInput())

# Creates a new connection.
response = client.backend().connection_create(BackendConnectioncreate())

# Creates a new row at a table on a database.
response = client.backend().connection_database_create_row("connection_id", "table_name", BackendDatabaserow())

# Creates a new table on a database.
response = client.backend().connection_database_create_table("connection_id", BackendDatabasetable())

# Deletes an existing row at a table on a database.
response = client.backend().connection_database_delete_row("connection_id", "table_name", "id")

# Deletes an existing table on a database.
response = client.backend().connection_database_delete_table("connection_id", "table_name")

# Returns a specific row at a table on a database.
response = client.backend().connection_database_get_row("connection_id", "table_name", "id")

# Returns paginated rows at a table on a database.
response = client.backend().connection_database_get_rows("connection_id", "table_name", 1, 1, "filter_by", "filter_op", "filter_value", "sort_by", "sort_order", "columns")

# Returns the schema of a specific table on a database.
response = client.backend().connection_database_get_table("connection_id", "table_name")

# Returns all available tables on a database.
response = client.backend().connection_database_get_tables("connection_id", 1, 1)

# Updates an existing row at a table on a database.
response = client.backend().connection_database_update_row("connection_id", "table_name", "id", BackendDatabaserow())

# Updates an existing table on a database.
response = client.backend().connection_database_update_table("connection_id", "table_name", BackendDatabasetable())

# Deletes an existing connection.
response = client.backend().connection_delete("connection_id")

# Uploads one or more files on the filesystem connection.
response = client.backend().connection_filesystem_create("connection_id", Any())

# Deletes an existing file on the filesystem connection.
response = client.backend().connection_filesystem_delete("connection_id", "file_id")

# Returns the content of the provided file id on the filesystem connection.
client.backend().connection_filesystem_get("connection_id", "file_id")

# Returns all available files on the filesystem connection.
response = client.backend().connection_filesystem_get_all("connection_id", 1, 1)

# Updates an existing file on the filesystem connection.
response = client.backend().connection_filesystem_update("connection_id", "file_id", Any())

# Returns a specific connection.
response = client.backend().connection_get("connection_id")

# Returns a paginated list of connections.
response = client.backend().connection_get_all(1, 1, "search", "class")

# Returns all available connection classes.
response = client.backend().connection_get_classes()

# Returns the connection config form.
response = client.backend().connection_get_form("class")

# Returns a redirect url to start the OAuth2 authorization flow for the given connection.
response = client.backend().connection_get_redirect("connection_id")

# Sends an arbitrary HTTP request to the connection.
response = client.backend().connection_http_execute("connection_id", BackendHttprequest())

# Returns the SDK specification.
response = client.backend().connection_sdk_get("connection_id")

# Updates an existing connection.
response = client.backend().connection_update("connection_id", BackendConnectionupdate())

# Creates a new cronjob.
response = client.backend().cronjob_create(BackendCronjobcreate())

# Deletes an existing cronjob.
response = client.backend().cronjob_delete("cronjob_id")

# Returns a specific cronjob.
response = client.backend().cronjob_get("cronjob_id")

# Returns a paginated list of cronjobs.
response = client.backend().cronjob_get_all(1, 1, "search", 1)

# Updates an existing cronjob.
response = client.backend().cronjob_update("cronjob_id", BackendCronjobupdate())

# Returns all available dashboard widgets.
response = client.backend().dashboard_get_all()

# Creates a new event.
response = client.backend().event_create(BackendEventcreate())

# Deletes an existing event.
response = client.backend().event_delete("event_id")

# Returns a specific event.
response = client.backend().event_get("event_id")

# Returns a paginated list of events.
response = client.backend().event_get_all(1, 1, "search", 1)

# Updates an existing event.
response = client.backend().event_update("event_id", BackendEventupdate())

# Creates a new firewall rule.
response = client.backend().firewall_create(BackendFirewallcreate())

# Deletes an existing firewall rule.
response = client.backend().firewall_delete("firewall_id")

# Returns a specific firewall rule.
response = client.backend().firewall_get("firewall_id")

# Returns a paginated list of firewall rules.
response = client.backend().firewall_get_all(1, 1, "search")

# Updates an existing firewall rule.
response = client.backend().firewall_update("firewall_id", BackendFirewallupdate())

# Creates a new form.
response = client.backend().form_create(BackendFormcreate())

# Deletes an existing form.
response = client.backend().form_delete("form_id")

# Returns a specific form.
response = client.backend().form_get("form_id")

# Returns a paginated list of forms.
response = client.backend().form_get_all(1, 1, "search")

# Updates an existing form.
response = client.backend().form_update("form_id", BackendFormupdate())

# Executes a generator with the provided config.
response = client.backend().generator_execute_provider("provider", BackendGeneratorprovider())

# Generates a changelog of all potential changes if you execute this generator with the provided config.
response = client.backend().generator_get_changelog("provider", BackendGeneratorproviderconfig())

# Returns all available generator classes.
response = client.backend().generator_get_classes()

# Returns the generator config form.
response = client.backend().generator_get_form("provider")

# Creates a new identity.
response = client.backend().identity_create(BackendIdentitycreate())

# Deletes an existing identity.
response = client.backend().identity_delete("identity_id")

# Returns a specific identity.
response = client.backend().identity_get("identity_id")

# Returns a paginated list of identities.
response = client.backend().identity_get_all(1, 1, "search")

# Returns all available identity classes.
response = client.backend().identity_get_classes()

# Returns the identity config form.
response = client.backend().identity_get_form("class")

# Updates an existing identity.
response = client.backend().identity_update("identity_id", BackendIdentityupdate())

# Returns a specific log.
response = client.backend().log_get("log_id")

# Returns a paginated list of logs.
response = client.backend().log_get_all(1, 1, "search", "from", "to", 1, 1, 1, "ip", "user_agent", "method", "path", "header", "body")

# Returns a paginated list of log errors.
response = client.backend().log_get_all_errors(1, 1, "search")

# Returns a specific error.
response = client.backend().log_get_error("error_id")

# Returns a specific marketplace action.
response = client.backend().marketplace_action_get("user", "name")

# Returns a paginated list of marketplace actions.
response = client.backend().marketplace_action_get_all(1, "query")

# Installs an action from the marketplace.
response = client.backend().marketplace_action_install(Marketplaceinstall())

# Upgrades an action from the marketplace.
response = client.backend().marketplace_action_upgrade("user", "name")

# Returns a specific marketplace app.
response = client.backend().marketplace_app_get("user", "name")

# Returns a paginated list of marketplace apps.
response = client.backend().marketplace_app_get_all(1, "query")

# Installs an app from the marketplace.
response = client.backend().marketplace_app_install(Marketplaceinstall())

# Upgrades an app from the marketplace.
response = client.backend().marketplace_app_upgrade("user", "name")

# Returns a specific marketplace bundle.
response = client.backend().marketplace_bundle_get("user", "name")

# Returns a paginated list of marketplace bundles.
response = client.backend().marketplace_bundle_get_all(1, "query")

# Installs an bundle from the marketplace.
response = client.backend().marketplace_bundle_install(Marketplaceinstall())

# Upgrades an bundle from the marketplace.
response = client.backend().marketplace_bundle_upgrade("user", "name")

# Creates a new operation.
response = client.backend().operation_create(BackendOperationcreate())

# Deletes an existing operation.
response = client.backend().operation_delete("operation_id")

# Returns a specific operation.
response = client.backend().operation_get("operation_id")

# Returns a paginated list of operations.
response = client.backend().operation_get_all(1, 1, "search", 1)

# Updates an existing operation.
response = client.backend().operation_update("operation_id", BackendOperationupdate())

# Creates a new page.
response = client.backend().page_create(BackendPagecreate())

# Deletes an existing page.
response = client.backend().page_delete("page_id")

# Returns a specific page.
response = client.backend().page_get("page_id")

# Returns a paginated list of pages.
response = client.backend().page_get_all(1, 1, "search")

# Updates an existing page.
response = client.backend().page_update("page_id", BackendPageupdate())

# Creates a new plan.
response = client.backend().plan_create(BackendPlancreate())

# Deletes an existing plan.
response = client.backend().plan_delete("plan_id")

# Returns a specific plan.
response = client.backend().plan_get("plan_id")

# Returns a paginated list of plans.
response = client.backend().plan_get_all(1, 1, "search")

# Updates an existing plan.
response = client.backend().plan_update("plan_id", BackendPlanupdate())

# Creates a new rate limitation.
response = client.backend().rate_create(BackendRatecreate())

# Deletes an existing rate.
response = client.backend().rate_delete("rate_id")

# Returns a specific rate.
response = client.backend().rate_get("rate_id")

# Returns a paginated list of rate limitations.
response = client.backend().rate_get_all(1, 1, "search")

# Updates an existing rate.
response = client.backend().rate_update("rate_id", BackendRateupdate())

# Creates a new role.
response = client.backend().role_create(BackendRolecreate())

# Deletes an existing role.
response = client.backend().role_delete("role_id")

# Returns a specific role.
response = client.backend().role_get("role_id")

# Returns a paginated list of roles.
response = client.backend().role_get_all(1, 1, "search")

# Updates an existing role.
response = client.backend().role_update("role_id", BackendRoleupdate())

# Creates a new schema.
response = client.backend().schema_create(BackendSchemacreate())

# Deletes an existing schema.
response = client.backend().schema_delete("schema_id")

# Returns a specific schema.
response = client.backend().schema_get("schema_id")

# Returns a paginated list of schemas.
response = client.backend().schema_get_all(1, 1, "search", 1)

# Returns a paginated list of schema commits.
response = client.backend().schema_get_commits("schema_id", 1, 1, "search")

# Returns a HTML preview of the provided schema.
response = client.backend().schema_get_preview("schema_id")

# Updates an existing schema.
response = client.backend().schema_update("schema_id", BackendSchemaupdate())

# Creates a new scope.
response = client.backend().scope_create(BackendScopecreate())

# Deletes an existing scope.
response = client.backend().scope_delete("scope_id")

# Returns a specific scope.
response = client.backend().scope_get("scope_id")

# Returns a paginated list of scopes.
response = client.backend().scope_get_all(1, 1, "search")

# Returns all available scopes grouped by category.
response = client.backend().scope_get_categories()

# Updates an existing scope.
response = client.backend().scope_update("scope_id", BackendScopeupdate())

# Generates a specific SDK.
response = client.backend().sdk_generate(BackendSdkgenerate())

# Returns a paginated list of SDKs.
response = client.backend().sdk_get_all()

# Returns the TypeHub specification.
response = client.backend().specification_get()

# Returns the changelog between your current specification and the last tag.
response = client.backend().specification_get_changelog()

# Publish the specification.
response = client.backend().specification_publish(BackendSpecificationpublish())

# Creates a new tag of your specification.
response = client.backend().specification_tag(Passthru())

# Returns a statistic containing the activities per user.
response = client.backend().statistic_get_activities_per_user(1, 1, "search", "from", "to", 1, 1, 1, "ip", "user_agent", "method", "path", "header", "body")

# Returns a statistic containing the request count.
response = client.backend().statistic_get_count_requests(1, 1, "search", "from", "to", 1, 1, 1, "ip", "user_agent", "method", "path", "header", "body")

# Returns a statistic containing the errors per operation.
response = client.backend().statistic_get_errors_per_operation(1, 1, "search", "from", "to", 1, 1, 1, "ip", "user_agent", "method", "path", "header", "body")

# Returns a statistic containing the incoming requests.
response = client.backend().statistic_get_incoming_requests(1, 1, "search", "from", "to", 1, 1, 1, "ip", "user_agent", "method", "path", "header", "body")

# Returns a statistic containing the incoming transactions.
response = client.backend().statistic_get_incoming_transactions(1, 1, "search", "from", "to", 1, 1, 1, "ip", "user_agent", "method", "path", "header", "body")

# Returns a statistic containing the issues tokens.
response = client.backend().statistic_get_issued_tokens(1, 1, "search", "from", "to", 1, 1, 1, "ip", "user_agent", "method", "path", "header", "body")

# Returns a statistic containing the most used activities.
response = client.backend().statistic_get_most_used_activities(1, 1, "search", "from", "to", 1, 1, 1, "ip", "user_agent", "method", "path", "header", "body")

# Returns a statistic containing the most used apps.
response = client.backend().statistic_get_most_used_apps(1, 1, "search", "from", "to", 1, 1, 1, "ip", "user_agent", "method", "path", "header", "body")

# Returns a statistic containing the most used operations.
response = client.backend().statistic_get_most_used_operations(1, 1, "search", "from", "to", 1, 1, 1, "ip", "user_agent", "method", "path", "header", "body")

# Returns a statistic containing the requests per ip.
response = client.backend().statistic_get_requests_per_ip(1, 1, "search", "from", "to", 1, 1, 1, "ip", "user_agent", "method", "path", "header", "body")

# Returns a statistic containing the requests per operation.
response = client.backend().statistic_get_requests_per_operation(1, 1, "search", "from", "to", 1, 1, 1, "ip", "user_agent", "method", "path", "header", "body")

# Returns a statistic containing the requests per user.
response = client.backend().statistic_get_requests_per_user(1, 1, "search", "from", "to", 1, 1, 1, "ip", "user_agent", "method", "path", "header", "body")

# Returns a statistic containing the test coverage.
response = client.backend().statistic_get_test_coverage()

# Returns a statistic containing the time average.
response = client.backend().statistic_get_time_average(1, 1, "search", "from", "to", 1, 1, 1, "ip", "user_agent", "method", "path", "header", "body")

# Returns a statistic containing the time per operation.
response = client.backend().statistic_get_time_per_operation(1, 1, "search", "from", "to", 1, 1, 1, "ip", "user_agent", "method", "path", "header", "body")

# Returns a statistic containing the used points.
response = client.backend().statistic_get_used_points(1, 1, "search", "from", "to", 1, 1, 1, "ip", "user_agent", "method", "path", "header", "body")

# Returns a statistic containing the user registrations.
response = client.backend().statistic_get_user_registrations(1, 1, "search", "from", "to", 1, 1, 1, "ip", "user_agent", "method", "path", "header", "body")

# Creates a new taxonomy.
response = client.backend().taxonomy_create(BackendTaxonomycreate())

# Deletes an existing taxonomy.
response = client.backend().taxonomy_delete("taxonomy_id")

# Returns a specific taxonomy.
response = client.backend().taxonomy_get("taxonomy_id")

# Returns a paginated list of taxonomies.
response = client.backend().taxonomy_get_all(1, 1, "search")

# Moves the provided ids to the taxonomy.
response = client.backend().taxonomy_move("taxonomy_id", BackendTaxonomymove())

# Updates an existing taxonomy.
response = client.backend().taxonomy_update("taxonomy_id", BackendTaxonomyupdate())

# Removes an existing tenant.
response = client.backend().tenant_remove("tenant_id")

# Setup a new tenant.
response = client.backend().tenant_setup("tenant_id")

# Returns a specific test.
response = client.backend().test_get("test_id")

# Returns a paginated list of tests.
response = client.backend().test_get_all(1, 1, "search")

# Refresh all tests.
response = client.backend().test_refresh()

# Run all tests.
response = client.backend().test_run()

# Updates an existing test.
response = client.backend().test_update("test_id", BackendTest())

# Returns a specific token.
response = client.backend().token_get("token_id")

# Returns a paginated list of tokens.
response = client.backend().token_get_all(1, 1, "search", "from", "to", 1, 1, 1, "scope", "ip")

# Returns a specific transaction.
response = client.backend().transaction_get("transaction_id")

# Returns a paginated list of transactions.
response = client.backend().transaction_get_all(1, 1, "search", "from", "to", 1, 1, 1, "status", "provider", 1)

# Returns all deleted records by trash type.
response = client.backend().trash_get_all_by_type("type", 1, 1, "search")

# Returns all trash types.
response = client.backend().trash_get_types()

# Restores a previously deleted record.
response = client.backend().trash_restore("type", BackendTrashrestore())

# Creates a new trigger.
response = client.backend().trigger_create(BackendTriggercreate())

# Deletes an existing trigger.
response = client.backend().trigger_delete("trigger_id")

# Returns a specific trigger.
response = client.backend().trigger_get("trigger_id")

# Returns a paginated list of triggers.
response = client.backend().trigger_get_all(1, 1, "search", 1)

# Updates an existing trigger.
response = client.backend().trigger_update("trigger_id", BackendTriggerupdate())

# Creates a new user.
response = client.backend().user_create(BackendUsercreate())

# Deletes an existing user.
response = client.backend().user_delete("user_id")

# Returns a specific user.
response = client.backend().user_get("user_id")

# Returns a paginated list of users.
response = client.backend().user_get_all(1, 1, "search")

# Resend the activation mail to the provided user.
response = client.backend().user_resend("user_id", Passthru())

# Updates an existing user.
response = client.backend().user_update("user_id", BackendUserupdate())

# Creates a new webhook.
response = client.backend().webhook_create(BackendWebhookcreate())

# Deletes an existing webhook.
response = client.backend().webhook_delete("webhook_id")

# Returns a specific webhook.
response = client.backend().webhook_get("webhook_id")

# Returns a paginated list of webhooks.
response = client.backend().webhook_get_all(1, 1, "search")

# Updates an existing webhook.
response = client.backend().webhook_update("webhook_id", BackendWebhookupdate())

# Activates an previously registered account through a token which was provided to the user via email.
response = client.consumer().account_activate(ConsumerUseractivate())

# Authorizes the access of a specific app for the authenticated user.
response = client.consumer().account_authorize(ConsumerAuthorizerequest())

# Change the password for the authenticated user.
response = client.consumer().account_change_password(BackendAccountchangepassword())

# Change the password after the password reset flow was started.
response = client.consumer().account_execute_password_reset(ConsumerUserpasswordreset())

# Returns a user data for the authenticated user.
response = client.consumer().account_get()

# Returns information about a specific app to start the OAuth2 authorization code flow.
response = client.consumer().account_get_app("client_id", "scope")

# User login by providing a username and password.
response = client.consumer().account_login(ConsumerUserlogin())

# Refresh a previously obtained access token.
response = client.consumer().account_refresh(ConsumerUserrefresh())

# Register a new user account.
response = client.consumer().account_register(ConsumerUserregister())

# Start the password reset flow.
response = client.consumer().account_request_password_reset(ConsumerUseremail())

# Updates user data for the authenticated user.
response = client.consumer().account_update(ConsumerUseraccount())

# Returns a specific agent.
response = client.consumer().agent_get("agent_id")

# Returns a paginated list of agents.
response = client.consumer().agent_get_all(1, 1, "search")

# Returns a paginated list of agent messages.
response = client.consumer().agent_message_get_all("agent_id", "chat_id")

# Submits a new agent message.
response = client.consumer().agent_message_submit("agent_id", AgentInput())

# Creates a new app for the authenticated user.
response = client.consumer().app_create(ConsumerAppcreate())

# Deletes an existing app for the authenticated user.
response = client.consumer().app_delete("app_id")

# Returns a specific app for the authenticated user.
response = client.consumer().app_get("app_id")

# Returns a paginated list of apps which are assigned to the authenticated user.
response = client.consumer().app_get_all(1, 1, "search")

# Updates an existing app for the authenticated user.
response = client.consumer().app_update("app_id", ConsumerAppupdate())

# Returns a specific event for the authenticated user.
response = client.consumer().event_get("event_id")

# Returns a paginated list of apps which are assigned to the authenticated user.
response = client.consumer().event_get_all(1, 1, "search")

# Returns a specific form for the authenticated user.
response = client.consumer().form_get("form_id")

# Returns a paginated list of forms which are relevant to the authenticated user.
response = client.consumer().form_get_all(1, 1, "search")

# Deletes an existing grant for an app which was created by the authenticated user.
response = client.consumer().grant_delete("grant_id")

# Returns a paginated list of grants which are assigned to the authenticated user.
response = client.consumer().grant_get_all(1, 1, "search")

# Identity callback endpoint to exchange an access token.
response = client.consumer().identity_exchange("identity")

# Returns a paginated list of identities which are relevant to the authenticated user.
response = client.consumer().identity_get_all(1, "app_key")

# Redirect the user to the configured identity provider.
response = client.consumer().identity_redirect("identity")

# Returns a specific log for the authenticated user.
response = client.consumer().log_get("log_id")

# Returns a paginated list of logs which are assigned to the authenticated user.
response = client.consumer().log_get_all(1, 1, "search")

# Returns a specific page for the authenticated user.
response = client.consumer().page_get("page_id")

# Returns a paginated list of pages which are relevant to the authenticated user.
response = client.consumer().page_get_all(1, 1, "search")

# Start the checkout process for a specific plan.
response = client.consumer().payment_checkout("provider", ConsumerPaymentcheckoutrequest())

# Generates a payment portal link for the authenticated user.
response = client.consumer().payment_portal("provider", ConsumerPaymentportalrequest())

# Returns a specific plan for the authenticated user.
response = client.consumer().plan_get("plan_id")

# Returns a paginated list of plans which are relevant to the authenticated user.
response = client.consumer().plan_get_all(1, 1, "search")

# Returns a paginated list of scopes which are assigned to the authenticated user.
response = client.consumer().scope_get_all(1, 1, "search")

# Returns all scopes by category.
response = client.consumer().scope_get_categories()

# Creates a new token for the authenticated user.
response = client.consumer().token_create(ConsumerTokencreate())

# Deletes an existing token for the authenticated user.
response = client.consumer().token_delete("token_id")

# Returns a specific token for the authenticated user.
response = client.consumer().token_get("token_id")

# Returns a paginated list of tokens which are assigned to the authenticated user.
response = client.consumer().token_get_all(1, 1, "search")

# Updates an existing token for the authenticated user.
response = client.consumer().token_update("token_id", ConsumerTokenupdate())

# Returns a specific transaction for the authenticated user.
response = client.consumer().transaction_get("transaction_id")

# Returns a paginated list of transactions which are assigned to the authenticated user.
response = client.consumer().transaction_get_all(1, 1, "search")

# Creates a new webhook for the authenticated user.
response = client.consumer().webhook_create(ConsumerWebhookcreate())

# Deletes an existing webhook for the authenticated user.
response = client.consumer().webhook_delete("webhook_id")

# Returns a specific webhook for the authenticated user.
response = client.consumer().webhook_get("webhook_id")

# Returns a paginated list of webhooks which are assigned to the authenticated user.
response = client.consumer().webhook_get_all(1, 1, "search")

# Updates an existing webhook for the authenticated user.
response = client.consumer().webhook_update("webhook_id", ConsumerWebhookupdate())

# Connection OAuth2 callback to authorize a connection.
response = client.system().connection_callback("name")

# Returns meta information and links about the current installed Fusio version.
response = client.system().meta_get_about()

# Debug endpoint which returns the provided data.
response = client.system().meta_get_debug(Passthru())

# Health check endpoint which returns information about the health status of the system.
response = client.system().meta_get_health()

# Returns all available routes.
response = client.system().meta_get_routes()

# Returns details of a specific schema.
response = client.system().meta_get_schema("name")

# Payment webhook endpoint after successful purchase of a plan.
response = client.system().payment_webhook("provider")
```
