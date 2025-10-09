from __future__ import annotations

from typing import TYPE_CHECKING, List

from binarylane.config.options import OptionName

from binarylane.console.runners import ExitCode, Runner

if TYPE_CHECKING:
    from binarylane.console.parser import Parser


class Command(Runner):
    """Display a preference value for a given key, or list all set preferences"""

    def configure(self, parser: Parser) -> None:
        parser.add_argument(
            "key",
            nargs="?",  # Make key optional
            help="Preference key to retrieve (omit to list all set preferences)",
        )

    def run(self, args: List[str]) -> None:
        if args == [self.CHECK]:
            return

        # Check for help first
        if args and args[0] in [self.HELP, "-h", "--help"]:
            self.parse(args)
            return

        # If no arguments, list all set preferences
        if not args:
            self._list_all_preferences()
            return

        # Get specific preference
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

        value = self._context.get_option(option)
        if value is None:
            print(f"{key} is not set")
        else:
            print(f"{key} = {value}")

    def _list_all_preferences(self) -> None:
        """List all preferences that have been set"""
        # Sensitive keys to exclude from listing
        sensitive_keys = {"api-token", "default-password"}

        set_preferences = []

        for option in OptionName:
            # Skip sensitive values
            if option.value in sensitive_keys:
                continue

            value = self._context.get_option(option)
            if value is not None:
                set_preferences.append((option.value, value))

        if not set_preferences:
            print("No preferences are currently set.")
            print("\nTo set a preference, use:")
            print("  bl preferences set KEY VALUE")
            print("\nAvailable preference keys:")
            for opt in OptionName:
                print(f"  {opt.value}")
        else:
            print("Currently set preferences:")
            print()
            # Find the longest key name for formatting
            max_key_len = max(len(key) for key, _ in set_preferences)
            for key, value in sorted(set_preferences):
                print(f"  {key:<{max_key_len}} = {value}")
            print()
            print(f"Total: {len(set_preferences)} preference(s) set")
            print()
            print("Note: Sensitive values (api-token, default-password) are not listed.")
            print("      Use 'bl preferences get <key>' to retrieve them individually.")
