from __future__ import annotations

import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="Console")


@attr.s(auto_attribs=True)
class Console:
    """
    Attributes:
        iframe (str): The URL for the embedded version of the console.
        browser (str): The URL for the full screen and full featured version of the console.
        width (int): Rescue console native width.
        height (int): Rescue console native height.
        expiry (datetime.datetime): The expiry time of the provided URLs.
    """

    iframe: str
    browser: str
    width: int
    height: int
    expiry: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        iframe = self.iframe
        browser = self.browser
        width = self.width
        height = self.height
        expiry = self.expiry.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iframe": iframe,
                "browser": browser,
                "width": width,
                "height": height,
                "expiry": expiry,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        iframe = d.pop("iframe")

        browser = d.pop("browser")

        width = d.pop("width")

        height = d.pop("height")

        expiry = isoparse(d.pop("expiry"))

        console = cls(
            iframe=iframe,
            browser=browser,
            width=width,
            height=height,
            expiry=expiry,
        )

        console.additional_properties = d
        return console

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
