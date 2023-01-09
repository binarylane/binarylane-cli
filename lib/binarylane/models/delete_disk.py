from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.delete_disk_type import DeleteDiskType

T = TypeVar("T", bound="DeleteDisk")


@attr.s(auto_attribs=True)
class DeleteDisk:
    """Delete an Additional Disk for a Server

    Attributes:
        type (DeleteDiskType):
        disk_id (str): The ID of the existing disk. See server.disks for a list of IDs.
    """

    type: DeleteDiskType
    disk_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        disk_id = self.disk_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "disk_id": disk_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = DeleteDiskType(d.pop("type"))

        disk_id = d.pop("disk_id")

        delete_disk = cls(
            type=type,
            disk_id=disk_id,
        )

        delete_disk.additional_properties = d
        return delete_disk

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
