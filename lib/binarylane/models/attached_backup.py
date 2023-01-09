from __future__ import annotations

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="AttachedBackup")


@attr.s(auto_attribs=True)
class AttachedBackup:
    """
    Attributes:
        id (int): The ID of the backup image.
        disk_identifiers (List[str]): A list of the operating specific disk identifiers for the attached backup disks.
        attached_at (Union[Unset, None, datetime.datetime]): The date and time in ISO8601 format when this image was
            attached to the server.
        attachment_expires (Union[Unset, None, datetime.datetime]): The date and time in ISO8601 format when the backup
            will be automatically detached unless it is manually detached earlier.
    """

    id: int
    disk_identifiers: List[str]
    attached_at: Union[Unset, None, datetime.datetime] = UNSET
    attachment_expires: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        disk_identifiers = self.disk_identifiers

        attached_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.attached_at, Unset):
            attached_at = self.attached_at.isoformat() if self.attached_at else None

        attachment_expires: Union[Unset, None, str] = UNSET
        if not isinstance(self.attachment_expires, Unset):
            attachment_expires = self.attachment_expires.isoformat() if self.attachment_expires else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "disk_identifiers": disk_identifiers,
            }
        )
        if attached_at is not UNSET:
            field_dict["attached_at"] = attached_at
        if attachment_expires is not UNSET:
            field_dict["attachment_expires"] = attachment_expires

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        disk_identifiers = cast(List[str], d.pop("disk_identifiers"))

        _attached_at = d.pop("attached_at", UNSET)
        attached_at: Union[Unset, None, datetime.datetime]
        if _attached_at is None:
            attached_at = None
        elif isinstance(_attached_at, Unset):
            attached_at = UNSET
        else:
            attached_at = isoparse(_attached_at)

        _attachment_expires = d.pop("attachment_expires", UNSET)
        attachment_expires: Union[Unset, None, datetime.datetime]
        if _attachment_expires is None:
            attachment_expires = None
        elif isinstance(_attachment_expires, Unset):
            attachment_expires = UNSET
        else:
            attachment_expires = isoparse(_attachment_expires)

        attached_backup = cls(
            id=id,
            disk_identifiers=disk_identifiers,
            attached_at=attached_at,
            attachment_expires=attachment_expires,
        )

        attached_backup.additional_properties = d
        return attached_backup

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
