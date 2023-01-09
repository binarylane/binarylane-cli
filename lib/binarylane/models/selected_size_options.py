from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SelectedSizeOptions")


@attr.s(auto_attribs=True)
class SelectedSizeOptions:
    """
    Attributes:
        daily_backups (int): The number of retained daily backups. e.g. if this is '2' we will store two daily backups,
            so each daily backup will be retained for two days before being overwritten.
        weekly_backups (int): The number of retained weekly backups. e.g. if this is '1' we will store one weekly
            backup, so that weekly backup will be retained for one week before being overwritten.
        monthly_backups (int): The number of retained monthly backups. e.g. if this is '3' we will store three monthly
            backups, so each monthly backup will be retained for three months before being overwritten.
        offsite_backups (bool): If this is true any daily, weekly or monthly backups will be duplicated to an off-site
            location.
        ipv4_addresses (int): The total count of IPv4 addresses for this server.
        memory (int): The total memory in MB for this server.
        disk (int): The total storage in GB for this server.
        transfer (float): The total transfer per month in TB for this server.
    """

    daily_backups: int
    weekly_backups: int
    monthly_backups: int
    offsite_backups: bool
    ipv4_addresses: int
    memory: int
    disk: int
    transfer: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        daily_backups = self.daily_backups
        weekly_backups = self.weekly_backups
        monthly_backups = self.monthly_backups
        offsite_backups = self.offsite_backups
        ipv4_addresses = self.ipv4_addresses
        memory = self.memory
        disk = self.disk
        transfer = self.transfer

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "daily_backups": daily_backups,
                "weekly_backups": weekly_backups,
                "monthly_backups": monthly_backups,
                "offsite_backups": offsite_backups,
                "ipv4_addresses": ipv4_addresses,
                "memory": memory,
                "disk": disk,
                "transfer": transfer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        daily_backups = d.pop("daily_backups")

        weekly_backups = d.pop("weekly_backups")

        monthly_backups = d.pop("monthly_backups")

        offsite_backups = d.pop("offsite_backups")

        ipv4_addresses = d.pop("ipv4_addresses")

        memory = d.pop("memory")

        disk = d.pop("disk")

        transfer = d.pop("transfer")

        selected_size_options = cls(
            daily_backups=daily_backups,
            weekly_backups=weekly_backups,
            monthly_backups=monthly_backups,
            offsite_backups=offsite_backups,
            ipv4_addresses=ipv4_addresses,
            memory=memory,
            disk=disk,
            transfer=transfer,
        )

        selected_size_options.additional_properties = d
        return selected_size_options

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
