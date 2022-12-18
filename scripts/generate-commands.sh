#!/bin/bash
set -e
script_path="$(dirname "$(readlink -f "$0")")"
cd "${script_path}"

if [[ ! -e openapi.json ]]; then
    #curl -s https://api.binarylane.com.au/reference/openapi.json -o openapi.json
    echo "Download or place a link to openapi.json in ${script_path}"
    exit 1
fi

rm -rf commands ../src/blcli/commands
mkdir commands
openapi-python-client update --path openapi.json --config commands.yml --custom-template-path ../templates
mv commands/api ../src/blcli/commands
rm -rf commands
