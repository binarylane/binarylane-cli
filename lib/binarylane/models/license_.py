from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="License")


@attr.s(auto_attribs=True)
class License:
    """
    Attributes:
        software_id (str): The ID of the software to license.
        count (int): The number of licences.
    """

    software_id: str
    count: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        software_id = self.software_id
        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "software_id": software_id,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        software_id = d.pop("software_id")

        count = d.pop("count")

        license_ = cls(
            software_id=software_id,
            count=count,
        )

        license_.additional_properties = d
        return license_

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
