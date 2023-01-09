from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.clone_using_backup_type import CloneUsingBackupType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="CloneUsingBackup")


@attr.s(auto_attribs=True)
class CloneUsingBackup:
    """Restore a Backup of a Server to a Different Existing Server

    Attributes:
        type (CloneUsingBackupType):
        image_id (int): The ID of the image to clone. Only backup type images are currently supported. This must be a
            backup of the server ID in the action endpoint URL.
        target_server_id (int): The target server ID. This server's current disks will be wiped and replaced with the
            selected backup image.
        name (Union[Unset, None, str]): The new hostname for the target server. If this is not supplied the target
            server's existing hostname will be used.
    """

    type: CloneUsingBackupType
    image_id: int
    target_server_id: int
    name: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        image_id = self.image_id
        target_server_id = self.target_server_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "image_id": image_id,
                "target_server_id": target_server_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = CloneUsingBackupType(d.pop("type"))

        image_id = d.pop("image_id")

        target_server_id = d.pop("target_server_id")

        name = d.pop("name", UNSET)

        clone_using_backup = cls(
            type=type,
            image_id=image_id,
            target_server_id=target_server_id,
            name=name,
        )

        clone_using_backup.additional_properties = d
        return clone_using_backup

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
