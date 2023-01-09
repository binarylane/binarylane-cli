from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.change_manage_offsite_backup_copies_type import ChangeManageOffsiteBackupCopiesType

T = TypeVar("T", bound="ChangeManageOffsiteBackupCopies")


@attr.s(auto_attribs=True)
class ChangeManageOffsiteBackupCopies:
    """Change the Management of Offsite Backup Copies

    Attributes:
        type (ChangeManageOffsiteBackupCopiesType):
        manage_offsite_backup_copies (bool): This only has effect if a custom offsite location is being used: the
            internal offsite backup location always manages copies. If this is true old offsite backups will be removed once
            the replacement upload is complete. If this is false backups must be removed from the Amazon S3 bucket manually.
            Amazon will charge your S3 account at their standard rate for every backup stored.
    """

    type: ChangeManageOffsiteBackupCopiesType
    manage_offsite_backup_copies: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        manage_offsite_backup_copies = self.manage_offsite_backup_copies

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "manage_offsite_backup_copies": manage_offsite_backup_copies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ChangeManageOffsiteBackupCopiesType(d.pop("type"))

        manage_offsite_backup_copies = d.pop("manage_offsite_backup_copies")

        change_manage_offsite_backup_copies = cls(
            type=type,
            manage_offsite_backup_copies=manage_offsite_backup_copies,
        )

        change_manage_offsite_backup_copies.additional_properties = d
        return change_manage_offsite_backup_copies

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
