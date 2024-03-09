
# Fusio Python SDK

This is the official Fusio Java CSharp, it helps to talk to the Fusio REST API.
Fusio is an open source API management system, more information at:
https://www.fusio-project.org

## Usage

The following example shows how you can get all registered routes at the backend.
A working example is also available at: https://github.com/apioo/fusio-sample-csharp-cli

```csharp
package org.fusioproject.sample;

import app.sdkgen.client.Credentials.OAuth2;
import app.sdkgen.client.CredentialsInterface;
import app.sdkgen.client.Exception.ClientException;
import app.sdkgen.client.TokenStore.MemoryTokenStore;
import app.sdkgen.client.TokenStoreInterface;
import org.fusioproject.sdk.BackendOperationCollection;
import org.fusioproject.sdk.Client;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) throws ClientException {
        List<String> scopes = new ArrayList<>();
        scopes.add("backend");
        TokenStoreInterface tokenStore = new MemoryTokenStore();

        CredentialsInterface credentials = new OAuth2("test", "FRsNh1zKCXlB", "https://demo.fusio-project.org/authorization/token", "", tokenStore, scopes);
        Client client = new Client("https://demo.fusio-project.org/", credentials);

        BackendOperationCollection operations = client.backend().operation().getAll(0, 16, "");

        System.out.println("Operations:");
        for (int i = 0; i < operations.getEntry().size(); i++) {
            System.out.println("* " + operations.getEntry().get(i).getHttpMethod() + " " + operations.getEntry().get(i).getHttpPath());
        }
    }

}

```
