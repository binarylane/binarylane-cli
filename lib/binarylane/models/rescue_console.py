from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RescueConsole")


@attr.s(auto_attribs=True)
class RescueConsole:
    """
    Attributes:
        url (str): The URL for the embedded version of the rescue console.
        fullscreen_url (str): The URL for the full screen version of the rescue console.
        width (int): Rescue console native width.
        height (int): Rescue console native height.
    """

    url: str
    fullscreen_url: str
    width: int
    height: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        fullscreen_url = self.fullscreen_url
        width = self.width
        height = self.height

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "fullscreen_url": fullscreen_url,
                "width": width,
                "height": height,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        fullscreen_url = d.pop("fullscreen_url")

        width = d.pop("width")

        height = d.pop("height")

        rescue_console = cls(
            url=url,
            fullscreen_url=fullscreen_url,
            width=width,
            height=height,
        )

        rescue_console.additional_properties = d
        return rescue_console

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
