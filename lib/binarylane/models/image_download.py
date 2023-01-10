from __future__ import annotations

import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from binarylane.models.image_disk_download import ImageDiskDownload

T = TypeVar("T", bound="ImageDownload")


@attr.s(auto_attribs=True)
class ImageDownload:
    """
    Attributes:
        id (int): The ID of the image this download object refers to.
        expiry (datetime.datetime): The date and time in ISO8601 format that this download URL will expire.
        disks (List[ImageDiskDownload]): A list of objects containing the download URLs for each disk in the image.
    """

    id: int
    expiry: datetime.datetime
    disks: List[ImageDiskDownload]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        expiry = self.expiry.isoformat()

        disks = []
        for disks_item_data in self.disks:
            disks_item = disks_item_data.to_dict()

            disks.append(disks_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "expiry": expiry,
                "disks": disks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        expiry = isoparse(d.pop("expiry"))

        disks = []
        _disks = d.pop("disks")
        for disks_item_data in _disks:
            disks_item = ImageDiskDownload.from_dict(disks_item_data)

            disks.append(disks_item)

        image_download = cls(
            id=id,
            expiry=expiry,
            disks=disks,
        )

        image_download.additional_properties = d
        return image_download

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
