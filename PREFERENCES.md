# BinaryLane CLI User Preferences Guide

This guide covers all aspects of customizing the BinaryLane CLI using preferences, including output formatting and server creation defaults.

## Table of Contents

- [Quick Start](#quick-start)
- [Managing Preferences](#managing-preferences)
- [Server Creation Defaults](#server-creation-defaults)
- [Output Formatting Preferences](#output-formatting-preferences)
- [Terminal Settings](#console-settings)
- [Configuration Priority](#configuration-priority)
- [Field Reference](#field-reference)
  - [Images](#images)
  - [Servers](#servers)
  - [Domains](#domains)
  - [VPCs](#vpcs)
  - [Load Balancers](#load-balancers)
  - [SSH Keys](#ssh-keys)
  - [Actions](#actions)
  - [And more...](#additional-resources)

---

## Quick Start

Preferences allow you to customize the CLI's behavior without repeating the same options every time.

### Without Preferences (Full Command)

```bash
# Create a server - must specify all required parameters
bl server create --size std-min --image ubuntu-24.04 --region syd

# Name is optional (auto-generated if omitted)
bl server create --name web-01 --size std-min --image ubuntu-24.04 --region syd

# Every server requires repeating these options
bl server create --name api-01 --size std-min --image ubuntu-24.04 --region syd
bl server create --size std-2vcpu --image ubuntu-24.04 --region syd  # Different size
```

### With Preferences (Simplified)

```bash
# Step 1: Set preferences once
bl preferences set default-region syd
bl preferences set default-size std-min
bl preferences set default-image ubuntu-24.04

# Step 2: Verify your configuration
bl preferences show server create
```

Output:
```
Server Creation Defaults:

Currently set:

  default-region   = syd
  default-size     = std-min
  default-image    = ubuntu-24.04

Available (not set):

  default-backups       - Enable backups by default (API default: false)
  default-ssh-keys      - Default SSH key IDs (comma-separated)
  default-user-data     - Default user data file path
  default-port-blocking - Disable port blocking (API default: true/enabled)
  default-password      - Default root/administrator password
  default-vpc           - Default VPC ID for server creation


All required server creation fields have default values set.

With your current defaults, this command:
  bl server create --name myserver

Expands to (what gets sent to the API):
  bl server create --name myserver --region syd --size std-min --image ubuntu-24.04

To set a preference: bl preferences set <key> <value>
To unset: bl preferences set <key> null
```

```bash
# Step 3: Now create servers with zero arguments
bl server create
# ↑ Uses: size=std-min, image=ubuntu-24.04, region=syd (all from preferences)

# Or specify a custom name if you want
bl server create --name web-01
# ↑ Uses: name=web-01 (specified), size=std-min, image=ubuntu-24.04, region=syd (from preferences)

# Create multiple servers quickly
bl server create
bl server create
bl server create --name db-worker --size std-2vcpu
# ↑ Last one overrides: size=std-2vcpu, uses preferences for other settings
```

### Customize Output Format

```bash
# Set your preferred columns for server lists
bl preferences set format-servers "id,name,status,region,created_at"

# Now lists use your format automatically
bl server list
# Shows only: id, name, status, region, created_at columns
```

---

## Managing Preferences

### Set a Preference

```bash
bl preferences set <key> <value>
```

Examples:
```bash
bl preferences set default-region syd
bl preferences set format-servers "id,name,status,region"
bl preferences set terminal-width 120
```

**Need help with a preference?** Omit the value to see contextual help:

```bash
# Show help for a specific preference
bl preferences set default-port-blocking

# Output:
# (not currently set)
# 
# Valid values: false (to disable port blocking)
# Default (if not set): true (port blocking enabled)
# Example: bl preferences set default-port-blocking false
# 
# To set: bl preferences set default-port-blocking <value>
# To unset: bl preferences set default-port-blocking null
```

This works for all preferences and will show:
- Current value (if set)
- Where to find valid values (e.g., `bl region list`)
- Examples
- How to unset

### View a Specific Preference

There are two ways to view preferences:

**`preferences get`** - Shows just the value (quick lookup):
```bash
bl preferences get default-region
# Output: default-region = syd
```

**`preferences show`** - Shows detailed information with help text:
```bash
bl preferences show default-region
# Output:
# default-region = syd
# 
# Description: Default region for server creation
# 
#   Available regions: bl region list
#   Example: bl preferences set default-region syd
# 
# To set: bl preferences set default-region <value>
# To unset: bl preferences set default-region null
```

**When to use which:**
- Use `get` when you just need the value
- Use `show` when you want help on how to set it or what values are valid

### List All Preferences

```bash
bl preferences get
```

This displays all currently set preferences (excludes sensitive values like `api-token`).

### View Preferences by Command Group

The `preferences show` command can also group related preferences together:

```bash
# Show all server creation defaults
bl preferences show server create

# Show Terminal Settings
bl preferences show terminal

# Show list formatting preferences
bl preferences show image list
bl preferences show server list
bl preferences show domain list
bl preferences show vpc list
bl preferences show load-balancer list
bl preferences show ssh-key list
bl preferences show action list
bl preferences show size list
bl preferences show region list
bl preferences show invoice list
bl preferences show software list
```

Example output with all required fields set:
```
Server Creation Defaults:

Currently set:

  default-region   = syd
  default-size     = std-min
  default-image    = ubuntu-24.04

Available (not set):

  default-backups       - Enable backups by default (API default: false)
  default-ssh-keys      - Default SSH key IDs (comma-separated)
  default-user-data     - Default user data file path
  default-port-blocking - Disable port blocking (API default: true/enabled)
  default-password      - Default root/administrator password
  default-vpc           - Default VPC ID for server creation


All required server creation fields have default values set.

With your current defaults, this command:
  bl server create --name myserver

Expands to (what gets sent to the API):
  bl server create --name myserver --region syd --size std-min --image ubuntu-24.04

To set a preference: bl preferences set <key> <value>
To unset: bl preferences set <key> null
```

**Note:** `region`, `size`, and `image` are required for server creation. All other preferences (like `default-backups`) are optional.

Example output with missing required fields:
```
Server Creation Defaults:

Currently set:

  default-region = syd
  default-image  = ubuntu-24.04

Available (not set):

  default-size          - Default size for server creation
  default-backups       - Enable backups by default (API default: false)
  default-ssh-keys      - Default SSH key IDs (comma-separated)
  default-user-data     - Default user data file path
  default-port-blocking - Disable port blocking (API default: true/enabled)
  default-password      - Default root/administrator password
  default-vpc           - Default VPC ID for server creation


Required for server creation (provide via command line or set as preference defaults):
  --size SIZE          (see: bl size list)

To set a preference: bl preferences set <key> <value>
To unset: bl preferences set <key> null
```

### Reset a Preference

Set any preference to `null` to reset it to the CLI's built-in default:

```bash
bl preferences set default-region null
bl preferences set format-images null
bl preferences set terminal-width null
```

---

## Server Creation Defaults

Set default values for server creation to speed up your workflow and ensure consistency:

### Available Server Defaults

| Preference Key | Description | Example Value |
|----------------|-------------|---------------|
| `default-region` | Default deployment region | `syd`, `bne`, `per` |
| `default-size` | Default server size | `std-min`, `std-1vcpu`, `std-2vcpu` |
| `default-image` | Default OS image | `ubuntu-24.04`, `debian-12` |
| `default-backups` | Enable backups by default (API default: false) | `true` |
| `default-ssh-keys` | Default SSH key fingerprints (comma-separated) | `aa:bb:cc:...` |
| `default-port-blocking` | Disable port blocking for email/SSH/RDP (API default: enabled) | `false` |
| `default-user-data` | Path to user-data file | `~/.config/bl/my-user-data.yaml` |
| `default-password` | Default password (not recommended) | Use SSH keys instead! |
| `default-vpc` | Default VPC ID | `12345` |

### Basic Example

**Before setting preferences:**
```bash
# Must specify all required fields every time
bl server create --name web-01 --size std-min --image ubuntu-24.04 --region syd
bl server create --name web-02 --size std-min --image ubuntu-24.04 --region syd
bl server create --name web-03 --size std-min --image ubuntu-24.04 --region syd
```

**After setting preferences:**
```bash
# Set your common defaults once
bl preferences set default-region syd
bl preferences set default-size std-min
bl preferences set default-image ubuntu-24.04

# Now create servers without specifying these every time
bl server create
# ↑ Automatically uses: size=std-min, image=ubuntu-24.04, region=syd

bl server create
# ↑ Another server with same config

# Or specify custom names when needed
bl server create --name web-01
# ↑ Custom name: web-01, uses preferences for everything else
```

**Override when needed:**
```bash
# Override specific values while keeping other preferences
bl server create --name db-server --size std-4vcpu
# ↑ Override: size=std-4vcpu
# ↑ Still uses preferences: image=ubuntu-24.04, region=syd

bl server create --name test-debian --image debian-12 --region per
# ↑ Override: image=debian-12, region=per
# ↑ Still uses preferences: size=std-min
```

### Advanced Example: User Data Files

The `default-user-data` preference allows you to specify a file path that will be automatically passed to all new servers. This is commonly used with cloud-init configuration files.

```bash
# Set a default user-data file
bl preferences set default-user-data ~/.config/bl/my-user-data.yaml

# Also set other common defaults
bl preferences set default-region syd
bl preferences set default-size std-min
bl preferences set default-image ubuntu-24.04

# Verify your settings
bl preferences show server create
# Output:
# Server Creation Defaults:
#   default-region    = syd
#   default-size      = std-min
#   default-image     = ubuntu-24.04
#   default-user-data = /home/user/.config/bl/my-user-data.yaml
#
# With your current defaults, this command:
#   bl server create --name myserver
#
# Expands to (what gets sent to the API):
#   bl server create --name myserver --region syd --size std-min --image ubuntu-24.04 --user-data ~/.config/bl/my-user-data.yaml

# Now create servers with zero arguments - user-data is automatically included
bl server create
# ↑ Uses: size=std-min, image=ubuntu-24.04, region=syd, user-data=my-user-data.yaml

# Or specify a custom name
bl server create --name web-01
# ↑ Custom name: web-01, uses all preferences including user-data

# Override user-data for a specific server
bl server create --user-data ~/custom-setup.yaml
# ↑ Uses: custom-setup.yaml (override), other preferences still apply
```

**Tip:** You can maintain different user-data files for different environments by using contexts:

```bash
# Development context with dev-specific user-data
bl -c dev preferences set default-user-data ~/.config/bl/user-data-dev.yaml
bl -c dev preferences set default-region syd
bl -c dev preferences set default-size std-min
bl -c dev preferences set default-image ubuntu-24.04

# Production context with prod-specific user-data
bl -c prod preferences set default-user-data ~/.config/bl/user-data-prod.yaml
bl -c prod preferences set default-region per
bl -c prod preferences set default-size std-2vcpu
bl -c prod preferences set default-image ubuntu-24.04

# Create servers in different contexts
bl -c dev server create --name app-dev-01   # Uses user-data-dev.yaml
bl -c prod server create --name app-prod-01  # Uses user-data-prod.yaml
```

---

## Output Formatting Preferences

Customize which fields are displayed in list commands. Each resource type has its own format preference.

### Available Format Preferences

| Preference Key | Command | Default Fields |
|----------------|---------|----------------|
| `format-images` | `bl image list` | `id,slug,distribution,name` |
| `format-servers` | `bl server list` | `id,name,image,vcpus,memory,disk,region,networks` |
| `format-domains` | `bl domain list` | `id,name,zone_file` |
| `format-vpcs` | `bl vpc list` | `id,name,ip_range` |
| `format-load-balancers` | `bl load-balancer list` | `id,name,ip,created_at` |
| `format-ssh-keys` | `bl ssh-key list` | `id,name,fingerprint` |
| `format-actions` | `bl action list` | `id,status,type,started_at` |
| `format-sizes` | `bl size list` | `slug,description,vcpus,memory` |
| `format-regions` | `bl region list` | `slug,name,available` |
| `format-invoices` | `bl account invoice list` | `id,amount,created_at,status` |
| `format-software` | `bl software list` | `name,status,version` |

### Setting Format Preferences

```bash
# Set default format for image lists
bl preferences set format-images "id,full_name,distribution,created_at,status"

# Set default format for server lists  
bl preferences set format-servers "id,name,status,region,created_at"

# Set default format for domains
bl preferences set format-domains "id,name,current_nameservers"
```

### Using Format Override

You can always override your preference for a single command:

```bash
# Override default format
bl image list --format "id,slug,name"

# Show all available fields
bl image list --format "*"

# Use wildcards for partial matching
bl image list --format "id,*name,distribution"
```

### Example Workflow

**Without format preferences:**
```bash
# Default shows many columns (can be overwhelming)
bl server list
# Shows: id, name, image, vcpus, memory, disk, region, networks (8 columns!)

# Must specify format every time for cleaner output
bl server list --format "id,name,status,region"
bl server list --format "id,name,status,region"  # Repetitive!
```

**With format preferences:**
```bash
# Set your preferred columns once
bl preferences set format-servers "id,name,status,region,created_at"

# Now lists automatically use your preferred format
bl server list
# Output:
# ID      NAME        STATUS  REGION  CREATED_AT
# 12345   web-01      active  syd     2024-01-15T10:30:00Z
# 12346   db-01       active  syd     2024-01-15T10:35:00Z

# Need more detail for one specific command? Override it
bl server list --format "id,name,vcpus,memory,disk,networks"
# ↑ One-time override, doesn't change your preference

# Reset to CLI's built-in default
bl preferences set format-servers null
```

---

## Terminal Settings

### Terminal Width

Control the terminal width for help text formatting:

```bash
# Set a specific width
bl preferences set terminal-width 120

# Use auto-detection (default)
bl preferences set terminal-width null
```

This affects how help text wraps in `--help` output.

---

## Configuration Priority

Preferences provide defaults that can always be overridden. The priority chain is:

1. **Command-line flags** (highest priority)
   - Example: `--region syd`
   
2. **Environment variables**
   - Example: `BL_API_TOKEN=your-token`
   - Format: `BL_<OPTION_NAME>` (uppercase, dashes become underscores)
   
3. **Preferences** (config file)
   - Example: `default-region = syd` in config.ini
   
4. **Built-in defaults** (lowest priority)
   - CLI's hardcoded defaults

### Example

**Setup:**
```bash
# Set preferences (all three required fields)
bl preferences set default-region syd
bl preferences set default-size std-min
bl preferences set default-image ubuntu-24.04
```

**Priority in action:**
```bash
# 1. Uses preferences (nothing overrides them)
bl server create
# ↑ Creates server with: region=syd, size=std-min, image=ubuntu-24.04 (all from preferences)

# 2. Command-line flag overrides preference
bl server create --region per
# ↑ Creates server with: region=per (CLI flag overrides preference)
# ↑ Still uses: size=std-min, image=ubuntu-24.04 (from preferences)
```

**Key Takeaway:** Command-line flags always win, so you can always override preferences when needed.

---

## Field Reference

This section provides a comprehensive reference for all available formatter fields. Each resource type includes:
- The config key for setting the preference
- The command that uses it
- Default fields
- All available fields with descriptions
- Human-readable formatting suggestions

### Images

**Config Key**: `format-images`  
**Command**: `bl image list`

**Default Fields:**
```
id,slug,distribution,name
```

**Available Fields:**

| Field | Description |
|-------|-------------|
| `id` | The ID of this image |
| `name` | If this is an operating system image, this is the name of the operating system version. If this is a backup image, this is the label of the backup if it exists, otherwise it is the UTC timestamp of the creation of the image |
| `slug` | If this is an operating system image this is a slug which may be used as an alternative to the ID as a reference |
| `distribution` | If this is an operating system image, this is the name of the distribution. If this is a backup image, this is the name of the distribution the server is using |
| `full_name` | If this is an operating system image, this is the name and version of the distribution. If this is a backup image, this is the server hostname and label of the backup if it exists, otherwise it is the server hostname and UTC timestamp of the creation of the image |
| `type` | Image type: `custom`, `snapshot`, or `backup` |
| `public` | A public image is available to all users. A private image is available only to the account that created the image |
| `regions` | The slugs of the regions where the image is available for use |
| `min_disk_size` | For a distribution image this is the minimum disk size in GB required to install the operating system. For a backup image this is the minimum total disk size in GB required to restore the backup |
| `size_gigabytes` | For a distribution image this is the disk size used in GB by the operating system on initial install. For a backup image this is the size of the compressed backup image in GB |
| `status` | Image status: `NEW`, `available`, `pending`, or `deleted` |
| `created_at` | If this is a backup image this is the date and time in ISO8601 format when the image was created |
| `description` | A description that may provide further details or warnings about the image |
| `error_message` | If the image creation failed this may provide further information |
| `min_memory_megabytes` | This is minimum memory in MB necessary to support this operating system (or the base operating system for a backup image) |
| `distribution_info` | This object may provide further information about the distribution |
| `distribution_surcharges` | If this is not null the use of this image may incur surcharges above the base cost of the server. All costs are in AU$ |
| `backup_info` | If this image is a backup, this object will provide further information |

**Suggested Formats:**
```bash
# Compact overview
bl preferences set format-images "id,slug,distribution,name"

# Detailed for backups
bl preferences set format-images "id,full_name,distribution,created_at,min_disk_size,status"

# With availability info
bl preferences set format-images "id,name,distribution,regions,status,size_gigabytes"
```

---

### Servers

**Config Key**: `format-servers`  
**Command**: `bl server list`

**Default Fields:**
```
id,name,image,vcpus,memory,disk,region,networks
```

**Available Fields:**

| Field | Description |
|-------|-------------|
| `id` | The ID of this server |
| `name` | The hostname of this server |
| `status` | Server status: `new`, `active`, `archive`, or `off` |
| `memory` | The memory in MB of this server |
| `vcpus` | The number of virtual CPUs of this server |
| `disk` | The total disk in GB of this server |
| `created_at` | The date and time in ISO8601 format of this server's initial creation |
| `region` | The region this server is allocated to |
| `image` | The base image used to create this server |
| `size` | The currently selected size for this server |
| `size_slug` | The slug of the currently selected size for this server |
| `networks` | A list of the networks of the server |
| `disks` | A list of the disks that are currently attached to the server |
| `backup_ids` | A list of the currently existing backup image IDs for this server (if any) |
| `features` | A list of the currently enabled features on this server |
| `backup_settings` | Detailed backup settings for the server |
| `failover_ips` | A list of any assigned failover IP addresses for this server |
| `host` | Summary information about the host of this server |
| `password_change_supported` | If this is true the password_reset server action can be called to change a user's password |
| `advanced_features` | The currently enabled advanced features, machine type and processor flags |
| `vpc_id` | The VPC ID that this server is allocated to. If this value is null the server is in the default (public) network for the region |
| `selected_size_options` | An object that details the selected options for the current size |
| `kernel` | The currently selected kernel for the server |
| `next_backup_window` | The details of the next scheduled backup, if any |
| `cancelled_at` | If the server has been cancelled, this is the date and time in ISO8601 format of that cancellation |
| `partner_id` | The server ID of the partner of this server, if one has been assigned |
| `permalink` | A randomly generated two-word identifier assigned to servers in regions that support this feature |
| `attached_backup` | An object that provides details of any backup image currently attached to the server |

**Suggested Formats:**
```bash
# Compact overview
bl preferences set format-servers "id,name,status,region,created_at"

# With resources
bl preferences set format-servers "id,name,vcpus,memory,disk,region,status"

# Network focused
bl preferences set format-servers "id,name,region,networks,vpc_id"

# Management view
bl preferences set format-servers "id,name,status,size_slug,image,created_at"
```

---

### Domains

**Config Key**: `format-domains`  
**Command**: `bl domain list`

**Default Fields:**
```
id,name,zone_file
```

**Available Fields:**

| Field | Description |
|-------|-------------|
| `id` | The ID of this domain |
| `name` | The name of the domain |
| `current_nameservers` | The current authoritative name servers for this domain |
| `zone_file` | The zone file for the selected domain. If the DNS records for this domain are not managed locally this is what the zone file would be if the authority was delegated to us |
| `ttl` | The time to live for records in this domain in seconds. If the DNS records for this domain are not managed locally this will be what the TTL would be if the authority was delegated to us |

**Suggested Formats:**
```bash
# Simple list
bl preferences set format-domains "id,name"

# With nameservers
bl preferences set format-domains "id,name,current_nameservers"

# Detailed
bl preferences set format-domains "id,name,current_nameservers,ttl"
```

---

### Additional Resources

For complete field references for all resource types (VPCs, Load Balancers, SSH Keys, Actions, Sizes, Regions, Invoices, Software, etc.), the CLI provides inline help:

```bash
# View available fields for any list command
bl image list --format "*"
bl server list --format "*"
bl domain list --format "*"
# etc.
```

Using `--format "*"` displays all available fields you can use in `--format` or preferences.

---

## Getting Help

### Command-Specific Help

```bash
# See available fields for a list command
bl image list --format "*"
bl server list --format "*"

# See all command options
bl server create --help
bl preferences --help
```

### View Current Preferences

```bash
# List all set preferences
bl preferences get

# View specific preference (value only)
bl preferences get default-region

# View preference with help and context
bl preferences show default-region

# View all preferences grouped by command
bl preferences show server create
bl preferences show terminal
```

### Configuration File Location

Preferences are stored in your system's config directory:

- **Linux/Mac**: `~/.config/binarylane/config.ini`
- **Windows**: `%APPDATA%\binarylane\config.ini`

You can manually edit this file if needed, though using `bl preferences set` is recommended.

---

## Tips and Best Practices

### 1. Start with Server Defaults

If you frequently create servers with similar configurations, set defaults first:

```bash
bl preferences set default-region syd
bl preferences set default-size std-min
bl preferences set default-image ubuntu-24.04
```

### 2. Use User Data Files for Reproducibility

Store your user-data files in version control and reference them in preferences:

```bash
bl preferences set default-user-data ~/projects/infra/user-data/dev-server.yaml
```

### 3. Different Contexts for Different Environments

Use contexts to maintain separate preferences for different environments:

```bash
# Development context
bl -c dev preferences set default-region syd
bl -c dev preferences set default-size std-min
bl -c dev preferences set default-image ubuntu-24.04

# Production context
bl -c prod preferences set default-region per
bl -c prod preferences set default-size std-4vcpu
bl -c prod preferences set default-image ubuntu-24.04

# Use them
bl -c dev server create --name dev-app-01
bl -c prod server create --name prod-app-01
```

### 4. Customize Output for Your Workflow

Set format preferences that match your needs:

```bash
# For quick scans
bl preferences set format-servers "id,name,status"

# For detailed management
bl preferences set format-servers "id,name,status,vcpus,memory,region,created_at"
```

### 5. Use preferences show for Discovery

When you can't remember what preferences are set for a workflow:

```bash
bl preferences show server create
bl preferences show terminal
```

---

## Security Notes

### API Tokens

While `api-token` is a valid configuration option, be aware that:
- Setting it via command line exposes it in shell history
- Use the interactive `bl configure` command for token management
- Environment variables are also supported (e.g., for CI/CD workflows)

```bash
# Recommended: Interactive (no shell history)
bl configure
```

### Sensitive Defaults

Be cautious with `default-password` - using SSH keys is more secure:

```bash
# Better: Use SSH keys
bl preferences set default-ssh-keys "aa:bb:cc:dd:..."

# Avoid: Storing passwords
bl preferences set default-password "..."  # Shows warning
```

---

## Complete Example Workflow

Here's a complete, realistic workflow for setting up a development environment:

### Step 1: Initial Setup (One Time)

```bash
# Set server creation defaults
bl preferences set default-region syd
bl preferences set default-size std-min
bl preferences set default-image ubuntu-24.04
bl preferences set default-user-data ~/.config/bl/my-user-data.yaml

# Set output formatting preferences
bl preferences set format-servers "id,name,status,region,created_at"
bl preferences set format-images "id,slug,distribution,status"

# Set terminal preferences
bl preferences set terminal-width 120
```

### Step 2: Verify Your Configuration

```bash
# Check server creation preferences
bl preferences show server create
# Output:
# Server Creation Defaults:
#   default-region    = syd
#   default-size      = std-min
#   default-image     = ubuntu-24.04
#   default-user-data = /home/user/.config/bl/my-user-data.yaml
#
# With your current defaults, this command:
#   bl server create --name myserver
#
# Expands to (what gets sent to the API):
#   bl server create --name myserver --region syd --size std-min --image ubuntu-24.04 --user-data ~/.config/bl/my-user-data.yaml

# Check Terminal Settings
bl preferences show terminal
# Output:
# Terminal Settings:
#   terminal-width = 120
```

### Step 3: Create Servers (Simplified)

**Before preferences:**
```bash
bl server create --name web-01 --size std-min --image ubuntu-24.04 --region syd --user-data ~/.config/bl/my-user-data.yaml
bl server create --name web-02 --size std-min --image ubuntu-24.04 --region syd --user-data ~/.config/bl/my-user-data.yaml
bl server create --name api-01 --size std-min --image ubuntu-24.04 --region syd --user-data ~/.config/bl/my-user-data.yaml
```

**After preferences:**
```bash
# Create servers with zero arguments
bl server create
# ↑ Uses: size=std-min, image=ubuntu-24.04, region=syd, user-data=my-user-data.yaml

bl server create
# ↑ Another server with same config

bl server create
# ↑ And another!

# Specify custom names when you need them
bl server create --name web-01
bl server create --name api-01

# Need a bigger server? Just override the size
bl server create --name db-01 --size std-4vcpu
# ↑ Override: size=std-4vcpu
# ↑ Uses preferences: image=ubuntu-24.04, region=syd, user-data=my-user-data.yaml

# Need a different OS? Just override the image
bl server create --image debian-12
# ↑ Override: image=debian-12
# ↑ Uses preferences: size=std-min, region=syd, user-data=my-user-data.yaml
```

### Step 4: View Servers with Your Format

```bash
# Lists automatically use your preferred format
bl server list
# Output (only shows your preferred columns):
# ID      NAME        STATUS  REGION  CREATED_AT
# 12345   web-01      active  syd     2024-01-15T10:30:00Z
# 12346   web-02      active  syd     2024-01-15T10:32:00Z
# 12347   api-01      active  syd     2024-01-15T10:35:00Z
# 12348   db-01       active  syd     2024-01-15T10:40:00Z

# Need more details for one command? Override the format
bl server list --format "id,name,vcpus,memory,disk,networks"
# ↑ Shows additional columns just for this one command
```

### Summary

With preferences configured, the minimal server create command is:
```bash
bl server create
```

All required fields (region, size, image) are populated from preferences. Optional fields like user-data are also applied if configured.

---

**For More Information:**
- Main documentation: [README.md](README.md)
- CLI source: [https://github.com/binarylane/binarylane-cli](https://github.com/binarylane/binarylane-cli)
- API documentation: [https://api.binarylane.com.au/reference](https://api.binarylane.com.au/reference)
