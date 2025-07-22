# CHANGELOG

## v0.20.0 (2025-07-22)

### Features

- add x-cli-lookup attribute to load-balancer and vpc (#69)
- support x-cli-lookup attribute on request body properties (#68)

## v0.19.0 (2025-04-04)

### Bug Fixes

- output action properties at completion of command runner (#62)
- resolve exception when action ID is passed to printer formatter

### Features

- include action_id in formatted output of response containing ActionLink

## v0.18.0 (2025-02-28)

## v0.17.0 (2025-02-12)

- update to API 0.28.0 (#47)

## v0.16.0 (2023-04-21)

### Features

- allow use of server.name as server_id argument  (#11)

## v0.15.3 (2023-03-29)

### Fixes

- incorrect parsing of object list when a list primitive immediately preceeds keyword (#38)
- provide empty list instead of Unset for OpenAPI arrays marked "required" (#35)

## v0.15.2 (2023-03-22)

### Fixes

- partially revert #28 as it breaks --output json for lists (#32)

## v0.15.1 (2023-03-21)

### Fixes

- error handling for HTTP 200 (#31)

## v0.15.0 (2023-03-21)

### Features

- handle API response error in same manner as CLI parser error (#10)
- add globbing support to ListRunner --format option (#29)

## v0.14.0 (2023-03-15)

### Bug Fixes

- make importlib-metadata an explicit dependency for py3.7 (#24)
- add missing description for "server console" command (#18)

### Features

- add --context to allow selecting from multiple API tokens (#15)

## v0.13.0 (2023-03-02)

### Features

- update to API v0.23.0 (#16)

## v0.12.0 (2023-02-18)

### Features

- improved formatting of image and networks properties (#5)
- use OpenAPI x-cli-format as default value for --format option (#4)
- set API URL and TLS verification via environment variables (#1)

## [0.11.1](https://github.com/binarylane/binarylane-cli/compare/v0.11.0...v0.11.1) (2023-01-25)

### Bug Fixes

- create $HOME/.config if it does not exist 


## [0.11.0](https://github.com/binarylane/binarylane-cli/compare/v0.10.1...v0.11.0) (2023-01-25)

### Features

- Include command description in --help 
- python 3.7 support 
- show command-specific "API Documentation" URL in --help epilog 
- use OpenAPI "x-cli-command" for command names 

### Bug Fixes

- display correct metavar for COMMAND in error output 
- input validation for ListRunner --format option 


### [0.10.1](https://github.com/binarylane/binarylane-cli/compare/v0.10.0...v0.10.1) (2023-01-21)

### Bug Fixes

- regression in "--curl" + test case to prevent future breakage 


## [0.10.0](https://github.com/binarylane/binarylane-cli/compare/v0.9.1...v0.10.0) (2023-01-20)

### Performance Improvements

- delay importing CommandRunner 
- delay importing httpx in HttpxWrapper 


### [0.9.1](https://github.com/binarylane/binarylane-cli/compare/v0.9.0...v0.9.1) (2023-01-20)

### Bug Fixes

- disable UPX on windows executable 


## [0.9.0](https://github.com/binarylane/binarylane-cli/compare/v0.8.0...v0.9.0) (2023-01-20)

### Features

- make "configure" command echo keyboard input during token submission 
- parsing support for structured request objects 

### Bug Fixes

- --format output did respect order of requested fields 
- improve output formatting when stdout is not a tty 


## [0.8.0](https://github.com/binarylane/binarylane-cli/compare/v0.7.0...v0.8.0) (2023-01-09)

### Features

- display progress of commands returning ActionLink 
- display progress of commands returning ActionResponse and wait until completion 

### Bug Fixes

- display error on windows if APPDATA is not set 


## [0.7.0](https://github.com/binarylane/binarylane-cli/compare/v0.6.0...v0.7.0) (2023-01-07)

### Features

- convert enum definition markdown table to console 
- display warning on missing help 
- new command 'configure' to requestsAPI token, verify it works, save config 

### Bug Fixes

- add datetime to cli_argument() supported types 
- do not show warning for missing help on hidden arguments 
- field help reported as required arguments on error 
- make package_runner Runner.CHECK work the same as interactive invocations 


## [0.6.0](https://github.com/binarylane/binarylane-cli/compare/v0.5.0...v0.6.0) (2023-01-04)

### Features

- add --blcli-check for check of parameter mapping 
- display warning on unsupported parameter type 
- list requred parameters before optional in --help 

### Bug Fixes

- argument parsing for schema-less list parameter 
- display List[str] responses correctly, e.g. for  "domain nameservers list" 
- template changes required for compat with openapi-python-client v0.12 


## [0.5.0](https://github.com/binarylane/binarylane-cli/compare/v0.4.0...v0.5.0) (2022-12-31)

### Features

- support 3-word command names like "domain record list" 


## [0.4.0](https://github.com/binarylane/binarylane-cli/compare/v0.3.0...v0.4.0) (2022-12-31)

### Features

- support additional output formats - plain, tsv, json 

### Bug Fixes

- version command broken in pyinstaller .exe 


## [0.3.0](https://github.com/binarylane/binarylane-cli/compare/v0.2.0...v0.3.0) (2022-12-30)

### Features

- add --curl option to display API request as curl command line 


## [0.2.0](https://github.com/binarylane/binarylane-cli/compare/v0.1.0...v0.2.0) (2022-12-29)

### Features

- add --help to subcommands 
- add support for query parameters 
- add version command 
- auto-merge responses from paged list commands 
- display a reasonable subset of available response fields 
- list commands accept --format ,display list of fields in --help 

### Bug Fixes

- add imports required for model properties of json_body 
- show correct "prog" value in subcommand usage: output 


## [0.1.0](https://github.com/binarylane/binarylane-cli/compare/2005c251e268fabe333f5c314b26681e7fd5fcf7...v0.1.0) (2022-09-17)

### Features

- add support for json_body of type List[str] 
- add support for path parameters 
- add support for with json_body str and/or bool properties 
- generic execution of parameter-less API commands 
- generic response printing via terminaltables package 
