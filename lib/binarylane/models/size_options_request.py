from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="SizeOptionsRequest")


@attr.s(auto_attribs=True)
class SizeOptionsRequest:
    """
    Attributes:
        daily_backups (Union[Unset, None, int]): Leave null to accept the default for the size if this is a new server
            or to keep the current value if this is a resize of an existing server.
        weekly_backups (Union[Unset, None, int]): Leave null to accept the default for the size if this is a new server
            or to keep the current value if this is a resize of an existing server.
        monthly_backups (Union[Unset, None, int]): Leave null to accept the default for the size if this is a new server
            or to keep the current value if this is a resize of an existing server.
        offsite_backups (Union[Unset, None, bool]): Leave null to accept the default for the size if this is a new
            server or to keep the current value if this is a resize of an existing server.
        ipv4_addresses (Union[Unset, None, int]): The total count of IPv4 addresses for this server. If specified this
            is the absolute value, not just the additional IPv4 addresses above what is included in the size. Leave null to
            accept the default for the size if this is a new server or to keep the current value if this is a resize of an
            existing server. Must not exceed the size.ipv4_addresses_max value.
        memory (Union[Unset, None, int]): The total memory in MB for this server.
            If specified this is the absolute value, not just the additional memory above what is included in the size.
            Leave null to accept the default for the size if this is a new server or a resize to a different base size, or
            to keep the current value if this a resize with the same base size but different options.

            Valid values:
            - must be a multiple of 128
            - &gt; 2048MB must be a multiple of 1024
            - &gt; 16384MB must be a multiple of 2048
            - &gt; 24576MB must be a multiple of 4096
        disk (Union[Unset, None, int]): The total storage in GB for this server.
            If specified this is the absolute value, not just the additional storage above what is included in the size.
            Leave null to accept the default for the size if this is a new server or a resize to a different base size, or
            to keep the current value if this a resize with the same base size but different options.

            Valid values for sizes that do not provide a value for options.restricted_storage_values_gb:
            - must be a multiple of 5
            - &gt; 60GB must be a multiple of 10
            - &gt; 200GB must be a multiple of 100
        transfer (Union[Unset, None, float]): The total transfer per month in TB for this server.
            If specified this is the absolute value, not just the additional transfer above what is included in the size.
            Leave null to accept the default for the size if this is a new server or a resize to a different base size, or
            to keep the current value if this a resize with the same base size but different options.

            Valid values (when converted to GB by multiplying the value provided by 1024):
            - must be a multiple of 5GB
            - &gt; 30GB must be a multiple of 10
            - &gt; 200GB must be a multiple of 100
            - &gt; 2000GB must be a multiple of 1000
    """

    daily_backups: Union[Unset, None, int] = UNSET
    weekly_backups: Union[Unset, None, int] = UNSET
    monthly_backups: Union[Unset, None, int] = UNSET
    offsite_backups: Union[Unset, None, bool] = UNSET
    ipv4_addresses: Union[Unset, None, int] = UNSET
    memory: Union[Unset, None, int] = UNSET
    disk: Union[Unset, None, int] = UNSET
    transfer: Union[Unset, None, float] = UNSET
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
        field_dict.update({})
        if daily_backups is not UNSET:
            field_dict["daily_backups"] = daily_backups
        if weekly_backups is not UNSET:
            field_dict["weekly_backups"] = weekly_backups
        if monthly_backups is not UNSET:
            field_dict["monthly_backups"] = monthly_backups
        if offsite_backups is not UNSET:
            field_dict["offsite_backups"] = offsite_backups
        if ipv4_addresses is not UNSET:
            field_dict["ipv4_addresses"] = ipv4_addresses
        if memory is not UNSET:
            field_dict["memory"] = memory
        if disk is not UNSET:
            field_dict["disk"] = disk
        if transfer is not UNSET:
            field_dict["transfer"] = transfer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        daily_backups = d.pop("daily_backups", UNSET)

        weekly_backups = d.pop("weekly_backups", UNSET)

        monthly_backups = d.pop("monthly_backups", UNSET)

        offsite_backups = d.pop("offsite_backups", UNSET)

        ipv4_addresses = d.pop("ipv4_addresses", UNSET)

        memory = d.pop("memory", UNSET)

        disk = d.pop("disk", UNSET)

        transfer = d.pop("transfer", UNSET)

        size_options_request = cls(
            daily_backups=daily_backups,
            weekly_backups=weekly_backups,
            monthly_backups=monthly_backups,
            offsite_backups=offsite_backups,
            ipv4_addresses=ipv4_addresses,
            memory=memory,
            disk=disk,
            transfer=transfer,
        )

        size_options_request.additional_properties = d
        return size_options_request

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
