from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.console import Console

T = TypeVar("T", bound="ConsoleResponse")


@attr.s(auto_attribs=True)
class ConsoleResponse:
    """
    Attributes:
        console (Console):
    """

    console: Console
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        console = self.console.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "console": console,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        console = Console.from_dict(d.pop("console"))

        console_response = cls(
            console=console,
        )

        console_response.additional_properties = d
        return console_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
