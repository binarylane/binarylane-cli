from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.change_backup_schedule_type import ChangeBackupScheduleType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="ChangeBackupSchedule")


@attr.s(auto_attribs=True)
class ChangeBackupSchedule:
    """Change the Backup Schedule of a Server

    Attributes:
        type (ChangeBackupScheduleType):
        backup_hour_of_day (Union[Unset, None, int]): Do not provide a value to keep the current setting.
        backup_day_of_week (Union[Unset, None, int]): Sunday is 0, Monday is 1 etc. Do not provide a value to keep the
            current setting.
        backup_day_of_month (Union[Unset, None, int]): Do not provide a value to keep the current setting.
    """

    type: ChangeBackupScheduleType
    backup_hour_of_day: Union[Unset, None, int] = UNSET
    backup_day_of_week: Union[Unset, None, int] = UNSET
    backup_day_of_month: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        backup_hour_of_day = self.backup_hour_of_day
        backup_day_of_week = self.backup_day_of_week
        backup_day_of_month = self.backup_day_of_month

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if backup_hour_of_day is not UNSET:
            field_dict["backup_hour_of_day"] = backup_hour_of_day
        if backup_day_of_week is not UNSET:
            field_dict["backup_day_of_week"] = backup_day_of_week
        if backup_day_of_month is not UNSET:
            field_dict["backup_day_of_month"] = backup_day_of_month

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ChangeBackupScheduleType(d.pop("type"))

        backup_hour_of_day = d.pop("backup_hour_of_day", UNSET)

        backup_day_of_week = d.pop("backup_day_of_week", UNSET)

        backup_day_of_month = d.pop("backup_day_of_month", UNSET)

        change_backup_schedule = cls(
            type=type,
            backup_hour_of_day=backup_hour_of_day,
            backup_day_of_week=backup_day_of_week,
            backup_day_of_month=backup_day_of_month,
        )

        change_backup_schedule.additional_properties = d
        return change_backup_schedule

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
