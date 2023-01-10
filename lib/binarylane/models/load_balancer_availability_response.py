from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.load_balancer_availability_option import LoadBalancerAvailabilityOption

T = TypeVar("T", bound="LoadBalancerAvailabilityResponse")


@attr.s(auto_attribs=True)
class LoadBalancerAvailabilityResponse:
    """
    Attributes:
        load_balancer_availability_options (List[LoadBalancerAvailabilityOption]):
    """

    load_balancer_availability_options: List[LoadBalancerAvailabilityOption]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        load_balancer_availability_options = []
        for load_balancer_availability_options_item_data in self.load_balancer_availability_options:
            load_balancer_availability_options_item = load_balancer_availability_options_item_data.to_dict()

            load_balancer_availability_options.append(load_balancer_availability_options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "load_balancer_availability_options": load_balancer_availability_options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        load_balancer_availability_options = []
        _load_balancer_availability_options = d.pop("load_balancer_availability_options")
        for load_balancer_availability_options_item_data in _load_balancer_availability_options:
            load_balancer_availability_options_item = LoadBalancerAvailabilityOption.from_dict(
                load_balancer_availability_options_item_data
            )

            load_balancer_availability_options.append(load_balancer_availability_options_item)

        load_balancer_availability_response = cls(
            load_balancer_availability_options=load_balancer_availability_options,
        )

        load_balancer_availability_response.additional_properties = d
        return load_balancer_availability_response

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
