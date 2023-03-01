from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.backup_disk import BackupDisk
from binarylane.models.backup_slot import BackupSlot

T = TypeVar("T", bound="BackupInfo")


@attr.s(auto_attribs=True)
class BackupInfo:
    """
    Attributes:
        type (BackupSlot):
            | Value | Description |
            | ----- | ----------- |
            | daily | A backup which is scheduled to be taken each day. |
            | weekly | A backup which is scheduled to be taken each week. |
            | monthly | A backup which is scheduled to be taken each month. |
            | temporary | A backup which is created on demand and only retained for a maximum of seven days. |

        server_id (int): The server ID that was used to create this backup.
        offsite (bool): If this is true, an attempt to create an offsite copy was made. This does not mean that the
            offsite copy attempt was successful or that the copy still exists.
        locked (bool): If this is true the backup is locked and cannot be replaced.
        iso (bool): If this is true the backup is an ISO image and cannot be restored. ISO images may only be attached
            for use as a boot disk or an additional disk.
        backup_disks (List[BackupDisk]): A list of the individual disks that make up this backup.
    """

    type: BackupSlot
    server_id: int
    offsite: bool
    locked: bool
    iso: bool
    backup_disks: List[BackupDisk]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        server_id = self.server_id
        offsite = self.offsite
        locked = self.locked
        iso = self.iso
        backup_disks = []
        for backup_disks_item_data in self.backup_disks:
            backup_disks_item = backup_disks_item_data.to_dict()

            backup_disks.append(backup_disks_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "server_id": server_id,
                "offsite": offsite,
                "locked": locked,
                "iso": iso,
                "backup_disks": backup_disks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = BackupSlot(d.pop("type"))

        server_id = d.pop("server_id")

        offsite = d.pop("offsite")

        locked = d.pop("locked")

        iso = d.pop("iso")

        backup_disks = []
        _backup_disks = d.pop("backup_disks")
        for backup_disks_item_data in _backup_disks:
            backup_disks_item = BackupDisk.from_dict(backup_disks_item_data)

            backup_disks.append(backup_disks_item)

        backup_info = cls(
            type=type,
            server_id=server_id,
            offsite=offsite,
            locked=locked,
            iso=iso,
            backup_disks=backup_disks,
        )

        backup_info.additional_properties = d
        return backup_info

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
