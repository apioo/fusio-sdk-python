
# Fusio Python SDK

This is the official Fusio Python SDK, it helps to talk to the Fusio REST API.
Fusio is an open source API management system, more information at:
https://www.fusio-project.org

## Usage

The following example shows how you can get all registered routes at the backend.
A working example is also available at: https://github.com/apioo/fusio-sample-python-cli

```python
from sdk.client import Client
from sdkgen import OAuth2, MemoryTokenStore

tokenStore = MemoryTokenStore()
scopes = ["backend"]

credentials = OAuth2(
    "test",
    "FRsNh1zKCXlB",
    "https://demo.fusio-project.org/authorization/token",
    "",
    tokenStore,
    scopes
)

client = Client("https://demo.fusio-project.org", credentials)

print("Operations:")
collection = client.backend().operation().get_all(0, 16, "")

for operation in collection.entry:
    print(" * " + operation.http_method + " " + operation.http_path)

```
