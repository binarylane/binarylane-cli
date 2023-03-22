from __future__ import annotations

import pytest
from _pytest.capture import CaptureFixture

from binarylane.models.meta import Meta
from binarylane.models.route_entry import RouteEntry
from binarylane.models.vpc import Vpc
from tests.runner import TypeRunner

from binarylane.console.commands.api import get_v2_vpcs as vpc_list
from binarylane.console.commands.api import get_v2_vpcs_vpc_id as vpc_get
from binarylane.console.runners.command import CommandRunner
from binarylane.console.runners.list import ListRunner


@pytest.fixture
def vpc() -> Vpc:
    return Vpc(
        id=1,
        name="test",
        ip_range="10.240.0.0/16",
        route_entries=[RouteEntry(router="10.240.1.1", destination="192.168.0.0/24", description="Test Route")],
    )


def test_list_response(vpc: Vpc, capsys: CaptureFixture[str]) -> None:
    runner = TypeRunner[ListRunner](vpc_list.Command)
    response = runner.test.ok_response_type(meta=Meta(total=1), vpcs=[vpc])

    runner.test.process(runner.test.parse(["--output", "json"]))
    runner.test.response(200, response)

    assert capsys.readouterr().out == (
        '{"meta": {"total": 1}, "vpcs": [{"id": 1, "name": "test", "ip_range": "10.240.0.0/16",'
        ' "route_entries": [{"router": "10.240.1.1", "destination": "192.168.0.0/24", "description":'
        ' "Test Route"}]}]}\n'
    )


def test_get_response(vpc: Vpc, capsys: CaptureFixture[str]) -> None:
    runner = TypeRunner[CommandRunner](vpc_get.Command)
    response = runner.test.ok_response_type(vpc=vpc)

    runner.test.process(runner.test.parse(["--output", "json", "1"]))
    runner.test.response(200, response)

    assert capsys.readouterr().out == (
        '{"vpc": {"id": 1, "name": "test", "ip_range": "10.240.0.0/16",'
        ' "route_entries": [{"router": "10.240.1.1", "destination": "192.168.0.0/24", "description":'
        ' "Test Route"}]}}\n'
    )
