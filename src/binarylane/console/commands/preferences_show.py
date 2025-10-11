from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List

from binarylane.config.options import OptionName

from binarylane.console.runners import ExitCode, Runner

if TYPE_CHECKING:
    from binarylane.console.parser import Parser


class Command(Runner):
    """Display preference values for a specific command or resource, or all preferences grouped by category"""

    # Map command patterns to relevant option prefixes
    COMMAND_GROUPS: Dict[str, tuple[str, List[OptionName]]] = {
        "server create": (
            "Server Creation Defaults",
            [
                OptionName.DEFAULT_REGION,
                OptionName.DEFAULT_SIZE,
                OptionName.DEFAULT_IMAGE,
                OptionName.DEFAULT_BACKUPS,
                OptionName.DEFAULT_SSH_KEYS,
                OptionName.DEFAULT_USER_DATA,
                OptionName.DEFAULT_PORT_BLOCKING,
                OptionName.DEFAULT_PASSWORD,
                OptionName.DEFAULT_VPC,
            ],
        ),
        "image list": (
            "Image List Preferences",
            [
                OptionName.FORMAT_IMAGES,
                OptionName.OUTPUT_FORMAT,
                OptionName.SHOW_HEADER,
            ],
        ),
        "server list": (
            "Server List Preferences",
            [
                OptionName.FORMAT_SERVERS,
                OptionName.OUTPUT_FORMAT,
                OptionName.SHOW_HEADER,
            ],
        ),
        "domain list": (
            "Domain List Preferences",
            [
                OptionName.FORMAT_DOMAINS,
                OptionName.OUTPUT_FORMAT,
                OptionName.SHOW_HEADER,
            ],
        ),
        "vpc list": (
            "VPC List Preferences",
            [
                OptionName.FORMAT_VPCS,
                OptionName.OUTPUT_FORMAT,
                OptionName.SHOW_HEADER,
            ],
        ),
        "load-balancer list": (
            "Load Balancer List Preferences",
            [
                OptionName.FORMAT_LOAD_BALANCERS,
                OptionName.OUTPUT_FORMAT,
                OptionName.SHOW_HEADER,
            ],
        ),
        "ssh-key list": (
            "SSH Key List Preferences",
            [
                OptionName.FORMAT_SSH_KEYS,
                OptionName.OUTPUT_FORMAT,
                OptionName.SHOW_HEADER,
            ],
        ),
        "action list": (
            "Action List Preferences",
            [
                OptionName.FORMAT_ACTIONS,
                OptionName.OUTPUT_FORMAT,
                OptionName.SHOW_HEADER,
            ],
        ),
        "size list": (
            "Size List Preferences",
            [
                OptionName.FORMAT_SIZES,
                OptionName.OUTPUT_FORMAT,
                OptionName.SHOW_HEADER,
            ],
        ),
        "region list": (
            "Region List Preferences",
            [
                OptionName.FORMAT_REGIONS,
                OptionName.OUTPUT_FORMAT,
                OptionName.SHOW_HEADER,
            ],
        ),
        "invoice list": (
            "Invoice List Preferences",
            [
                OptionName.FORMAT_INVOICES,
                OptionName.OUTPUT_FORMAT,
                OptionName.SHOW_HEADER,
            ],
        ),
        "software list": (
            "Software List Preferences",
            [
                OptionName.FORMAT_SOFTWARE,
                OptionName.OUTPUT_FORMAT,
                OptionName.SHOW_HEADER,
            ],
        ),
        "terminal": (
            "Terminal Settings",
            [
                OptionName.TERMINAL_WIDTH,
            ],
        ),
    }

    # Category groupings for displaying all preferences
    ALL_CATEGORIES: List[tuple[str, List[OptionName]]] = [
        (
            "Server Creation Defaults",
            [
                OptionName.DEFAULT_REGION,
                OptionName.DEFAULT_SIZE,
                OptionName.DEFAULT_IMAGE,
                OptionName.DEFAULT_BACKUPS,
                OptionName.DEFAULT_SSH_KEYS,
                OptionName.DEFAULT_USER_DATA,
                OptionName.DEFAULT_PORT_BLOCKING,
                OptionName.DEFAULT_PASSWORD,
                OptionName.DEFAULT_VPC,
            ],
        ),
        (
            "Output Formatting",
            [
                OptionName.FORMAT_IMAGES,
                OptionName.FORMAT_SERVERS,
                OptionName.FORMAT_DOMAINS,
                OptionName.FORMAT_VPCS,
                OptionName.FORMAT_LOAD_BALANCERS,
                OptionName.FORMAT_SSH_KEYS,
                OptionName.FORMAT_ACTIONS,
                OptionName.FORMAT_SIZES,
                OptionName.FORMAT_REGIONS,
                OptionName.FORMAT_INVOICES,
                OptionName.FORMAT_SOFTWARE,
                OptionName.OUTPUT_FORMAT,
                OptionName.SHOW_HEADER,
            ],
        ),
        (
            "Terminal Settings",
            [
                OptionName.TERMINAL_WIDTH,
            ],
        ),
    ]

    def configure(self, parser: Parser) -> None:
        parser.add_argument(
            "command_group",
            nargs="*",  # Optional - if empty, show all grouped
            help=f"Command or resource to show preferences for. Omit to show all preferences grouped by category. Valid options: {', '.join(repr(g) for g in self.COMMAND_GROUPS.keys())}",
        )

    def run(self, args: List[str]) -> None:
        if args == [self.CHECK]:
            return

        # Check for help first
        if args and args[0] in [self.HELP, "-h", "--help"]:
            self.parse(args)
            return

        # If no arguments, show all preferences grouped by category
        if not args:
            self._show_all_grouped()
            return

        # Join args to handle multi-word commands like "server create"
        command_group = " ".join(args).lower()

        # Check if it's a command group first
        if command_group in self.COMMAND_GROUPS:
            self._show_command_group(command_group)
            return

        # Check if it's a single preference key
        if len(args) == 1:
            preference_key = args[0].lower()
            # Try to find matching OptionName
            matching_option = None
            for option in OptionName:
                if option.value == preference_key:
                    matching_option = option
                    break

            if matching_option:
                self._show_single_preference(matching_option)
                return

        # Not a valid command group or preference key
        print(f"Unknown command group or preference: '{command_group}'")
        print("\nValid command groups:")
        for group in sorted(self.COMMAND_GROUPS.keys()):
            print(f"  {group}")
        print("\nOr show a specific preference by name:")
        print("  bl preferences show default-region")
        print("  bl preferences show terminal-width")
        print()
        print("Example usage:")
        print("  bl preferences show")
        print("  bl preferences show server create")
        print("  bl preferences show default-region")
        self.error(ExitCode.API, "Invalid command group or preference")

    def _get_option_description(self, option: OptionName) -> str:
        """Get a description for an option"""
        descriptions = {
            OptionName.TERMINAL_WIDTH: "Terminal width for help text formatting",
            OptionName.OUTPUT_FORMAT: "Output format (table, plain, tsv, json)",
            OptionName.SHOW_HEADER: "Show column headers in output",
            OptionName.FORMAT_IMAGES: "Custom columns for image list",
            OptionName.FORMAT_SERVERS: "Custom columns for server list",
            OptionName.FORMAT_DOMAINS: "Custom columns for domain list",
            OptionName.FORMAT_VPCS: "Custom columns for VPC list",
            OptionName.FORMAT_LOAD_BALANCERS: "Custom columns for load balancer list",
            OptionName.FORMAT_SSH_KEYS: "Custom columns for SSH key list",
            OptionName.FORMAT_ACTIONS: "Custom columns for action list",
            OptionName.FORMAT_SIZES: "Custom columns for size list",
            OptionName.FORMAT_REGIONS: "Custom columns for region list",
            OptionName.FORMAT_INVOICES: "Custom columns for invoice list",
            OptionName.FORMAT_SOFTWARE: "Custom columns for software list",
            OptionName.DEFAULT_REGION: "Default region for server creation",
            OptionName.DEFAULT_SIZE: "Default size for server creation",
            OptionName.DEFAULT_IMAGE: "Default image for server creation",
            OptionName.DEFAULT_BACKUPS: "Enable backups by default (API default: false)",
            OptionName.DEFAULT_PORT_BLOCKING: "Disable port blocking (API default: true/enabled)",
            OptionName.DEFAULT_SSH_KEYS: "Default SSH key IDs (comma-separated)",
            OptionName.DEFAULT_USER_DATA: "Default cloud-init user data",
            OptionName.DEFAULT_PASSWORD: "Default root/administrator password",
            OptionName.DEFAULT_VPC: "Default VPC ID for server creation",
        }
        return descriptions.get(option, "")

    def _show_command_group(self, command_group: str) -> None:
        """Display preferences for a specific command group"""
        title, option_names = self.COMMAND_GROUPS[command_group]
        print(f"{title}:")
        print()

        # Find the longest key name for formatting
        max_key_len = max(len(opt.value) for opt in option_names)

        # Separate set and unset options
        set_options = []
        unset_options = []
        for option in option_names:
            value = self._context.get_option(option)
            if value is not None:
                set_options.append((option, value))
            else:
                unset_options.append(option)

        # Show currently set preferences
        if set_options:
            print("Currently set:")
            print()
            for option, value in set_options:
                print(f"  {option.value:<{max_key_len}} = {value}")
            print()

        # Show available (not set) preferences
        if unset_options:
            print("Available (not set):")
            print()
            for option in unset_options:
                description = self._get_option_description(option)
                if description:
                    print(f"  {option.value:<{max_key_len}} - {description}")
                else:
                    print(f"  {option.value}")
            print()

        if not set_options and not unset_options:
            print(f"  (no preferences available for {command_group})")
            print()

        # For server create, show missing required fields and example command
        if command_group == "server create":
            self._show_missing_required_fields()
            self._show_example_command()

        print("To set a preference: bl preferences set <key> <value>")
        print("To unset: bl preferences set <key> null")

    def _show_missing_required_fields(self) -> None:
        """Show which required server creation fields are not set as defaults"""
        # Required fields for server creation
        required_fields = [
            (OptionName.DEFAULT_REGION, "--region REGION", "bl region list"),
            (OptionName.DEFAULT_SIZE, "--size SIZE", "bl size list"),
            (OptionName.DEFAULT_IMAGE, "--image IMAGE", "bl image list"),
        ]

        missing = []
        for option, arg_format, list_cmd in required_fields:
            value = self._context.get_option(option)
            if value is None:
                missing.append((arg_format, list_cmd))

        if missing:
            print()
            print("Required for server creation (provide via command line or set as preference defaults):")
            for arg_format, list_cmd in missing:
                print(f"  {arg_format:<20} (see: {list_cmd})")
        else:
            print()
            print("All required server creation fields have default values set.")

    def _show_example_command(self) -> None:
        """Show what the command would look like with current defaults applied"""
        # Check which preferences are set
        preference_map = [
            (OptionName.DEFAULT_REGION, "--region"),
            (OptionName.DEFAULT_SIZE, "--size"),
            (OptionName.DEFAULT_IMAGE, "--image"),
            (OptionName.DEFAULT_BACKUPS, "--backups"),
            (OptionName.DEFAULT_PORT_BLOCKING, "--port-blocking"),
            (OptionName.DEFAULT_SSH_KEYS, "--ssh-keys"),
            (OptionName.DEFAULT_USER_DATA, "--user-data"),
            (OptionName.DEFAULT_PASSWORD, "--password"),
            (OptionName.DEFAULT_VPC, "--vpc"),
        ]

        args = []
        for option, flag in preference_map:
            value = self._context.get_option(option)
            if value is not None:
                # Handle boolean values - convert to --flag or --no-flag format
                if option in (OptionName.DEFAULT_BACKUPS, OptionName.DEFAULT_PORT_BLOCKING):
                    bool_value = value.lower() in ("true", "1", "yes", "on")
                    if bool_value:
                        args.append(flag)
                    else:
                        # Convert --backups to --no-backups, --port-blocking to --no-port-blocking
                        no_flag = flag.replace("--", "--no-", 1)
                        args.append(no_flag)
                else:
                    args.append(f"{flag} {value}")

        if args:
            print()
            print("With your current defaults, this command:")
            print("  bl server create --name myserver")
            print()
            print("Expands to (what gets sent to the API):")
            print(f"  bl server create --name myserver {' '.join(args)}")
            print()

    def _show_single_preference(self, option: OptionName) -> None:
        """Display detailed information about a single preference"""
        key = option.value
        value = self._context.get_option(option)
        description = self._get_option_description(option)

        # Don't show sensitive values
        if key in {"api-token", "default-password"}:
            print(f"{key}: (sensitive - use 'bl preferences get {key}' to view)")
            return

        # Show current value
        if value is not None:
            print(f"{key} = {value}")
        else:
            print(f"{key} is not set")

        print()

        # Show description if available
        if description:
            print(f"Description: {description}")
            print()

        # Show help/examples based on the key
        help_info = self._get_help_info_for_key(key)
        if help_info:
            for line in help_info:
                print(f"  {line}")
            print()

        print(f"To set: bl preferences set {key} <value>")
        print(f"To unset: bl preferences set {key} null")

    def _get_help_info_for_key(self, key: str) -> List[str]:
        """Get help information for a specific preference key"""

        # API-sourced list values
        if key == "default-region":
            return ["Available regions: bl region list", "Example: bl preferences set default-region syd"]
        elif key == "default-size":
            return ["Available sizes: bl size list", "Example: bl preferences set default-size std-min"]
        elif key == "default-image":
            return ["Available images: bl image list", "Example: bl preferences set default-image ubuntu-24.04"]

        # Boolean values
        elif key == "default-port-blocking":
            return [
                "Valid values: false (to disable port blocking)",
                "Default (if not set): true (port blocking enabled)",
                "Example: bl preferences set default-port-blocking false",
            ]
        elif key == "default-backups":
            return [
                "Valid values: true (to enable backups)",
                "Default (if not set): false (backups disabled)",
                "Example: bl preferences set default-backups true",
            ]

        # Format preferences
        elif key.startswith("format-"):
            format_to_command = {
                "format-servers": "server",
                "format-images": "image",
                "format-domains": "domain",
                "format-vpcs": "vpc",
                "format-load-balancers": "load-balancer",
                "format-ssh-keys": "ssh-key",
                "format-actions": "action",
                "format-sizes": "size",
                "format-regions": "region",
                "format-invoices": "account invoice",
                "format-software": "software",
            }
            command = format_to_command.get(key, key.replace("format-", ""))
            return [
                f'Available fields: bl {command} list --output "*"',
                f'Example: bl preferences set {key} "id,name,status"',
                "Note: Use quotes for comma-separated values",
            ]

        # File path
        elif key == "default-user-data":
            return [
                "Path to user-data file for server initialization",
                "Example: bl preferences set default-user-data ~/.config/bl/my-user-data.yaml",
                "Note: File must exist",
            ]

        # SSH keys
        elif key == "default-ssh-keys":
            return [
                "Available SSH keys: bl ssh-key list",
                'Example (single): bl preferences set default-ssh-keys "aa:bb:cc:..."',
                'Example (multiple): bl preferences set default-ssh-keys "aa:bb:cc:...,11:22:33:..."',
            ]

        # VPC
        elif key == "default-vpc":
            return ["Available VPCs: bl vpc list", "Example: bl preferences set default-vpc 12345"]

        # Terminal width
        elif key == "terminal-width":
            return [
                "Valid values: numeric (e.g., 120)",
                "Example: bl preferences set terminal-width 120",
                "To use auto-detection: bl preferences set terminal-width null",
            ]

        # Output format
        elif key == "output-format":
            return ["Valid values: table, plain, tsv, json", "Example: bl preferences set output-format json"]

        # Show header
        elif key == "show-header":
            return ["Valid values: true, false", "Example: bl preferences set show-header false"]

        # Password (discouraged)
        elif key == "default-password":
            return [
                "Warning: Storing passwords is not recommended",
                "Consider using SSH keys instead (default-ssh-keys)",
                "Example: bl preferences set default-password <password>",
            ]

        # Generic fallback
        return [f"Example: bl preferences set {key} <value>"]

    def _show_all_grouped(self) -> None:
        """Display all set preferences grouped by category"""
        # Sensitive keys to exclude from display
        sensitive_keys = {"api-token", "default-password"}

        total_count = 0
        has_any_values = False

        for category_name, option_names in self.ALL_CATEGORIES:
            # Collect values for this category
            category_values = []
            for option in option_names:
                if option.value in sensitive_keys:
                    continue
                value = self._context.get_option(option)
                if value is not None:
                    category_values.append((option.value, value))

            # Only display category if it has values
            if category_values:
                has_any_values = True
                print(f"{category_name}:")

                # Find the longest key name in this category for formatting
                max_key_len = max(len(key) for key, _ in category_values)

                for key, value in category_values:
                    print(f"  {key:<{max_key_len}} = {value}")
                    total_count += 1

                print()  # Blank line between categories

        if not has_any_values:
            print("No preferences are currently set.")
            print()
            print("To set a preference, use:")
            print("  bl preferences set <key> <value>")
            print()
            print("To view preferences for a specific command:")
            print("  bl preferences show server create")
            print("  bl preferences show output")
        else:
            print(f"Total: {total_count} preference(s) set")
            print()
            print("Note: Sensitive values (api-token, default-password) are not displayed.")
            print("      Use 'bl preferences show <command>' to view specific command preferences.")
