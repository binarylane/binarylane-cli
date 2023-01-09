from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ImageDiskDownload")


@attr.s(auto_attribs=True)
class ImageDiskDownload:
    """
    Attributes:
        id (str): The ID of the disk that this download URL refers to.
        compressed_url (str): The URL of the compressed disk image. It is always preferable to download the compressed
            disk image if at all possible.
        raw_url (str): The URL of the raw (uncompressed) disk image.
    """

    id: str
    compressed_url: str
    raw_url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        compressed_url = self.compressed_url
        raw_url = self.raw_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "compressed_url": compressed_url,
                "raw_url": raw_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        compressed_url = d.pop("compressed_url")

        raw_url = d.pop("raw_url")

        image_disk_download = cls(
            id=id,
            compressed_url=compressed_url,
            raw_url=raw_url,
        )

        image_disk_download.additional_properties = d
        return image_disk_download

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
