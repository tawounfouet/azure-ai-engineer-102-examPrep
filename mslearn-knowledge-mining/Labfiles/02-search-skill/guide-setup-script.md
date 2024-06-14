
# Convert Windows batch script to a Bash script for macOS :


```sh
# setup.cmd
@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

rem Set values for your subscription and resource group
set subscription_id=YOUR_SUBSCRIPTION_ID
set resource_group=YOUR_RESOURCE_GROUP
set location=YOUR_LOCATION_NAME

rem Get random numbers to create unique resource names
set unique_id=!random!!random!

echo Creating storage...
call az storage account create --name ai102str!unique_id! --subscription !subscription_id! --resource-group !resource_group! --location !location! --sku Standard_LRS --encryption-services blob --default-action Allow --allow-blob-public-access true --only-show-errors --output none

echo Uploading files...
rem Hack to get storage key
for /f "tokens=*" %%a in ( 
'az storage account keys list --subscription !subscription_id! --resource-group !resource_group! --account-name ai102str!unique_id! --query "[?keyName=='key1'].{keyName:keyName, permissions:permissions, value:value}"' 
) do ( 
set key_json=!key_json!%%a 
) 
set key_string=!key_json:[ { "keyName": "key1", "permissions": "Full", "value": "=!
set AZURE_STORAGE_KEY=!key_string:" } ]=!
call az storage container create --account-name ai102str!unique_id! --name margies --public-access blob --auth-mode key --account-key %AZURE_STORAGE_KEY% --output none
call az storage blob upload-batch -d margies -s data --account-name ai102str!unique_id! --auth-mode key --account-key %AZURE_STORAGE_KEY%  --output none

echo Creating search service...
echo (If this gets stuck at '- Running ..' for more than a couple minutes, press CTRL+C then select N)
call az search service create --name ai102srch!unique_id! --subscription !subscription_id! --resource-group !resource_group! --location !location! --sku basic --output none

echo -------------------------------------
echo Storage account: ai102str!unique_id!
call az storage account show-connection-string --subscription !subscription_id! --resource-group !resource_group! --name ai102str!unique_id!
echo ----
echo Search Service: ai102srch
echo  Url: https://ai102srch!unique_id!.search.windows.net
echo  Admin Keys:
call az search admin-key show --subscription !subscription_id! --resource-group !resource_group! --service-name ai102srch!unique_id!
echo  Query Keys:
call az search query-key list --subscription !subscription_id! --resource-group !resource_group! --service-name ai102srch!unique_id!
```

To convert the given Windows batch script to a Bash script for macOS, you need to replace Windows-specific commands and syntax with their Unix counterparts. Here is the equivalent `Bash script`:



```sh
#!/bin/bash

# Set values for your subscription and resource group
subscription_id="YOUR_SUBSCRIPTION_ID"
resource_group="YOUR_RESOURCE_GROUP"
location="YOUR_LOCATION_NAME"

# Get random numbers to create unique resource names
unique_id=$RANDOM$RANDOM

echo "Creating storage..."
az storage account create --name ai102str$unique_id --subscription $subscription_id --resource-group $resource_group --location $location --sku Standard_LRS --encryption-services blob --default-action Allow --allow-blob-public-access true --only-show-errors --output none

echo "Uploading files..."
# Hack to get storage key
key_json=$(az storage account keys list --subscription $subscription_id --resource-group $resource_group --account-name ai102str$unique_id --query "[?keyName=='key1'].{keyName:keyName, permissions:permissions, value:value}" -o json)
AZURE_STORAGE_KEY=$(echo $key_json | jq -r '.[0].value')

az storage container create --account-name ai102str$unique_id --name margies --public-access blob --auth-mode key --account-key $AZURE_STORAGE_KEY --output none
az storage blob upload-batch -d margies -s data --account-name ai102str$unique_id --auth-mode key --account-key $AZURE_STORAGE_KEY --output none

echo "Creating search service..."
echo "(If this gets stuck at '- Running ..' for more than a couple minutes, press CTRL+C then select N)"
az search service create --name ai102srch$unique_id --subscription $subscription_id --resource-group $resource_group --location $location --sku basic --output none

echo "-------------------------------------"
echo "Storage account: ai102str$unique_id"
az storage account show-connection-string --subscription $subscription_id --resource-group $resource_group --name ai102str$unique_id
echo "----"
echo "Search Service: ai102srch"
echo " Url: https://ai102srch$unique_id.search.windows.net"
echo " Admin Keys:"
az search admin-key show --subscription $subscription_id --resource-group $resource_group --service-name ai102srch$unique_id
echo " Query Keys:"
az search query-key list --subscription $subscription_id --resource-group $resource_group --service-name ai102srch$unique_id

```



```sh
# Dependencies : jq for JSON parsing
brew install jq


# Executation : Make the script executable:
chmod +x setup_script.sh
```



## Explanation:

1. Variable Assignment:
- Use `=` for assignment without spaces around it.
- Replace `set` with direct variable assignment.


2. Unique ID Generation:
- Use `$RANDOM` for generating random numbers in Unix.

3. Multi-line Command Substitution:
- Use `$()` for command substitution in Unix.
- Use `jq` for parsing JSON, which can be installed via brew install jq.

4. Loop and Conditional Constructs:
- No direct translation needed as all Azure CLI commands are executed directly.

5. Azure CLI Commands:
- Replace Windows-specific syntax with Unix-compatible syntax.

6. File Upload and Container Creation:
- Use `az storage container create` and `az storage blob upload-batch` commands with the correct arguments.

