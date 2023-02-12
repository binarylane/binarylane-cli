from __future__ import annotations

import datetime

import pytest

from tests.models.host import Host
from tests.models.image import Image
from tests.models.meta import Meta
from tests.models.networks import Networks
from tests.models.region import Region
from tests.models.server import Server
from tests.models.server_status import ServerStatus
from tests.models.servers_response import ServersResponse
from tests.models.size import Size


@pytest.fixture
def servers_response() -> ServersResponse:
    host = Host(display_name="hostname")
    region = Region(slug="syd", name="Sydney", sizes=[], available=True, features=[], name_servers=[])
    image = Image(
        id=1,
        name="20.04",
        type="os",
        public=True,
        regions=[],
        min_disk_size=1,
        size_gigabytes=2,
        status="active",
        distribution_info={},
    )
    size = Size(
        slug="size_min",
        size_type="vps",
        available=True,
        regions=[],
        price_monthly=1,
        price_hourly=1,
        disk=20,
        memory=1024,
        transfer=1000,
        excess_transfer_cost_per_gigabyte=0.01,
        vcpus=1,
        vcpu_units="VCPU",
        options={},
    )
    networks = Networks(v4=[], v6=[], port_blocking=False, recent_ddos=False)
    server = Server(
        id=1,
        name="test",
        memory=1024,
        vcpus=1,
        disk=20,
        created_at=datetime.datetime.now(),
        status=ServerStatus.ACTIVE,
        backup_ids=[],
        features=[],
        region=region,
        image=image,
        size_slug="size",
        failover_ips=[],
        host=host,
        password_change_supported=True,
        size=size,
        networks=networks,
    )

    return ServersResponse(meta=Meta(total=1), servers=[server])
