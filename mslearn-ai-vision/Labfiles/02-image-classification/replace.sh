#!/bin/bash

# Usage: ./replace_storage_account.sh path/to/json_file storage_account

# Check if the correct number of arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 path/to/json_file storage_account"
    exit 1
fi

# Assign arguments to variables
JSON_FILE=$1
STORAGE_ACCOUNT=$2

# Check if the file exists
if [ ! -f "$JSON_FILE" ]; then
    echo "File not found: $JSON_FILE"
    exit 1
fi

# Replace the placeholder with the storage account value and write back to the file
sed -i '' "s/ai102blobstorage/$STORAGE_ACCOUNT/g" "$JSON_FILE"

echo "Placeholder replaced with storage account: $STORAGE_ACCOUNT"


# chmod +x replace.sh
