from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from binarylane.models.offsite_backup_frequency_cost import OffsiteBackupFrequencyCost
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="SizeOptions")


@attr.s(auto_attribs=True)
class SizeOptions:
    """Available add-ons (optional features not included in the base price) for the size. All costs are per month (pro-
    rated).

        Attributes:
            disk_min (int): The minimum storage in GB permitted on this size.
            disk_max (int): The maximum storage in GB permitted on this size.
            disk_cost_per_additional_gigabyte (float): The additional cost per GB per month for additional storage space.
            memory_max (int): The maximum memory in MB permitted on this size.
            memory_cost_per_additional_megabyte (float): The additional cost per MB per month for additional memory.
            transfer_max (float): The maximum transfer in TB permitted for this size.
            transfer_cost_per_additional_gigabyte (float): The additional cost per GB per month for additional included
                transfer.
            ipv4_addresses_max (int): The maximum number of IPv4 addresses permitted on this size.
            ipv4_addresses_cost_per_address (float): The additional cost per public IPv4 address per month for additional
                IPv4 addresses.
            discount_for_no_public_ipv4 (float): This is the discount (if any) that is applied if no public IPv4 addresses
                are selected.
            daily_backups (int): The number of daily backups included in the base size cost.
            weekly_backups (int): The number of weekly backups included in the base size cost.
            monthly_backups (int): The number of monthly backups included in the base size cost.
            backups_cost_per_backup_per_gigabyte (float): The cost per GB of storage of each selected backup. See the API
                support document for how to calculate the final cost of backups based on the options selected.
            offsite_backups_cost_per_gigabyte (float): The additional cost per GB of storage for enabling offsite backups.
                See the API support document for how to calculate the final cost of backups based on the options selected.
            offsite_backup_frequency_cost (OffsiteBackupFrequencyCost): The additional cost per GB of storage for enabling
                offsite backups based on highest frequency of backups currently enabled. All costs are in AU$.
            restricted_disk_values (Union[Unset, None, List[int]]): If this is null the normal valid values in the
                documentation for SizeOptionsRequest are used, otherwise only these values (in GB) are permitted.
    """

    disk_min: int
    disk_max: int
    disk_cost_per_additional_gigabyte: float
    memory_max: int
    memory_cost_per_additional_megabyte: float
    transfer_max: float
    transfer_cost_per_additional_gigabyte: float
    ipv4_addresses_max: int
    ipv4_addresses_cost_per_address: float
    discount_for_no_public_ipv4: float
    daily_backups: int
    weekly_backups: int
    monthly_backups: int
    backups_cost_per_backup_per_gigabyte: float
    offsite_backups_cost_per_gigabyte: float
    offsite_backup_frequency_cost: OffsiteBackupFrequencyCost
    restricted_disk_values: Union[Unset, None, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        disk_min = self.disk_min
        disk_max = self.disk_max
        disk_cost_per_additional_gigabyte = self.disk_cost_per_additional_gigabyte
        memory_max = self.memory_max
        memory_cost_per_additional_megabyte = self.memory_cost_per_additional_megabyte
        transfer_max = self.transfer_max
        transfer_cost_per_additional_gigabyte = self.transfer_cost_per_additional_gigabyte
        ipv4_addresses_max = self.ipv4_addresses_max
        ipv4_addresses_cost_per_address = self.ipv4_addresses_cost_per_address
        discount_for_no_public_ipv4 = self.discount_for_no_public_ipv4
        daily_backups = self.daily_backups
        weekly_backups = self.weekly_backups
        monthly_backups = self.monthly_backups
        backups_cost_per_backup_per_gigabyte = self.backups_cost_per_backup_per_gigabyte
        offsite_backups_cost_per_gigabyte = self.offsite_backups_cost_per_gigabyte
        offsite_backup_frequency_cost = self.offsite_backup_frequency_cost.to_dict()

        restricted_disk_values: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.restricted_disk_values, Unset):
            if self.restricted_disk_values is None:
                restricted_disk_values = None
            else:
                restricted_disk_values = self.restricted_disk_values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "disk_min": disk_min,
                "disk_max": disk_max,
                "disk_cost_per_additional_gigabyte": disk_cost_per_additional_gigabyte,
                "memory_max": memory_max,
                "memory_cost_per_additional_megabyte": memory_cost_per_additional_megabyte,
                "transfer_max": transfer_max,
                "transfer_cost_per_additional_gigabyte": transfer_cost_per_additional_gigabyte,
                "ipv4_addresses_max": ipv4_addresses_max,
                "ipv4_addresses_cost_per_address": ipv4_addresses_cost_per_address,
                "discount_for_no_public_ipv4": discount_for_no_public_ipv4,
                "daily_backups": daily_backups,
                "weekly_backups": weekly_backups,
                "monthly_backups": monthly_backups,
                "backups_cost_per_backup_per_gigabyte": backups_cost_per_backup_per_gigabyte,
                "offsite_backups_cost_per_gigabyte": offsite_backups_cost_per_gigabyte,
                "offsite_backup_frequency_cost": offsite_backup_frequency_cost,
            }
        )
        if restricted_disk_values is not UNSET:
            field_dict["restricted_disk_values"] = restricted_disk_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        disk_min = d.pop("disk_min")

        disk_max = d.pop("disk_max")

        disk_cost_per_additional_gigabyte = d.pop("disk_cost_per_additional_gigabyte")

        memory_max = d.pop("memory_max")

        memory_cost_per_additional_megabyte = d.pop("memory_cost_per_additional_megabyte")

        transfer_max = d.pop("transfer_max")

        transfer_cost_per_additional_gigabyte = d.pop("transfer_cost_per_additional_gigabyte")

        ipv4_addresses_max = d.pop("ipv4_addresses_max")

        ipv4_addresses_cost_per_address = d.pop("ipv4_addresses_cost_per_address")

        discount_for_no_public_ipv4 = d.pop("discount_for_no_public_ipv4")

        daily_backups = d.pop("daily_backups")

        weekly_backups = d.pop("weekly_backups")

        monthly_backups = d.pop("monthly_backups")

        backups_cost_per_backup_per_gigabyte = d.pop("backups_cost_per_backup_per_gigabyte")

        offsite_backups_cost_per_gigabyte = d.pop("offsite_backups_cost_per_gigabyte")

        offsite_backup_frequency_cost = OffsiteBackupFrequencyCost.from_dict(d.pop("offsite_backup_frequency_cost"))

        restricted_disk_values = cast(List[int], d.pop("restricted_disk_values", UNSET))

        size_options = cls(
            disk_min=disk_min,
            disk_max=disk_max,
            disk_cost_per_additional_gigabyte=disk_cost_per_additional_gigabyte,
            memory_max=memory_max,
            memory_cost_per_additional_megabyte=memory_cost_per_additional_megabyte,
            transfer_max=transfer_max,
            transfer_cost_per_additional_gigabyte=transfer_cost_per_additional_gigabyte,
            ipv4_addresses_max=ipv4_addresses_max,
            ipv4_addresses_cost_per_address=ipv4_addresses_cost_per_address,
            discount_for_no_public_ipv4=discount_for_no_public_ipv4,
            daily_backups=daily_backups,
            weekly_backups=weekly_backups,
            monthly_backups=monthly_backups,
            backups_cost_per_backup_per_gigabyte=backups_cost_per_backup_per_gigabyte,
            offsite_backups_cost_per_gigabyte=offsite_backups_cost_per_gigabyte,
            offsite_backup_frequency_cost=offsite_backup_frequency_cost,
            restricted_disk_values=restricted_disk_values,
        )

        size_options.additional_properties = d
        return size_options

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
