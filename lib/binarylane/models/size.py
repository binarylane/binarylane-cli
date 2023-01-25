from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from binarylane.models.size_options import SizeOptions
from binarylane.models.size_type import SizeType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="Size")


@attr.s(auto_attribs=True)
class Size:
    """
    Attributes:
        slug (str): The slug of this size.
        size_type (SizeType): The type of this size, generally used to differentiate sizes optimized for different
            usages.
        available (bool): If this is false the size is not available for new servers.
        regions (List[str]): A list of region slugs where this size is available regardless of stock.
            If this a response to a query that included a selected operating system this response will only include regions
            where that operating system is available on this size,
            otherwise not all regions listed will support all operating systems on this size.
        price_monthly (float): Monthly Price in AU$.
        price_hourly (float): Hourly price in AU$.
        disk (int): The included storage for this size in GB.
        memory (int): The included memory for this size in MB.
        transfer (float): The included data transfer for this size in TB.
        excess_transfer_cost_per_gigabyte (float): The excess charged for any transfer above the included data transfer
            in AU$ per GB.
        vcpus (int): The count of virtual CPUs for this size. See vcpu_units for a description of how each virtual CPU
            maps to the underlying hardware.
        vcpu_units (str): This is the unit that the vcpus field counts, e.g. "core" or "thread".
        options (SizeOptions): Available add-ons (optional features not included in the base price) for the size. All
            costs are in AU$ per month (pro-rated).
        description (Union[Unset, None, str]): A description of this size.
        cpu_description (Union[Unset, None, str]): A description of the CPU provided in this size.
        storage_description (Union[Unset, None, str]): A description of the storage provided in this size.
        regions_out_of_stock (Union[Unset, None, List[str]]): A list of region slugs where the size is normally
            available but is currently not available due to lack of stock.
    """

    slug: str
    size_type: SizeType
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
    options: SizeOptions
    description: Union[Unset, None, str] = UNSET
    cpu_description: Union[Unset, None, str] = UNSET
    storage_description: Union[Unset, None, str] = UNSET
    regions_out_of_stock: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        slug = self.slug
        size_type = self.size_type.to_dict()

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
        options = self.options.to_dict()

        description = self.description
        cpu_description = self.cpu_description
        storage_description = self.storage_description
        regions_out_of_stock: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.regions_out_of_stock, Unset):
            if self.regions_out_of_stock is None:
                regions_out_of_stock = None
            else:
                regions_out_of_stock = self.regions_out_of_stock

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        if regions_out_of_stock is not UNSET:
            field_dict["regions_out_of_stock"] = regions_out_of_stock

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        slug = d.pop("slug")

        size_type = SizeType.from_dict(d.pop("size_type"))

        available = d.pop("available")

        regions = cast(List[str], d.pop("regions"))

        price_monthly = d.pop("price_monthly")

        price_hourly = d.pop("price_hourly")

        disk = d.pop("disk")

        memory = d.pop("memory")

        transfer = d.pop("transfer")

        excess_transfer_cost_per_gigabyte = d.pop("excess_transfer_cost_per_gigabyte")

        vcpus = d.pop("vcpus")

        vcpu_units = d.pop("vcpu_units")

        options = SizeOptions.from_dict(d.pop("options"))

        description = d.pop("description", UNSET)

        cpu_description = d.pop("cpu_description", UNSET)

        storage_description = d.pop("storage_description", UNSET)

        regions_out_of_stock = cast(List[str], d.pop("regions_out_of_stock", UNSET))

        size = cls(
            slug=slug,
            size_type=size_type,
            available=available,
            regions=regions,
            price_monthly=price_monthly,
            price_hourly=price_hourly,
            disk=disk,
            memory=memory,
            transfer=transfer,
            excess_transfer_cost_per_gigabyte=excess_transfer_cost_per_gigabyte,
            vcpus=vcpus,
            vcpu_units=vcpu_units,
            options=options,
            description=description,
            cpu_description=cpu_description,
            storage_description=storage_description,
            regions_out_of_stock=regions_out_of_stock,
        )

        size.additional_properties = d
        return size

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
