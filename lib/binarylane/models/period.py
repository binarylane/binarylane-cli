from __future__ import annotations

import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from binarylane.models.data_interval import DataInterval

T = TypeVar("T", bound="Period")


@attr.s(auto_attribs=True)
class Period:
    """
    Attributes:
        start (datetime.datetime): The date and time of the start of the period in ISO8601 format.
        end (datetime.datetime): The date and time of the end of the period in ISO8601 format.
        data_interval (DataInterval): The duration between data points. This is not the collection interval.

            | Value | Description |
            | ----- | ----------- |
            | five-minute | 5 Minutes |
            | half-hour | 30 Minutes |
            | four-hour | 4 Hours |
            | day | 1 Day |
            | week | 7 Days |
            | month | 1 Month |

    """

    start: datetime.datetime
    end: datetime.datetime
    data_interval: DataInterval
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start = self.start.isoformat()

        end = self.end.isoformat()

        data_interval = self.data_interval.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "end": end,
                "data_interval": data_interval,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start = isoparse(d.pop("start"))

        end = isoparse(d.pop("end"))

        data_interval = DataInterval(d.pop("data_interval"))

        period = cls(
            start=start,
            end=end,
            data_interval=data_interval,
        )

        period.additional_properties = d
        return period

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
