from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.resize_disk_type import ResizeDiskType

T = TypeVar("T", bound="ResizeDisk")


@attr.s(auto_attribs=True)
class ResizeDisk:
    """Alter the Size of an Existing Disk for a Server

    Attributes:
        type (ResizeDiskType):
        disk_id (str): The ID of the existing disk. See server.disks for a list of IDs.
        size_gigabytes (int): The new size of the disk in GB. If increasing the size of the disk the server must have
            sufficient unallocated storage space.
    """

    type: ResizeDiskType
    disk_id: str
    size_gigabytes: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        disk_id = self.disk_id
        size_gigabytes = self.size_gigabytes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "disk_id": disk_id,
                "size_gigabytes": size_gigabytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ResizeDiskType(d.pop("type"))

        disk_id = d.pop("disk_id")

        size_gigabytes = d.pop("size_gigabytes")

        resize_disk = cls(
            type=type,
            disk_id=disk_id,
            size_gigabytes=size_gigabytes,
        )

        resize_disk.additional_properties = d
        return resize_disk

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
