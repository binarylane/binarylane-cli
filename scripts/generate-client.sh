#!/bin/bash
script_path="$(dirname "$(readlink -f "$0")")"
cd "${script_path}"

if [[ ! -e openapi.json ]]; then
    #curl -s https://api.binarylane.com.au/reference/openapi.json -o openapi.json
    echo "Download or place a link to openapi.json in ${script_path}"
    exit 1
fi

if openapi-python-client update --path openapi.json --config client.yml
then
    cd ..
    rm -f lib/binarylane/__init__.py
    find lib -name '*.py' -exec poetry run absolufy-imports --application-directories lib {} + || true  # retu
    poetry run isort --add-import 'from __future__ import annotations' lib | grep -v 'Fixing'
fi
