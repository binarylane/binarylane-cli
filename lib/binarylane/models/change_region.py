from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.change_region_type import ChangeRegionType

T = TypeVar("T", bound="ChangeRegion")


@attr.s(auto_attribs=True)
class ChangeRegion:
    """Change the Region of a Server

    Attributes:
        type (ChangeRegionType):
        region (str): The slug of the selected region.
    """

    type: ChangeRegionType
    region: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        region = self.region

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "region": region,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ChangeRegionType(d.pop("type"))

        region = d.pop("region")

        change_region = cls(
            type=type,
            region=region,
        )

        change_region.additional_properties = d
        return change_region

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
