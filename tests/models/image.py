import datetime
from typing import Any, Dict, List, Union

import attr

from binarylane.types import UNSET, Unset


@attr.s(auto_attribs=True)
class Image:
    id: int
    name: str
    type: str
    public: bool
    regions: List[str]
    min_disk_size: int
    size_gigabytes: float
    status: str
    distribution_info: Dict[str, str]
    distribution: Union[Unset, None, str] = UNSET
    full_name: Union[Unset, None, str] = UNSET
    slug: Union[Unset, None, str] = UNSET
    created_at: Union[Unset, None, datetime.datetime] = UNSET
    description: Union[Unset, None, str] = UNSET
    error_message: Union[Unset, None, str] = UNSET
    min_memory_megabytes: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        type = self.type

        public = self.public
        regions = self.regions

        min_disk_size = self.min_disk_size
        size_gigabytes = self.size_gigabytes
        status = self.status

        distribution_info = self.distribution_info

        distribution = self.distribution
        full_name = self.full_name
        slug = self.slug
        created_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat() if self.created_at else None

        description = self.description
        error_message = self.error_message
        min_memory_megabytes = self.min_memory_megabytes

        field_dict: Dict[str, Any] = {}
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

        return field_dict
