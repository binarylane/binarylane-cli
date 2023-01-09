from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="OffsiteBackupFrequencyCost")


@attr.s(auto_attribs=True)
class OffsiteBackupFrequencyCost:
    """All costs are in AU$.

    Attributes:
        daily_per_gigabyte (float): The additional cost per GB per month for enabling daily offsite backups. Only the
            highest value of the daily, weekly and monthly is applied. See the API support document for how to calculate the
            final cost of backups based on the options selected.
        weekly_per_gigabyte (float): The additional cost per GB per month for enabling weekly offsite backups. Only the
            highest value of the daily, weekly and monthly is applied. See the API support document for how to calculate the
            final cost of backups based on the options selected.
        monthly_per_gigabyte (float): The additional cost per GB per month for enabling monthly offsite backups. Only
            the highest value of the daily, weekly and monthly is applied. See the API support document for how to calculate
            the final cost of backups based on the options selected.
    """

    daily_per_gigabyte: float
    weekly_per_gigabyte: float
    monthly_per_gigabyte: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        daily_per_gigabyte = self.daily_per_gigabyte
        weekly_per_gigabyte = self.weekly_per_gigabyte
        monthly_per_gigabyte = self.monthly_per_gigabyte

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "daily_per_gigabyte": daily_per_gigabyte,
                "weekly_per_gigabyte": weekly_per_gigabyte,
                "monthly_per_gigabyte": monthly_per_gigabyte,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        daily_per_gigabyte = d.pop("daily_per_gigabyte")

        weekly_per_gigabyte = d.pop("weekly_per_gigabyte")

        monthly_per_gigabyte = d.pop("monthly_per_gigabyte")

        offsite_backup_frequency_cost = cls(
            daily_per_gigabyte=daily_per_gigabyte,
            weekly_per_gigabyte=weekly_per_gigabyte,
            monthly_per_gigabyte=monthly_per_gigabyte,
        )

        offsite_backup_frequency_cost.additional_properties = d
        return offsite_backup_frequency_cost

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
