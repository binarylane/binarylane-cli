from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.data_usage import DataUsage

T = TypeVar("T", bound="DataUsageResponse")


@attr.s(auto_attribs=True)
class DataUsageResponse:
    """
    Attributes:
        data_usage (DataUsage):
    """

    data_usage: DataUsage
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_usage = self.data_usage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_usage": data_usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data_usage = DataUsage.from_dict(d.pop("data_usage"))

        data_usage_response = cls(
            data_usage=data_usage,
        )

        data_usage_response.additional_properties = d
        return data_usage_response

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
