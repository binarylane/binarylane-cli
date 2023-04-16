""" BooleanOptionalAction imported from 3.9 """
from __future__ import annotations

import argparse
from typing import Any, Callable, Iterable, Optional, Sequence, Tuple, Union


# New to 3.9 - copied here to import if required
class BooleanOptionalAction(argparse.Action):
    def __init__(
        self,
        option_strings: Sequence[str],
        dest: str,
        default: Union[object, str, None] = None,
        type: Union[Callable[[str], object], argparse.FileType, None] = None,  # pylint: disable=redefined-builtin
        choices: Union[Iterable[object], None] = None,
        required: bool = False,
        help: Union[str, None] = None,  # pylint: disable=redefined-builtin
        metavar: Union[str, Tuple[str, ...], None] = None,
    ) -> None:
        _option_strings = []
        for option_string in option_strings:
            _option_strings.append(option_string)

            if option_string.startswith("--"):
                option_string = "--no-" + option_string[2:]
                _option_strings.append(option_string)

        if help is not None and default is not None and default is not argparse.SUPPRESS:
            help += " (default: %(default)s)"

        super().__init__(
            option_strings=_option_strings,
            dest=dest,
            nargs=0,
            default=default,
            type=type,
            choices=choices,
            required=required,
            help=help,
            metavar=metavar,
        )

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: Union[str, Sequence[Any], None],
        option_string: Optional[str] = None,
    ) -> None:
        if option_string is None:
            return
        if option_string in self.option_strings:
            setattr(namespace, self.dest, not option_string.startswith("--no-"))

    def format_usage(self) -> str:
        return " | ".join(self.option_strings)
