from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="LocalNameserversResponse")


@attr.s(auto_attribs=True)
class LocalNameserversResponse:
    """
    Attributes:
        local_nameservers (List[str]):
    """

    local_nameservers: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        local_nameservers = self.local_nameservers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "local_nameservers": local_nameservers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        local_nameservers = cast(List[str], d.pop("local_nameservers"))

        local_nameservers_response = cls(
            local_nameservers=local_nameservers,
        )

        local_nameservers_response.additional_properties = d
        return local_nameservers_response

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
