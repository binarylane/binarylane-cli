from __future__ import annotations

import argparse
import logging
import shutil
from argparse import HelpFormatter
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Sequence, Union

from binarylane.console.parser.help_formatter import CommandHelpFormatter
from binarylane.console.parser.object_attribute import Mapping

if TYPE_CHECKING:
    from typing_extensions import TypeAlias

    ArgumentGroup: TypeAlias = argparse._ArgumentGroup  # pylint: disable=protected-access

logger = logging.getLogger(__name__)


class Namespace(argparse.Namespace):
    mapped_object: Any


# FIXME: Wrap ArgumentParser instead of subclassing it
class Parser(argparse.ArgumentParser):

    _argument_names: List[str]
    _mapping: Optional[Mapping] = None
    _parsed: Optional[argparse.Namespace] = None
    _configured: bool = False
    _keywords: List[str]
    _groups: Dict[str, ArgumentGroup]
    _dest_counter: int = 0

    def __init__(self, prog: str, description: Optional[str] = None, epilog: Optional[str] = None) -> None:
        super().__init__(prog=prog, description=description, epilog=epilog, add_help=False, allow_abbrev=False)

        self._groups = {
            "required=True": self.add_argument_group(title="Arguments"),
            "required=False": self.add_argument_group(title="Parameters"),
        }
        self._optionals.title = "Options"
        self._argument_names = []
        self._keywords = []

    def _get_formatter(self) -> HelpFormatter:
        # argparse defaults to 70 when terminal size is unavailable, which is rather narrow
        size = shutil.get_terminal_size((80, 25))
        return CommandHelpFormatter(self.prog, width=size.columns - 2)

    @property
    def argument_names(self) -> List[str]:
        # Make a copy:
        return list(self._argument_names)

    def configure(self) -> None:
        if not self._configured and self._mapping:
            self._mapping.configure(self)
        self._configured = True

    def add_keyword(self, keyword: str) -> None:
        self._keywords.append(keyword)

    def add_group_help(self, *, title: str, description: Optional[str] = None, entries: Dict[str, str]) -> None:
        group = self.add_group(title, description)
        for key, value in entries.items():
            # FIXME: Use HelpFormatter to create an epilog instead
            #
            # NOTE: These group arguments will never parse, the group exists purely to provide argparse-formatted help -
            # dest: argparse needs it to be unique, but we otherwise dont need it
            # metavar: field name, displayed as-is in argument group's help
            # nargs: SUPPRESS (since python 3.7) will cause it to accept no arguments nor be shown in usage
            # default: SUPPRESS so that `dest` is not added to parsed namespace object
            # help: description of the field
            group.add_argument(
                self._create_dest(), metavar=key, nargs=argparse.SUPPRESS, default=argparse.SUPPRESS, help=value
            ).required = False

    def _create_dest(self) -> str:
        """Obtain a unique dest value"""
        self._dest_counter += 1
        return f"_dest_{self._dest_counter}"

    def _format_usage(self) -> str:
        mapping_usage = []
        if self._mapping:
            attributes = self._mapping.attributes
            for attr in attributes:
                if attr.required:
                    attributes += attr.attributes

            mapping_usage += [arg.usage for arg in attributes if arg.required and arg.usage]
            if any(not arg.required for arg in attributes if arg.usage):
                mapping_usage.append("[PARAMETERS]")
            mapping_usage += [f"[{keyword} ... ]" for keyword in self._keywords]

        return f"{self.prog} [OPTIONS] {' '.join(mapping_usage)}"

    def parse(self, args: Sequence[str]) -> Namespace:
        self.configure()
        self.usage = self._format_usage()

        self._parsed = self.parse_args(args, Namespace())
        if self._mapping:
            self._parsed.mapped_object = self._mapping.construct(self, self._parsed)

        return self._parsed

    def set_mapping(self, mapping: Mapping) -> Mapping:
        self._mapping = mapping
        return mapping

    def add_group(self, group_name: str, description: Optional[str] = None) -> ArgumentGroup:
        if group_name not in self._groups:
            self._groups[group_name] = self.add_argument_group(title=group_name, description=description)
        return self._groups[group_name]

    def add_to_group(self, group_name: Union[str, bool], name_or_flag: str, type_: type, **kwargs: Any) -> None:
        self._argument_names.append(name_or_flag)

        if isinstance(group_name, bool):
            group_name = f"required={group_name}"
        elif group_name not in self._groups:
            logger.warning("%s not added to groups yet", group_name)
            self.add_group(group_name)

        # Place argument in appropriate group:
        group = self._groups[group_name]

        # argparse wont accept required for a po=True
        if name_or_flag[0] not in self.prefix_chars and "required" in kwargs:
            del kwargs["required"]

        logger.debug("add_argument %s (%s) - %s", name_or_flag, type_, repr(kwargs))
        group.add_argument(name_or_flag, type=type_, **kwargs)
