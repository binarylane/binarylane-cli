from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="Host")


@attr.s(auto_attribs=True)
class Host:
    """
    Attributes:
        display_name (str): The name for this host.
        uptime_ms (Union[Unset, None, int]): The current uptime in milliseconds of this host.
        status_page (Union[Unset, None, str]): This is the URL of the status page of the host. This will normally only
            be set if the host is under maintenance.
    """

    display_name: str
    uptime_ms: Union[Unset, None, int] = UNSET
    status_page: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        uptime_ms = self.uptime_ms
        status_page = self.status_page

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "display_name": display_name,
            }
        )
        if uptime_ms is not UNSET:
            field_dict["uptime_ms"] = uptime_ms
        if status_page is not UNSET:
            field_dict["status_page"] = status_page

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("display_name")

        uptime_ms = d.pop("uptime_ms", UNSET)

        status_page = d.pop("status_page", UNSET)

        host = cls(
            display_name=display_name,
            uptime_ms=uptime_ms,
            status_page=status_page,
        )

        host.additional_properties = d
        return host

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
