from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.period import Period
from binarylane.models.sample import Sample

T = TypeVar("T", bound="SampleSet")


@attr.s(auto_attribs=True)
class SampleSet:
    """
    Attributes:
        server_id (int): The ID of the server that this sample set refers to.
        period (Period): The period when this sample set was collected.
        average (Sample): The average values of the samples collected during this period.
        maximum_memory_megabytes (float): The maximum memory used in MB at any point during this collection period.
        maximum_storage_gigabytes (float): The maximum storage used in GB at any point during this collection period.
    """

    server_id: int
    period: Period
    average: Sample
    maximum_memory_megabytes: float
    maximum_storage_gigabytes: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server_id = self.server_id
        period = self.period.to_dict()

        average = self.average.to_dict()

        maximum_memory_megabytes = self.maximum_memory_megabytes
        maximum_storage_gigabytes = self.maximum_storage_gigabytes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server_id": server_id,
                "period": period,
                "average": average,
                "maximum_memory_megabytes": maximum_memory_megabytes,
                "maximum_storage_gigabytes": maximum_storage_gigabytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        server_id = d.pop("server_id")

        period = Period.from_dict(d.pop("period"))

        average = Sample.from_dict(d.pop("average"))

        maximum_memory_megabytes = d.pop("maximum_memory_megabytes")

        maximum_storage_gigabytes = d.pop("maximum_storage_gigabytes")

        sample_set = cls(
            server_id=server_id,
            period=period,
            average=average,
            maximum_memory_megabytes=maximum_memory_megabytes,
            maximum_storage_gigabytes=maximum_storage_gigabytes,
        )

        sample_set.additional_properties = d
        return sample_set

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
