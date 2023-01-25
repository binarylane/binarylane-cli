from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.offsite_backup_settings import OffsiteBackupSettings
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="BackupSettings")


@attr.s(auto_attribs=True)
class BackupSettings:
    """
    Attributes:
        backup_hour_of_day (int): The hour of the day that backups will be scheduled. This is an approximate value.
        backup_day_of_week (int): If weekly backups are enabled the day of the week that the weekly backup will occur.
            Sunday is day 0.
        backup_day_of_month (int): If monthly backups are enabled the day of the month the monthly backup will occur.
        offsite_backup_settings (Union[Unset, None, OffsiteBackupSettings]): If offsite backups are enabled this details
            how they are stored and managed.
    """

    backup_hour_of_day: int
    backup_day_of_week: int
    backup_day_of_month: int
    offsite_backup_settings: Union[Unset, None, OffsiteBackupSettings] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        backup_hour_of_day = self.backup_hour_of_day
        backup_day_of_week = self.backup_day_of_week
        backup_day_of_month = self.backup_day_of_month
        offsite_backup_settings: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.offsite_backup_settings, Unset):
            offsite_backup_settings = self.offsite_backup_settings.to_dict() if self.offsite_backup_settings else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backup_hour_of_day": backup_hour_of_day,
                "backup_day_of_week": backup_day_of_week,
                "backup_day_of_month": backup_day_of_month,
            }
        )
        if offsite_backup_settings is not UNSET:
            field_dict["offsite_backup_settings"] = offsite_backup_settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        backup_hour_of_day = d.pop("backup_hour_of_day")

        backup_day_of_week = d.pop("backup_day_of_week")

        backup_day_of_month = d.pop("backup_day_of_month")

        _offsite_backup_settings = d.pop("offsite_backup_settings", UNSET)
        offsite_backup_settings: Union[Unset, None, OffsiteBackupSettings]
        if _offsite_backup_settings is None:
            offsite_backup_settings = None
        elif isinstance(_offsite_backup_settings, Unset):
            offsite_backup_settings = UNSET
        else:
            offsite_backup_settings = OffsiteBackupSettings.from_dict(_offsite_backup_settings)

        backup_settings = cls(
            backup_hour_of_day=backup_hour_of_day,
            backup_day_of_week=backup_day_of_week,
            backup_day_of_month=backup_day_of_month,
            offsite_backup_settings=offsite_backup_settings,
        )

        backup_settings.additional_properties = d
        return backup_settings

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
