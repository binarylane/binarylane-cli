from __future__ import annotations

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from binarylane.models.backup_info import BackupInfo
from binarylane.models.distribution_info import DistributionInfo
from binarylane.models.distribution_surcharges import DistributionSurcharges
from binarylane.models.image_status import ImageStatus
from binarylane.models.image_type import ImageType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="Image")


@attr.s(auto_attribs=True)
class Image:
    """
    Attributes:
        id (int): The ID of this image.
        name (str): The name of this image.
        type (ImageType):
            | Value | Description |
            | ----- | ----------- |
            | custom | An image uploaded by a user. |
            | snapshot | A snapshot. Snapshot creation is not currently supported so only distribution images will have this
            value. |
            | backup | A backup of a server. |

        public (bool): A public image is available to all users. A private image is available only to the account that
            created the image.
        regions (List[str]): The slugs of the regions where the image is available for use.
        min_disk_size (int): For a distribution image this is the minimum disk size in GB required to install the
            operating system. For a backup image this is the minimum total disk size in GB required to restore the backup.
        size_gigabytes (float): For a distribution image this is the disk size used in GB by the operating system on
            initial install. For a backup image this is the size of the compressed backup image in GB.
        status (ImageStatus):
            | Value | Description |
            | ----- | ----------- |
            | NEW | The image is new. |
            | available | The image is available for use. |
            | pending | The image is pending and is not yet available for use. |
            | deleted | The image has been deleted and is no longer available for use. |

        distribution_info (DistributionInfo): This object may provide further information about the distribution.
        distribution (Union[Unset, None, str]): If this is an operating system image, this is the name of the
            distribution. If this is a backup image, this is the name of the distribution the server is using.
        full_name (Union[Unset, None, str]): If this is an operating system image, this is the name and version of the
            distribution. If this is a backup image, this is the name and version of the distribution the server is using.
        slug (Union[Unset, None, str]): If this is an operating system image this is a slug which may be used as an
            alternative to the ID as a reference.
        created_at (Union[Unset, None, datetime.datetime]): If this is a backup image this is the date and time in
            ISO8601 format when the image was created.
        description (Union[Unset, None, str]): A description that may provide further details or warnings about the
            image.
        error_message (Union[Unset, None, str]): If the image creation failed this may provide further information.
        min_memory_megabytes (Union[Unset, None, int]): This is minimum memory in MB necessary to support this operating
            system (or the base operating system for a backup image).
        distribution_surcharges (Union[Unset, None, DistributionSurcharges]): If this is not null the use of this image
            may incur surcharges above the base cost of the server. All costs are in AU$.
        backup_info (Union[Unset, None, BackupInfo]): If this image is a backup, this object will provide further
            information.
    """

    id: int
    name: str
    type: ImageType
    public: bool
    regions: List[str]
    min_disk_size: int
    size_gigabytes: float
    status: ImageStatus
    distribution_info: DistributionInfo
    distribution: Union[Unset, None, str] = UNSET
    full_name: Union[Unset, None, str] = UNSET
    slug: Union[Unset, None, str] = UNSET
    created_at: Union[Unset, None, datetime.datetime] = UNSET
    description: Union[Unset, None, str] = UNSET
    error_message: Union[Unset, None, str] = UNSET
    min_memory_megabytes: Union[Unset, None, int] = UNSET
    distribution_surcharges: Union[Unset, None, DistributionSurcharges] = UNSET
    backup_info: Union[Unset, None, BackupInfo] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        type = self.type.value

        public = self.public
        regions = self.regions

        min_disk_size = self.min_disk_size
        size_gigabytes = self.size_gigabytes
        status = self.status.value

        distribution_info = self.distribution_info.to_dict()

        distribution = self.distribution
        full_name = self.full_name
        slug = self.slug
        created_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat() if self.created_at else None

        description = self.description
        error_message = self.error_message
        min_memory_megabytes = self.min_memory_megabytes
        distribution_surcharges: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.distribution_surcharges, Unset):
            distribution_surcharges = self.distribution_surcharges.to_dict() if self.distribution_surcharges else None

        backup_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.backup_info, Unset):
            backup_info = self.backup_info.to_dict() if self.backup_info else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type,
                "public": public,
                "regions": regions,
                "min_disk_size": min_disk_size,
                "size_gigabytes": size_gigabytes,
                "status": status,
                "distribution_info": distribution_info,
            }
        )
        if distribution is not UNSET:
            field_dict["distribution"] = distribution
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if min_memory_megabytes is not UNSET:
            field_dict["min_memory_megabytes"] = min_memory_megabytes
        if distribution_surcharges is not UNSET:
            field_dict["distribution_surcharges"] = distribution_surcharges
        if backup_info is not UNSET:
            field_dict["backup_info"] = backup_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        type = ImageType(d.pop("type"))

        public = d.pop("public")

        regions = cast(List[str], d.pop("regions"))

        min_disk_size = d.pop("min_disk_size")

        size_gigabytes = d.pop("size_gigabytes")

        status = ImageStatus(d.pop("status"))

        distribution_info = DistributionInfo.from_dict(d.pop("distribution_info"))

        distribution = d.pop("distribution", UNSET)

        full_name = d.pop("full_name", UNSET)

        slug = d.pop("slug", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, None, datetime.datetime]
        if _created_at is None:
            created_at = None
        elif isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        description = d.pop("description", UNSET)

        error_message = d.pop("error_message", UNSET)

        min_memory_megabytes = d.pop("min_memory_megabytes", UNSET)

        _distribution_surcharges = d.pop("distribution_surcharges", UNSET)
        distribution_surcharges: Union[Unset, None, DistributionSurcharges]
        if _distribution_surcharges is None:
            distribution_surcharges = None
        elif isinstance(_distribution_surcharges, Unset):
            distribution_surcharges = UNSET
        else:
            distribution_surcharges = DistributionSurcharges.from_dict(_distribution_surcharges)

        _backup_info = d.pop("backup_info", UNSET)
        backup_info: Union[Unset, None, BackupInfo]
        if _backup_info is None:
            backup_info = None
        elif isinstance(_backup_info, Unset):
            backup_info = UNSET
        else:
            backup_info = BackupInfo.from_dict(_backup_info)

        image = cls(
            id=id,
            name=name,
            type=type,
            public=public,
            regions=regions,
            min_disk_size=min_disk_size,
            size_gigabytes=size_gigabytes,
            status=status,
            distribution_info=distribution_info,
            distribution=distribution,
            full_name=full_name,
            slug=slug,
            created_at=created_at,
            description=description,
            error_message=error_message,
            min_memory_megabytes=min_memory_megabytes,
            distribution_surcharges=distribution_surcharges,
            backup_info=backup_info,
        )

        image.additional_properties = d
        return image

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
