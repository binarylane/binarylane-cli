# `bl`: BinaryLane command-line interface

```
$ bl --help
usage: bl [OPTIONS] COMMAND

bl is a command-line interface for the BinaryLane API

Options:
  --help                Display available commands and descriptions

Available Commands:
    account             Access account commands
    action              Access action commands
    configure           Configure access to BinaryLane API
    domain              Access domain commands
    image               Access image commands
    load-balancer       Access load-balancer commands
    region              Access region commands
    server              Access server commands
    size                Access size commands
    software            Access software commands
    ssh-key             Access ssh-key commands
    version             Show the current version
    vpc                 Access vpc commands
```

## Installation

`bl` requires Python 3.7 or later and has been tested on a variety of Linux
distributions, Windows and Mac OSX. To install:

```
pip install binarylane-cli
```

### Portable install (without Python)

The [releases page](https://github.com/binarylane/binarylane-cli/releases) has
a standalone `bl.exe` for use on Windows.


## Getting Started

The BinaryLane CLI program is invoked by running `bl` (or `bl.exe` on Windows).
To use `bl` you must configure the program with a BinaryLane customer access
token.

 1. To start the configuration process, run:
```
bl configure
```

 2. A prompt will be shown requesting access token. Go to [Developer API](https://home.binarylane.com.au/api-info) section of BinaryLane website and select **+ Create Token**, enter a name such as *CLI* and **Create**. 

 3. Copy the displayed token and paste at the `bl` *Enter your API access token:*
prompt.

 4. To confirm token is working correctly, use `bl` to display BinaryLane account details:
```
bl account get
``` 

## Usage

`bl` provides commands to access all functionality provided by the [BinaryLane
API](https://api.binarylane.com.au/reference/), organised into a *command
tree*. The general form for invoking an command is `bl NOUN [NOUN] VERB`.
For example:

 - `bl server list`: Displays list of servers
 - `bl domain record create`: Create a DNS record

The available commands at each level of the tree are displayed by running `bl`
with no arguments:

```
$ bl

usage: bl [OPTIONS] COMMAND

bl is a command-line interface for the binaryLane API

Options:
  --help                Display available commands and descriptions

Available Commands:
    account             Access account commands
    action              Access action commands
    configure           Configure access to binaryLane API
    domain              Access domain commands
    image               Access image commands
    load-balancer       Access load-balancer commands
    region              Access region commands
    server              Access server commands
    size                Access size commands
    software            Access software commands
    ssh-key             Access ssh-key commands
    version             Show the current version
    vpc                 Access vpc commands
```

To see the available commands within the tree:

```
bl NOUN [NOUN]
```

For example:

```
$ bl domain
usage: bl domain [OPTIONS] COMMAND

Access domain commands

Options:
  --help                Display available commands and descriptions

Available Commands:
    create              Create a new domain
    delete              Delete an existing domain
    get                 Fetch an existing domain
    list                List all domains
    nameservers         Access domain nameservers commands
    record              Access domain record commands
```

To see the required arguments and optional parameters for a command:

```
bl NOUN [NOUN] VERB --help
```

For example:

```
$ bl domain create --help
usage: bl domain create [OPTIONS] --name NAME [PARAMETERS]

Create a New Domain

Options:
  --help                Display command options and descriptions
  --curl                Display API request as a 'curl' command-line
  --no-header           Display columns without field labels
  --output OUTPUT       Desired output format [plain, table, tsv, json] (Default: "table")

Arguments:
  --name NAME           The domain name to add to the DNS management system.

Parameters:
  --ip-address IP_ADDRESS
                        An optional IPv4 address that will be used to create an A record for the root domain.
```

### Walkthrough: Creating a server

Server creation is provided by the `bl server create` command. Use `--help` to
view all arguments and parameters:

```
$ bl server list --help
usage: bl server create [OPTIONS] --size SIZE --image IMAGE --region REGION [PARAMETERS]

Create a new server.

Options:
  --help                Display command options and descriptions
  --curl                Display API request as a 'curl' command-line
  --no-header           Display columns without field labels
  --output OUTPUT       Desired output format [plain, table, tsv, json] (Default: "table")
  --async               Do not wait for requested action to complete
  --quiet               Do not show progress while waiting for requested action to complete

Arguments:
  --size SIZE           The slug of the selected size.
  --image IMAGE         The slug or id of the selected operating system.
  --region REGION       The slug of the selected region.

Parameters:
  --name NAME           The hostname of your server, such as vps01.yourcompany.com. If not
                        provided, the server will be created with a random name.
  --backups, --no-backups
                        If true this will enable two daily backups for the server.
                        Options.daily_backups will override this value if provided. Setting
                        this to false has no effect.
  --ipv6, --no-ipv6     If true this will enable IPv6 for this server.
  --ssh-keys [SSH_KEYS [SSH_KEYS ...]]
                        This may be either the SSH keys Ids or fingerprints. If this is null
                        or not provided any SSH keys that have been marked as default will be
                        deployed (if the operating system supports SSH keys). Submit an empty
                        array to disable deployment of default keys.
  --password PASSWORD   If this is provided the default remote user account's password will be
                        set to this value. If this is null a random password will be generated
                        and emailed to the account email address.
  <additional parameters omitted for brevity>
```

In the help displayed by `bl`, **Arguments** are required and **Parameters**
are optional. For the `bl server list` command `--size SIZE`, `--image IMAGE`,
and `--region REGION` are required. A list of available choices for each can be
displayed by running:

```
bl size list
bl image list
bl region list
```

For example, to create a minimum-sized Ubuntu 22.04 LTS server in Sydney using
SSH public key authentication:

```
$ bl server create --size std-min --image ubuntu-22.04-lts --region syd
completed.
┌───────────────────────────┬─────────────────────────────────────────────────────────────────────────────────────┐
│ name                      │ value                                                                               │
├───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────┤
│ id                        │ 210658                                                                              │
│ name                      │ giant-rudolf.bnr.la                                                                 │
│ memory                    │ 1024                                                                                │
│ vcpus                     │ 1                                                                                   │
│ disk                      │ 20                                                                                  │
│ created_at                │ 2023-01-20T02:02:32+00:00                                                           │
│ status                    │ new                                                                                 │
│ region                    │ Sydney                                                                              │
│ image                     │ 20.04 LTS                                                                           │
│ size                      │ std-min                                                                             │
│ size_slug                 │ std-min                                                                             │
│ networks                  │ v4: [{'ip_address': '175.45.180.1',  'type': 'public', 'netmask': '255.255.255.0... │
  <additional rows omitted for brevity>
└───────────────────────────┴─────────────────────────────────────────────────────────────────────────────────────┘
```

### Server passwords

The use of SSH public key authentication is strongly recommended where
possible. When public key authentication is not suitable or the image being
deployed does not support SSH public key authentication (e.g. Windows Server),
commands such as `bl server create` and `bl server action password-reset` have
an optional `--password PASSWORD` parameter that specifies the password to use.

For example, to create a server per the previous example with password
authentication:

```
$ bl server create --size std-min --image ubuntu-22.04-lts --region syd --password 'qq7s6GYZgbiVG3'
```

Upon completion, the root password for the server in this example would be `qq7s6GYZgbiVG3`.

:warning: **Internet-connected servers with password-based authentication enabled
must have a strong, randomly generated password.** Brute-force login attempts
are pervasive on the public internet: if a server password is not randomly
generated, unauthorised access is likely to occur.

### Server actions

`bl` can be used to perform any action that the BinaryLane website can perform,
including:

 - Take and restore backups
 - Change plan, operating system, or reinstall
 - Restart and power cycle
 - and many more...

A list of available commands is displayed by running `bl server action`:

```
$ bl server action

Available Commands:
    add-disk            Create an additional disk for a server
    attach-backup       Attach a backup to a server
    change-advanced-features
                        Change the advanced features of a server
    change-advanced-firewall-rules
                        Change the advanced firewall rules for a server
    change-backup-schedule
                        Change the backup schedule of a server
    change-ipv6         Enable or disable IPv6 for a server
    change-ipv6-reverse-nameservers
                        Update the IPv6 reverse name servers for a server
    change-kernel       Change the kernel of a server
  <additional actions omitted for brevity>
    ping                Attempt to ping a server
    power-cycle         Power a server off and then on
    power-off           Power a server off
    power-on            Power a server on
    reboot              Request a server perform a reboot
    rebuild             Rebuild an existing server
    rename              Rename a server
    resize              Update the size and related options for a server
    resize-disk         Alter the size of an existing disk for a server
    restore             Restore a backup to a server
    shutdown            Request a server perform a shutdown
    take-backup         Take a backup of a server
    uncancel            Revert the cancellation of a server
    uptime              Check the uptime of a server
```

Each server action has a mandatory `SERVER_ID` argument  which can be obtained
from `bl server list`.

Many actions have additional *action-specific* arguments and parameters. Run
`bl server action COMMAND --help` to see what a particular action supports.

#### Example: password reset

 1. Use `--help` to see the available arguments and parameters:


```
$ bl server action password-reset --help
usage: bl server action password-reset [OPTIONS] SERVER_ID [PARAMETERS]

Reset the Password of a Server

<options omitted for brevity>

Arguments:
  SERVER_ID            The ID of the server on which the action should be performed.

Parameters:
  --username USERNAME  The username of the user to change the password.
  --password PASSWORD  If this is provided the specified or default remote user's account
                       password will be set to this value.
```

 2. Use `bl server list` to obtain the numeric server ID. In this example, the
server requiring a password reset is ID 123456.

 3. Provide the server ID and desired password to the `password-reset` command:

```
bl server action password-reset 123456 --password 'qq7s6GYZgbiVG3'
```

### Asynchronous actions

`bl` commands that perform an action - `bl create server`, `bl server
action restore-backup`, and many others - default to *synchronous* handling
where `bl` will display progress information to the console and not exit until
the command finishes.

In some scenarios such as when creating multiple servers, it may be desirable
run the command with *asynchronous* handling where `bl` will exit as
soon as the BinaryLane API accepts the requested command. To do so, include the
`--async` option in the command invocation. For example:

```
$ bl server create --size std-min --image ubuntu-22.04-lts --region syd --async
```

### Configuration file

`bl configure` creates a configuration file containing the API token, and reads
that configuration file on subsequent invocations. The configuration file is
stored at:

 * `$XDG_CONFIG_HOME/binarylane/config.ini`

Typically the environment variable `$XDG_CONFIG_HOME` is not set, in which case
the configuration file stored at:

 - **Linux/Mac/etc**: `$HOME/.config` - typical file location is
   `/home/username/.config/binarylane/config.ini`
 - **Windows**: `$APPDATA` - typical file location is
   `C:\Users\UserName\AppData\Roaming\binarylane\config.ini`


### Environment variables

For environments where the use of `bl configure` and a permanent configuration
file are not suitable, environment variables may be utilised instead.

The environment variable `BL_API_TOKEN` may be used to provide the API token
required to perform `bl` commands.

## Versioning

`bl` uses [semantic versioning](https://semver.org/spec/v2.0.0.html) to version
[releases](https://github.com/binarylane/binarylane-cli/releases).

Semantic versions are in the form of `MAJOR.MINOR.PATCH`. The value of `MAJOR`
is currently **0**, which indicates that each new release of the `bl` program may
contain changes to its interface that are not backwards-compatible with
previous releases such as:

 - Command names may change, or moved within the command tree
 - Parameter names may change, or be removed entirely
 - Available field names may change, or be removed entirely
 - Default set of displayed fields displayed in output may change

Such changes in a new release are not likely to impact interactive use of `bl`,
but may cause problems for customers who integrate `bl` into non-interactive
environments such as automation.

In non-interactive environments, customers should review the release
Changelog prior to deploying an updated `0.x.y` release, and  ensure that any
required adjustments to the non-interactive environment are made prior to
upgrading the `bl` program itself.
