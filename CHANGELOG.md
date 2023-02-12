## 0.11.3

### Features

- use OpenAPI x-cli-format as default value for --format option (#4)
- set API URL and TLS verification via environment variables (#1)
- show command-specific "API Documentation" URL in --help epilog
- python 3.7 support
- use OpenAPI "x-cli-command" for command names
- Include command description in --help
- parsing support for structured request objects
- make "configure" command echo keyboard input during token submission
- display progress of commands returning ActionLink
- display progress of commands returning ActionResponse and wait until completion
- new command 'configure' to requestsAPI token, verify it works, save config
- convert enum definition markdown table to console
- display warning on missing help
- add --blcli-check for check of parameter mapping
- display warning on unsupported parameter type
- list requred parameters before optional in --help
- support 3-word command names like "domain record list"
- support additional output formats - plain, tsv, json
- add --curl option to display API request as curl command line
- add version command
- list commands accept --format ,display list of fields in --help
- display a reasonable subset of available response fields
- auto-merge responses from paged list commands
- add --help to subcommands
- add support for query parameters
- generic response printing via terminaltables package
- add support for json_body of type List[str]
- add support for with json_body str and/or bool properties
- add support for path parameters
- generic execution of parameter-less API commands

### Fixes

- create $HOME/.config if it does not exist
- input validation for ListRunner --format option
- display correct metavar for COMMAND in error output
- regression in "--curl" + test case to prevent future breakage
- disable UPX on windows executable
- improve output formatting when stdout is not a tty
- --format output did respect order of requested fields
- display error on windows if APPDATA is not set
- add datetime to cli_argument() supported types
- make package_runner Runner.CHECK work the same as interactive invocations
- field help reported as required arguments on error
- do not show warning for missing help on hidden arguments
- argument parsing for schema-less list parameter
- template changes required for compat with openapi-python-client v0.12
- display List[str] responses correctly, e.g. for  "domain nameservers list"
- version command broken in pyinstaller .exe
- add imports required for model properties of json_body
- show correct "prog" value in subcommand usage: output
