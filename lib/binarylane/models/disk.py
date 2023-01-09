from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="Disk")


@attr.s(auto_attribs=True)
class Disk:
    """
    Attributes:
        id (str): The ID of this disk.
        size_gigabytes (float): If this is a disk on a server this value is the size of the disk in GB. If this is a
            disk in a backup image this value is the compressed size of the disk image in GB.
        primary (bool): A primary disk is treated differently from other disks.
        min_disk_size (Union[Unset, None, int]): This value is only available for disks in a backup image and is the
            minimum disk size in GB required to restore this disk image.
        description (Union[Unset, None, str]): A description of this disk.
    """

    id: str
    size_gigabytes: float
    primary: bool
    min_disk_size: Union[Unset, None, int] = UNSET
    description: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        size_gigabytes = self.size_gigabytes
        primary = self.primary
        min_disk_size = self.min_disk_size
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "size_gigabytes": size_gigabytes,
                "primary": primary,
            }
        )
        if min_disk_size is not UNSET:
            field_dict["min_disk_size"] = min_disk_size
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        size_gigabytes = d.pop("size_gigabytes")

        primary = d.pop("primary")

        min_disk_size = d.pop("min_disk_size", UNSET)

        description = d.pop("description", UNSET)

        disk = cls(
            id=id,
            size_gigabytes=size_gigabytes,
            primary=primary,
            min_disk_size=min_disk_size,
            description=description,
        )

        disk.additional_properties = d
        return disk

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
