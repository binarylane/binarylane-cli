from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.change_offsite_backup_location_type import ChangeOffsiteBackupLocationType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="ChangeOffsiteBackupLocation")


@attr.s(auto_attribs=True)
class ChangeOffsiteBackupLocation:
    """Change the Offsite Backup Location of a Server

    Attributes:
        type (ChangeOffsiteBackupLocationType):
        offsite_backup_location (Union[Unset, None, str]): Do not provide or set to null to use the internal offsite
            backup location, otherwise this must be a valid Amazon S3 bucket address. If this is provided Amazon will charge
            your S3 account at their standard rate for every backup stored.
    """

    type: ChangeOffsiteBackupLocationType
    offsite_backup_location: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        offsite_backup_location = self.offsite_backup_location

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if offsite_backup_location is not UNSET:
            field_dict["offsite_backup_location"] = offsite_backup_location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ChangeOffsiteBackupLocationType(d.pop("type"))

        offsite_backup_location = d.pop("offsite_backup_location", UNSET)

        change_offsite_backup_location = cls(
            type=type,
            offsite_backup_location=offsite_backup_location,
        )

        change_offsite_backup_location.additional_properties = d
        return change_offsite_backup_location

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
