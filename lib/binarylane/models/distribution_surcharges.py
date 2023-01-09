from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="DistributionSurcharges")


@attr.s(auto_attribs=True)
class DistributionSurcharges:
    """
    Attributes:
        surcharge_base_cost (Union[Unset, None, float]): The additional cost for using this operating system as the base
            image for a size.
        surcharge_per_memory_megabyte (Union[Unset, None, float]): The additional cost per MB for using this operating
            system as the base image for a size.
        surcharge_per_memory_max_megabytes (Union[Unset, None, int]): The maximum memory in MB that counts towards the
            surcharge_per_memory_mb. Any memory above this cap does not attract the surcharge.
        surcharge_per_vcpu (Union[Unset, None, float]): The additional cost per vcpu for using this operating system as
            the base image for a size.
        surcharge_min_vcpu (Union[Unset, None, int]): The minimum vcpu count for surcharge calculations.
    """

    surcharge_base_cost: Union[Unset, None, float] = UNSET
    surcharge_per_memory_megabyte: Union[Unset, None, float] = UNSET
    surcharge_per_memory_max_megabytes: Union[Unset, None, int] = UNSET
    surcharge_per_vcpu: Union[Unset, None, float] = UNSET
    surcharge_min_vcpu: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        surcharge_base_cost = self.surcharge_base_cost
        surcharge_per_memory_megabyte = self.surcharge_per_memory_megabyte
        surcharge_per_memory_max_megabytes = self.surcharge_per_memory_max_megabytes
        surcharge_per_vcpu = self.surcharge_per_vcpu
        surcharge_min_vcpu = self.surcharge_min_vcpu

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if surcharge_base_cost is not UNSET:
            field_dict["surcharge_base_cost"] = surcharge_base_cost
        if surcharge_per_memory_megabyte is not UNSET:
            field_dict["surcharge_per_memory_megabyte"] = surcharge_per_memory_megabyte
        if surcharge_per_memory_max_megabytes is not UNSET:
            field_dict["surcharge_per_memory_max_megabytes"] = surcharge_per_memory_max_megabytes
        if surcharge_per_vcpu is not UNSET:
            field_dict["surcharge_per_vcpu"] = surcharge_per_vcpu
        if surcharge_min_vcpu is not UNSET:
            field_dict["surcharge_min_vcpu"] = surcharge_min_vcpu

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        surcharge_base_cost = d.pop("surcharge_base_cost", UNSET)

        surcharge_per_memory_megabyte = d.pop("surcharge_per_memory_megabyte", UNSET)

        surcharge_per_memory_max_megabytes = d.pop("surcharge_per_memory_max_megabytes", UNSET)

        surcharge_per_vcpu = d.pop("surcharge_per_vcpu", UNSET)

        surcharge_min_vcpu = d.pop("surcharge_min_vcpu", UNSET)

        distribution_surcharges = cls(
            surcharge_base_cost=surcharge_base_cost,
            surcharge_per_memory_megabyte=surcharge_per_memory_megabyte,
            surcharge_per_memory_max_megabytes=surcharge_per_memory_max_megabytes,
            surcharge_per_vcpu=surcharge_per_vcpu,
            surcharge_min_vcpu=surcharge_min_vcpu,
        )

        distribution_surcharges.additional_properties = d
        return distribution_surcharges

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
