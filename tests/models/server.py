from __future__ import annotations

import datetime
from typing import Any, Dict, List, Union

import attr

from tests.models.host import Host
from tests.models.image import Image
from tests.models.networks import Networks
from tests.models.region import Region
from tests.models.server_status import ServerStatus
from tests.models.size import Size


@attr.s(auto_attribs=True)
class Server:
    id: int
    name: str
    memory: int
    vcpus: int
    disk: int
    created_at: datetime.datetime
    status: ServerStatus
    backup_ids: List[int]
    features: List[str]
    region: Region
    image: Image
    size: Size
    size_slug: str
    networks: Networks
    failover_ips: List[str]
    host: Host
    password_change_supported: bool

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        memory = self.memory
        vcpus = self.vcpus
        disk = self.disk
        created_at = self.created_at.isoformat()

        status = self.status.value

        backup_ids = self.backup_ids

        features = self.features

        region = self.region.to_dict()

        image = self.image.to_dict()

        size = self.size.to_dict()

        size_slug = self.size_slug
        networks = self.networks.to_dict()

        failover_ips = self.failover_ips

        host = self.host.to_dict()

        password_change_supported = self.password_change_supported

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
                "memory": memory,
                "vcpus": vcpus,
                "disk": disk,
                "created_at": created_at,
                "status": status,
                "backup_ids": backup_ids,
                "features": features,
                "region": region,
                "image": image,
                "size": size,
                "size_slug": size_slug,
                "networks": networks,
                "failover_ips": failover_ips,
                "host": host,
                "password_change_supported": password_change_supported,
            }
        )

        return field_dict
