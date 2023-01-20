from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="FailoverIpsRequest")


@attr.s(auto_attribs=True)
class FailoverIpsRequest:
    """
    Attributes:
        failover_ips (List[str]): The list of failover IP addresses to assign to this server. This overwrites the
            current list, so any current failover IP addresses that are omitted will be removed from the server.
    """

    failover_ips: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        failover_ips = self.failover_ips

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "failover_ips": failover_ips,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        failover_ips = cast(List[str], d.pop("failover_ips"))

        failover_ips_request = cls(
            failover_ips=failover_ips,
        )

        failover_ips_request.additional_properties = d
        return failover_ips_request

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
