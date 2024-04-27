# hcp-vault-secrets

Python package to implement the Hashicorp Cloud Platform - Vault Secrets API


## Description

Python package to implement the [Hashicorp Cloud Platform - Vault Secrets API](https://developer.hashicorp.com/hcp/docs/vault-secrets). In order for the code to function properly, we will need to set a few environment variables to provide authentication against the HCP API such that, we can retrieve the secret values containing sensitive information (i.e passwords, api_tokens, etc..) from various vault secret applications located within a given project. Please refer to the `Package Requirements` section for more information on the (4) required environment variables

You can find the `organizationID` and `projectID` in their respective settings tab in HCP. However, in order to get the clientID and clientSecret, you will need to navigate to the `Projects` -> `<Project Name>` -> `Access Control (IAM)` -> `Service Principals` tab within your organization. Create a service principal with the `Contributer Role` and generate keys. This will populate a `clientID` and `clientSecret` that the code will use to authenticate to the HCP API 

## Installation

    pip install hcp-vault-secrets

## Package Requirements

### Packages

    pip install requests

### Environment Variables

- `clientID`: This is the clientID that is associated with the service principal in HashiCorp Cloud Platform.

- `clientSecret`: This is the clientSecret that is associated with the service principal in HashiCorp Cloud Platform.

- `organizationID`: The HashiCorp Cloud Platform organization ID that owns the Vault Secrets application

- `projectID`: The HashiCorp Cloud Platform project ID where the Vault Secrets application is located

### Hashicorp Cloud Platform (HCP)

**HCP Topology**

- Organization -> Project(s) -> Service(s) [e.g Vault Secrets] -> Application -> Key/Value (secret)

## How to use

### Create Hashicorp Cloud Platform Instance

    # import hcp_vault_secrets package
    import hcp_vault_secrets.vaultsecrets as vaultsecrets

    # create hcp instance
    hcp = vaultsecrets.vaultsecrets()

### API ENDPOINTS Implemented

#### /apps/{app_name}/open/{secret_name}

**GET**

Path Parameters

| name | type | description | required |
| ---- | ---- | ----------- | -------- |
| appName | string | The name of the vault secrets application where the key is stored | True |
| secretName | string | The name of the secrets' key you want to retrieve | True |

![](https://github.com/JustinBatchelor/hcp-vault-secrets/blob/37ad8ca3c33e52dc256d3c187a05169665283192/docs/pics/hcp-topo.png?raw=true)


**EXAMPLES**

    import hcp_vault_secrets.vaultsecrets as vaultsecrets

    # create hcp instance
    hcp = vaultsecrets.vaultsecrets()

    # get the secret named "token" from the "assisted-installer" vault secrets application
    # return type is <str>
    token = hcp.getAppSecret(appName="assisted-installer", secretName="token")

    # get the secret named "pull_secret" from the "assisted-installer" vault secrets application
    # return type is <str>
    pull_secret = hcp.getAppSecret(appName="assisted-installer", secretName="pull_secret")

    # get the secret named "password" from the "proxmox" vault secrets application (in the same project)
    # return type is <str>
    prox = hcp.getAppSecret("proxmox", "password")

## References

- [Hashicorp Cloud Platform | Vault Secrets](https://developer.hashicorp.com/hcp/api-docs/vault-secrets)