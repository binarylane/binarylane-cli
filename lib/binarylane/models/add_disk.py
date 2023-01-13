from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.add_disk_type import AddDiskType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="AddDisk")


@attr.s(auto_attribs=True)
class AddDisk:
    """Create an Additional Disk for a Server

    Attributes:
        type (AddDiskType):
        size_gigabytes (int): The size of the new disk in GB. The server must have at least this much unallocated
            storage space.
        description (Union[Unset, None, str]): An optional description for the disk. If this is null a default
            description will be added. Submit an empty string to prevent the default description being added.
    """

    type: AddDiskType
    size_gigabytes: int
    description: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        size_gigabytes = self.size_gigabytes
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "size_gigabytes": size_gigabytes,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = AddDiskType(d.pop("type"))

        size_gigabytes = d.pop("size_gigabytes")

        description = d.pop("description", UNSET)

        add_disk = cls(
            type=type,
            size_gigabytes=size_gigabytes,
            description=description,
        )

        add_disk.additional_properties = d
        return add_disk

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
