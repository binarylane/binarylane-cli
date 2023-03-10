from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Dict, List, Tuple, Union

from binarylane.api.servers.get_v2_servers_server_id_advanced_firewall_rules import sync_detailed
from binarylane.models.advanced_firewall_rules_response import AdvancedFirewallRulesResponse
from binarylane.models.problem_details import ProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.list import ListRunner


class CommandRequest:
    server_id: int

    def __init__(self, server_id: int) -> None:
        self.server_id = server_id


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "source_addresses",
            "destination_addresses",
            "protocol",
            "destination_ports",
            "action",
            "description",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "source_addresses": """The source addresses to match for this rule. Each address may be an individual IPv4 address or a range in IPv4 CIDR notation.""",
            "destination_addresses": """The destination addresses to match for this rule. Each address may be an individual IPv4 address or a range in IPv4 CIDR notation.""",
            "protocol": """The protocol to match for this rule.""",
            "action": """The action to take when there is a match on this rule.""",
            "destination_ports": """The destination ports to match for this rule. Leave null or empty to match on all ports.""",
            "description": """A description to assist in identifying this rule. Commonly used to record the reason for the rule or the intent behind it, e.g. "Block access to RDP" or "Allow access from HQ".""",
        }

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """Fetch All Advanced Firewall Rules for a Server"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Servers/paths/~1v2~1servers~1%7Bserver_id%7D~1advanced_firewall_rules/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the server for which firewall rules should be listed.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return AdvancedFirewallRulesResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[AdvancedFirewallRulesResponse, None, ProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: AdvancedFirewallRulesResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=request.server_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
