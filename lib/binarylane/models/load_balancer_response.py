from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.load_balancer import LoadBalancer

T = TypeVar("T", bound="LoadBalancerResponse")


@attr.s(auto_attribs=True)
class LoadBalancerResponse:
    """
    Attributes:
        load_balancer (LoadBalancer):
    """

    load_balancer: LoadBalancer
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        load_balancer = self.load_balancer.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "load_balancer": load_balancer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        load_balancer = LoadBalancer.from_dict(d.pop("load_balancer"))

        load_balancer_response = cls(
            load_balancer=load_balancer,
        )

        load_balancer_response.additional_properties = d
        return load_balancer_response

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
