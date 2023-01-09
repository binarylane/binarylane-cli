from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="CurrentServerAlertsResponse")


@attr.s(auto_attribs=True)
class CurrentServerAlertsResponse:
    """
    Attributes:
        server_ids (List[int]):
    """

    server_ids: List[int]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server_ids = self.server_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server_ids": server_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        server_ids = cast(List[int], d.pop("server_ids"))

        current_server_alerts_response = cls(
            server_ids=server_ids,
        )

        current_server_alerts_response.additional_properties = d
        return current_server_alerts_response

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
