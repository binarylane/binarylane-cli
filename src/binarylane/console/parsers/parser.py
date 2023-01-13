from __future__ import annotations

import argparse
import logging
from typing import Any, Optional, Type

from binarylane.console.parsers.argument import CommandArgument
from binarylane.console.parsers.help_formatter import CommandHelpFormatter

logger = logging.getLogger(__name__)


class CommandParser(argparse.ArgumentParser):
    """Enhanced ArgumentParser with support for generic types"""

    def __init__(self, **kwargs: Any) -> None:
        kwargs["formatter_class"] = CommandHelpFormatter
        kwargs["add_help"] = False
        kwargs["allow_abbrev"] = False
        super().__init__(**kwargs)

        self.arguments_group = self.add_argument_group(title="Arguments")
        self.modifiers_group = self.add_argument_group(title="Modifiers")
        self._optionals.title = "Options"

    def cli_argument(
        self,
        name: str,
        _type: object,
        *,
        dest: Optional[str] = None,
        required: Optional[bool] = None,
        description: Optional[str] = None,
        action: Optional[Type[argparse.Action]] = None,
        warning: Optional[str] = None,
    ) -> None:
        """Add CLI argument to parser"""

        if warning:
            logger.warning(f"{self.prog} - {warning}")

        argument = CommandArgument(name, _type, dest=dest, required=required, description=description, action=action)
        argument.add_to_parser(self)
