from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="DomainRefreshRequest")


@attr.s(auto_attribs=True)
class DomainRefreshRequest:
    """
    Attributes:
        domain_names (List[str]): The domain names to refresh.
    """

    domain_names: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        domain_names = self.domain_names

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain_names": domain_names,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        domain_names = cast(List[str], d.pop("domain_names"))

        domain_refresh_request = cls(
            domain_names=domain_names,
        )

        domain_refresh_request.additional_properties = d
        return domain_refresh_request

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
