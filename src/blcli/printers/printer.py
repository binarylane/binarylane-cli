# pylint: disable=missing-module-docstring

from abc import ABC, abstractmethod
from typing import Any, List, Optional, Sequence, Union

from ..cli import debug

NULL_STR = ""


class Printer(ABC):
    """A Printer is responsible for formatting a structured API response and printing it to stdout"""

    _header: bool

    def __init__(self) -> None:
        self._header = True

    @property
    def header(self) -> bool:
        """Boolean specifying whether output should include field names in a header."""
        return self._header

    @header.setter
    def header(self, value: bool) -> None:
        self._header = value

    @abstractmethod
    def print_list(self, response: List[Any], fields: Optional[List[str]] = None) -> None:
        """Format response and print to stdout"""

    def print_object(self, response: Any) -> None:
        """Format structured API response object and print to stdout"""
        self.print_list(response)


class _TablePrinter(Printer):
    def print_list(self, response: List[Any], fields: Optional[List[str]] = None) -> None:
        response_type = type(response)
        # print(f"-- {response_type} ({response_type.__module__}) --")
        primary = None
        primary_type = None

        for name, _type in response_type.__annotations__.items():
            if name == "additional_properties":
                continue
            # get inner type if it is generic
            if getattr(_type, "__origin__", None):
                _type = _type.__args__[0]

            if response_type.__module__.startswith(_type.__module__) or _type is str:
                primary = name
                primary_type = _type

        if not primary:
            primary_type = response_type
        else:
            response = getattr(response, primary)

        if isinstance(response, list):
            for key, value in getattr(primary_type, "__annotations__", {"item": "value"}).items():
                debug(f'{key}: {value} dict?{hasattr(value, "to_dict")} origin:{getattr(value, "__origin__", None)}')

            header = fields or [
                key
                for key, value in getattr(primary_type, "__annotations__", {"item": "value"}).items()
                if key != "additional_properties"
                and not hasattr(value, "to_dict")
                and not getattr(value, "__origin__", None) in (Union, list)
            ]

            data = [header] if self.header else []
            data += [
                self.flatten(
                    [item]
                    if isinstance(item, str)
                    else [value for key, value in item.to_dict().items() if key in header]
                )
                for item in response
            ]
        elif isinstance(response, str):
            data = []
            print(response)
        else:
            data = [["Name", "Value"]] + [self.flatten(item, True) for item in response.to_dict().items()]

        if len(data) > 1:
            self._print(data)

    @abstractmethod
    def _print(self, data: Any) -> None:
        """Class-specific printer behaviour"""

    def flatten(self, values: Sequence[Any], single_object: bool = False) -> List[str]:
        """Transform each item in values into a format more suitable for displaying"""

        result: List[str] = []
        max_list = 5
        max_str = 80
        trunc = "..."

        for item in values:
            item_type = type(item)
            if item_type is list:
                if len(item) > max_list:
                    item = item[:max_list] + [trunc]
                if not single_object:
                    item = ", ".join(map(str, item))
                else:
                    item = (
                        "- "
                        + "\n- ".join(
                            [
                                (
                                    "  ".join(f"{key}: {value}\n" for key, value in i.items())
                                    if isinstance(i, dict)
                                    else str(i)
                                )
                                for i in item
                            ]
                        )
                        if item
                        else ""
                    )
            if item_type is dict:
                for key in ("display_name", "name", "slug", "id"):
                    if key in item:
                        item = item[key]
                        break
                else:
                    item = (
                        "<object>"
                        if not single_object
                        else "\n".join([f"{key}: {value}" for key, value in item.items()])
                    )
            if item_type is bool:
                item = "Yes" if item else "No"

            item = str(item) if item is not None else NULL_STR
            if len(item) > max_str + len(trunc):
                item = item[:max_str] + trunc
            result.append(item)

        return result
