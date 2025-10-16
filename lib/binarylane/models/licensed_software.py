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
        incompatible (bool): Software that is incompatible with the server will be automatically removed at the next
            plan change.
            Servers may have incompatible software due to changes made by support. Software is not incompatible merely
            because it is disabled;
            disabled software may be retained by servers that already have it, incompatible software will be removed.
    """

    software: Software
    licence_count: int
    incompatible: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        software = self.software.to_dict()

        licence_count = self.licence_count
        incompatible = self.incompatible

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "software": software,
                "licence_count": licence_count,
                "incompatible": incompatible,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        software = Software.from_dict(d.pop("software"))

        licence_count = d.pop("licence_count")

        incompatible = d.pop("incompatible")

        licensed_software = cls(
            software=software,
            licence_count=licence_count,
            incompatible=incompatible,
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
