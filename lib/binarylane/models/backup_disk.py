from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="BackupDisk")


@attr.s(auto_attribs=True)
class BackupDisk:
    """
    Attributes:
        id (int): The ID of this backup disk.
        size_gigabytes (float): This is the compressed size of the disk image in GB.
        min_disk_size (int): This is the minimum disk size in GB required to restore this disk image.
        description (Union[Unset, None, str]): A description of this disk.
    """

    id: int
    size_gigabytes: float
    min_disk_size: int
    description: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        size_gigabytes = self.size_gigabytes
        min_disk_size = self.min_disk_size
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "size_gigabytes": size_gigabytes,
                "min_disk_size": min_disk_size,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        size_gigabytes = d.pop("size_gigabytes")

        min_disk_size = d.pop("min_disk_size")

        description = d.pop("description", UNSET)

        backup_disk = cls(
            id=id,
            size_gigabytes=size_gigabytes,
            min_disk_size=min_disk_size,
            description=description,
        )

        backup_disk.additional_properties = d
        return backup_disk

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
