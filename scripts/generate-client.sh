#!/bin/bash
set -e
script_path="$(dirname "$(readlink -f "$0")")"
cd "${script_path}"

if [[ ! -e openapi.json ]]; then
    #curl -s https://api.binarylane.com.au/reference/openapi.json -o openapi.json
    echo "Download or place a link to openapi.json in ${script_path}"
    exit 1
fi

mkdir -p ../src/blcli/client

openapi-python-client update --path openapi.json --config client.yml # --custom-template-path ../client-templates

# As of v0.12.0 the generated models avoid importing referenced types, but we currently need this to happen
# for get_type_hints() in Printer. For example,  models.servers_response defines ServersResponse class with
# an attribute of type List["Server"].  The import of models.server.Server is conditional on 'if TYPE_CHECKING:'
# so during our runtime, the type of "Server" is not known without this change below:
find ../src/blcli/client/models -type f -exec sed -i 's/if TYPE_CHECKING:/if True:/' {} +
