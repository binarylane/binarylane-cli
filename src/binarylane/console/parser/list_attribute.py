from __future__ import annotations

import argparse
from typing import TYPE_CHECKING, Any, Optional, Sequence, Union

from binarylane.types import UNSET

from binarylane.console.parser.object_attribute import ObjectAttribute

if TYPE_CHECKING:
    from binarylane.console.parser.parser import Parser


class SingleStoreAction(argparse.Action):
    """
    Similar to StoreAction, except each destination variable may only be written to once.

    This action is used when parsing list input, to help user avoid accidentally omitting the required keyword
    at start of each list item.
    """

    keyword: Optional[str] = None

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: Union[str, Sequence[Any], None],
        option_string: Optional[str] = None,
    ) -> None:
        if getattr(namespace, self.dest, self.default) is not self.default:
            parser.error(f"duplicate argument: {option_string} - ensure {self.keyword} is at start of each entry")
        setattr(namespace, self.dest, values)


class ListAttribute(ObjectAttribute):
    def __init__(
        self,
        attribute_name: str,
        attribute_type: type,
        *,
        required: bool,
        option_name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> None:
        # pylint: disable=duplicate-code
        super().__init__(
            attribute_name,
            attribute_type,
            required=required,
            option_name=option_name,
            description=description,
        )
        # A list can be empty, so in the command-line sense list item attributes are never required:
        self.required = False

    @property
    def keyword(self) -> str:
        keyword = self.attribute_name
        # FIXME: update openapi spec to provide this
        if keyword == "route_entries":
            keyword = "route"
        else:
            if keyword[-1] == "s":
                keyword = keyword[:-1]
            keyword = keyword.split("_")[-1]

        return f"+{keyword}"

    def configure(self, parser: Parser) -> None:
        if not self.description:
            self._unsupported("missing help", False)

        usage_descriptions = {self.keyword: "Required marker at start of each item."}
        usage_descriptions.update({attr.usage: attr.description or "" for attr in self.attributes if attr.usage})
        parser.add_group_help(title=self.title, description=self.description, entries=usage_descriptions)

        parser.add_keyword(self.keyword)
        parser.add_argument(
            self.attribute_name, type=str, nargs=argparse.PARSER, help=argparse.SUPPRESS
        ).required = False

    def _create_singlestore_action(self, **kwargs: Any) -> argparse.Action:
        action = SingleStoreAction(**kwargs)
        action.keyword = self.keyword
        return action

    def construct(self, parser: Parser, parsed: argparse.Namespace) -> object:
        remainder = getattr(parsed, self.attribute_name) or []
        delattr(parsed, self.attribute_name)

        # If the last option provided within this item happens to be of type List[T], the parser would not stop at
        # +keyword (as that's an argument). For this reason, we insert a do-nothing `--keyword+keyword` option before
        # each additional +keyword to ensure the parser stops.
        keyword_option = f"--keyword{self.keyword}"
        for index in [i for i, value in enumerate(remainder) if i and value == self.keyword][::-1]:
            remainder.insert(index, keyword_option)

        result = []
        while remainder:
            keyword = remainder.pop(0)
            if keyword != self.keyword:
                parser.error(f"unrecognized arguments: {keyword}")

            # Create a new subparser, of same class as the primary parser
            subparser = parser.__class__(prog=parser.prog)

            # Replace the subparser's default StoreAction with a SingleStoreAction
            subparser.register("action", None, self._create_singlestore_action)

            # Use the main parser's error handler, so that displayed usage is correct on error
            subparser.error = parser.error  # type: ignore

            super().configure(subparser)
            self.configure(subparser)
            subparser.add_argument(keyword_option, nargs=0, help=argparse.SUPPRESS)
            parsed = subparser.parse(remainder)

            result.append(super().construct(subparser, parsed))
            if result[-1] is UNSET:
                parser.error(f"argument {keyword}: expected one or more arguments")
            remainder = getattr(parsed, self.attribute_name)

        if not result and not self.init:
            return UNSET
        return result
