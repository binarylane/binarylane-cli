from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.software import Software

T = TypeVar("T", bound="LicensedSoftware")


@attr.s(auto_attribs=True)
class LicensedSoftware:
    """
    Attributes:
        software (Software): The currently licensed software.
        licence_count (int): The current licence count for the software.
    """

    software: Software
    licence_count: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        software = self.software.to_dict()

        licence_count = self.licence_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "software": software,
                "licence_count": licence_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        software = Software.from_dict(d.pop("software"))

        licence_count = d.pop("licence_count")

        licensed_software = cls(
            software=software,
            licence_count=licence_count,
        )

        licensed_software.additional_properties = d
        return licensed_software

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
