from __future__ import annotations

from typing import TYPE_CHECKING, List

from binarylane.config.options import OptionName
from binarylane.config.sources import FileSource

from binarylane.console.runners import ExitCode, Runner

if TYPE_CHECKING:
    from binarylane.console.parser import Parser


class Command(Runner):
    """Set or unset a preference value"""

    def configure(self, parser: Parser) -> None:
        parser.add_argument("key", help="Preference key to set")
        parser.add_argument("value", help='Value to set (or "null" to unset)')

    def run(self, args: List[str]) -> None:
        if args == [self.CHECK]:
            return

        # Check for help first
        if not args or args[0] in [self.HELP, "-h", "--help"]:
            self.parse(args)
            return

        key = args[0]

        # Validate key is a known option
        try:
            option = OptionName(key)
        except ValueError:
            print(f"Unknown preference key: {key}")
            print("\nValid keys:")
            for opt in OptionName:
                print(f"  {opt.value}")
            self.error(ExitCode.API, "Invalid preference key")

        # If no value provided, show contextual help
        if len(args) < 2:
            self._show_preference_help(option)
            return

        value = args[1]

        # Update the file source directly
        file_source = self._context.get_source(FileSource)

        if value and value.lower() == "null":
            # Unset the key
            file_source._section.pop(option.value, None)
            print(f"Unset {key}")
        else:
            # Warn about sensitive values
            if key.lower() in ["api-token", "password", "default-password"]:
                print("⚠️  WARNING: Storing sensitive value in config file.")
                print(f"   Consider using environment variable instead: BL_{key.upper().replace('-', '_')}")
                print()

            # Set the key
            file_source._section[option.value] = value
            print(f"Set {key} = {value}")

        # Save to disk
        if file_source._path is None:
            self.error(ExitCode.API, "Cannot save preferences: config file path is not set")

        with open(file_source._path, "w", encoding="utf-8") as f:
            file_source._parser.write(f)

    def _show_preference_help(self, option: OptionName) -> None:
        """Show contextual help for a specific preference key"""
        key = option.value
        current_value = self._context.get_option(option)

        # Show current value
        if current_value is not None:
            # Don't display sensitive values
            if key in ["api-token", "default-password"]:
                print("Currently set to: (hidden)")
            else:
                print(f"Currently set to: {current_value}")
        else:
            print("(not currently set)")

        print()

        # Category-specific help
        help_info = self._get_help_info(key)
        for line in help_info:
            print(line)

        print()
        print(f"To set: bl preferences set {key} <value>")
        print(f"To unset: bl preferences set {key} null")

    def _get_help_info(self, key: str) -> List[str]:
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
        elif key == "default-ipv6":
            return ["Valid values: true, false", "Example: bl preferences set default-ipv6 true"]

        # Format preferences
        elif key.startswith("format-"):
            # Map format-* keys to their CLI command names
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
                "Path to cloud-config YAML file for server initialization",
                "Example: bl preferences set default-user-data ~/.config/bl/cloud-init.yaml",
                "Note: File must exist and contain valid cloud-config YAML",
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

        # Generic fallback
        else:
            return [f"Example: bl preferences set {key} <value>"]
