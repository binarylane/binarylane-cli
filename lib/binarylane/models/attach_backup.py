from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.attach_backup_type import AttachBackupType

T = TypeVar("T", bound="AttachBackup")


@attr.s(auto_attribs=True)
class AttachBackup:
    """Attach a Backup to a Server

    Attributes:
        type (AttachBackupType):
        image (int): Only attaching backup images is currently supported.
    """

    type: AttachBackupType
    image: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        image = self.image

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "image": image,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = AttachBackupType(d.pop("type"))

        image = d.pop("image")

        attach_backup = cls(
            type=type,
            image=image,
        )

        attach_backup.additional_properties = d
        return attach_backup

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
