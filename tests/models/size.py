from __future__ import annotations

from typing import Any, Dict, List, Union

import attr

from binarylane.types import UNSET, Unset


@attr.s(auto_attribs=True)
class Size:
    slug: str
    size_type: str
    available: bool
    regions: List[str]
    price_monthly: float
    price_hourly: float
    disk: int
    memory: int
    transfer: float
    excess_transfer_cost_per_gigabyte: float
    vcpus: int
    vcpu_units: str
    options: Dict[str, str]
    description: Union[Unset, None, str] = UNSET
    cpu_description: Union[Unset, None, str] = UNSET
    storage_description: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        slug = self.slug
        size_type = self.size_type

        available = self.available
        regions = self.regions

        price_monthly = self.price_monthly
        price_hourly = self.price_hourly
        disk = self.disk
        memory = self.memory
        transfer = self.transfer
        excess_transfer_cost_per_gigabyte = self.excess_transfer_cost_per_gigabyte
        vcpus = self.vcpus
        vcpu_units = self.vcpu_units
        options = self.options

        description = self.description
        cpu_description = self.cpu_description
        storage_description = self.storage_description

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "slug": slug,
                "size_type": size_type,
                "available": available,
                "regions": regions,
                "price_monthly": price_monthly,
                "price_hourly": price_hourly,
                "disk": disk,
                "memory": memory,
                "transfer": transfer,
                "excess_transfer_cost_per_gigabyte": excess_transfer_cost_per_gigabyte,
                "vcpus": vcpus,
                "vcpu_units": vcpu_units,
                "options": options,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if cpu_description is not UNSET:
            field_dict["cpu_description"] = cpu_description
        if storage_description is not UNSET:
            field_dict["storage_description"] = storage_description

        return field_dict
