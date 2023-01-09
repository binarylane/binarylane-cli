#!/bin/bash
set -e
script_path="$(dirname "$(readlink -f "$0")")"
cd "${script_path}"

if [[ ! -e openapi.json ]]; then
    #curl -s https://api.binarylane.com.au/reference/openapi.json -o openapi.json
    echo "Download or place a link to openapi.json in ${script_path}"
    exit 1
fi

openapi-python-client update --path openapi.json --config client.yml
rm -f ../lib/binarylane/__init__.py
