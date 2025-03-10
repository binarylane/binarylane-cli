from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List

from binarylane.models.action_link import ActionLink
from binarylane.models.actions_links import ActionsLinks
from tests.models.create_server_response import CreateServerResponse
from tests.models.network import Network
from tests.models.network_type import NetworkType

from binarylane.console.printers import formatter

if TYPE_CHECKING:
    from tests.models.servers_response import ServersResponse


def test_format_str() -> None:
    assert formatter.format_response("test", True) == [[formatter.DEFAULT_HEADING], ["test"]]
    assert formatter.format_response("test", False) == [["test"]]


def test_format_list() -> None:
    ns1 = "ns1.binarylane.com.au"
    ns2 = "ns2.binarylane.com.au"
    dns = [ns1, ns2]

    assert formatter.format_response(dns, True, ["value"]) == [["value"], [ns1], [ns2]]
    assert formatter.format_response(dns, False, ["value"]) == [[ns1], [ns2]]


def test_format_primary_list() -> None:
    class DnsList:
        dns: List[str]
        meta: Dict[str, Any]
        links: List[str]

        def __init__(self) -> None:
            self.dns = ["ns1.binarylane.com.au", "ns2.binarylane.com.au"]

    response = DnsList()
    assert formatter.format_response(response, True) == [
        [formatter.DEFAULT_HEADING],
        [response.dns[0]],
        [response.dns[1]],
    ]


def test_format_primary_str() -> None:
    class DnsError:
        message: str
        meta: Dict[str, Any]
        links: List[str]

        def __init__(self) -> None:
            self.message = "DNS Error"

    response = DnsError()
    assert formatter.format_response(response, True) == [[formatter.DEFAULT_HEADING], [response.message]]


def test_format_host(servers_response: ServersResponse) -> None:
    servers_response.servers[0].host.display_name = "test01"
    assert formatter.format_response(servers_response, False, ["host"]) == [["test01"]]


def test_format_image(servers_response: ServersResponse) -> None:
    servers_response.servers[0].image.full_name = "KDE Neon"
    assert formatter.format_response(servers_response, False, ["image"]) == [["KDE Neon"]]


def test_format_region(servers_response: ServersResponse) -> None:
    servers_response.servers[0].region.name = "bne"
    assert formatter.format_response(servers_response, False, ["region"]) == [["bne"]]


def test_format_size(servers_response: ServersResponse) -> None:
    servers_response.servers[0].size.slug = "medium"
    assert formatter.format_response(servers_response, False, ["size"]) == [["medium"]]


def test_format_networks_v4_only(servers_response: ServersResponse) -> None:
    servers_response.servers[0].networks.v4 = [
        Network(ip_address="ipv4", type=NetworkType.PUBLIC),
        Network(ip_address="value2", type=NetworkType.PUBLIC),
    ]
    assert formatter.format_response(servers_response, False, ["networks"]) == [["ipv4"]]


def test_format_networks_v4_and_v6(servers_response: ServersResponse) -> None:
    servers_response.servers[0].networks.v4 = [
        Network(ip_address="ipv4", type=NetworkType.PUBLIC),
        Network(ip_address="value2", type=NetworkType.PUBLIC),
    ]
    servers_response.servers[0].networks.v6 = [
        Network(ip_address="ipv6", type=NetworkType.PUBLIC),
        Network(ip_address="value4", type=NetworkType.PUBLIC),
    ]
    assert formatter.format_response(servers_response, False, ["networks"]) == [["ipv4\nipv6"]]


# ActionLinkRunner when used with --async will print the action ID
def test_format_int() -> None:
    assert formatter.format_response(12345, True) == [[formatter.DEFAULT_HEADING], ["12345"]]
    assert formatter.format_response(12345, False) == [["12345"]]


def test_format_action_link(servers_response: ServersResponse) -> None:
    action_link = ActionLink(12345, "create", "https://api.example.com/v2/actions/12345")
    response = CreateServerResponse(servers_response.servers[0], ActionsLinks([action_link]))
    assert formatter.format_response(response, True)[:4] == [
        ["name", "value"],
        ["action_id", "12345"],
        ["id", "1"],
        ["name", "test"],
    ]
