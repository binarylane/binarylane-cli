from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerAvailabilityOption")


@attr.s(auto_attribs=True)
class LoadBalancerAvailabilityOption:
    """
    Attributes:
        anycast (bool): If true this is an Anycast load balancer option.
        price_monthly (float): Monthly Price in AU$.
        price_hourly (float): Hourly price in AU$.
        regions (Union[Unset, None, List[str]]): The slugs of regions where this load balancer option is available. If
            this is an Anycast load balancer option this will be null.
    """

    anycast: bool
    price_monthly: float
    price_hourly: float
    regions: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        anycast = self.anycast
        price_monthly = self.price_monthly
        price_hourly = self.price_hourly
        regions: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.regions, Unset):
            if self.regions is None:
                regions = None
            else:
                regions = self.regions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "anycast": anycast,
                "price_monthly": price_monthly,
                "price_hourly": price_hourly,
            }
        )
        if regions is not UNSET:
            field_dict["regions"] = regions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        anycast = d.pop("anycast")

        price_monthly = d.pop("price_monthly")

        price_hourly = d.pop("price_hourly")

        regions = cast(List[str], d.pop("regions", UNSET))

        load_balancer_availability_option = cls(
            anycast=anycast,
            price_monthly=price_monthly,
            price_hourly=price_hourly,
            regions=regions,
        )

        load_balancer_availability_option.additional_properties = d
        return load_balancer_availability_option

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
