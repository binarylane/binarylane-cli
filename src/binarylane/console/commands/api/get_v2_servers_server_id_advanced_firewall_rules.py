from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Union

from binarylane.api.servers.get_v2_servers_server_id_advanced_firewall_rules import sync_detailed
from binarylane.models.advanced_firewall_rules_response import AdvancedFirewallRulesResponse
from binarylane.models.problem_details import ProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

import binarylane.console.commands.api.get_v2_servers as api_get_v2_servers
from binarylane.console.parser import Mapping, PrimitiveAttribute
from binarylane.console.runners.list import ListRunner


class CommandRequest:
    server_id: int

    def __init__(self, server_id: int) -> None:
        self.server_id = server_id


class Command(ListRunner):
    def response(self, status_code: int, received: Any) -> None:
        if not isinstance(received, AdvancedFirewallRulesResponse):
            return super().response(status_code, received)

        return self._printer.print(received, self._format)

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
            "protocol": """The protocol to match for this rule.

| Value | Description |
| ----- | ----------- |
| all | This rule will match any protocol. |
| icmp | This rule will match ICMP traffic only. |
| tcp | This rule will match TCP traffic only. |
| udp | This rule will match UDP traffic only. |

""",
            "action": """The action to take when there is a match on this rule.

| Value | Description |
| ----- | ----------- |
| drop | Traffic matching this rule will be dropped. |
| accept | Traffic matching this rule will be accepted. |

""",
            "destination_ports": """The destination ports to match for this rule. Leave null or empty to match on all ports.""",
            "description": """A description to assist in identifying this rule. Commonly used to record the reason for the rule or the intent behind it, e.g. "Block access to RDP" or "Allow access from HQ".""",
        }

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Servers/paths/~1v2~1servers~1%7Bserver_id%7D~1advanced_firewall_rules/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        def lookup_server_id(ref: str) -> Union[None, int]:
            return api_get_v2_servers.Command(self._context).lookup(ref)

        mapping.add(
            PrimitiveAttribute(
                "server_id",
                int,
                required=True,
                option_name=None,
                metavar="server",
                description="""The ID or name of the server for which firewall rules should be listed.""",
                lookup=lookup_server_id,
            )
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
