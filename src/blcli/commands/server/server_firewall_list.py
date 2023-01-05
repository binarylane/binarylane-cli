from typing import Any, Dict, List, Union

from ...client.api.server.server_firewall_list import sync_detailed
from ...client.client import Client
from ...client.models.advanced_firewall_rules_response import AdvancedFirewallRulesResponse
from ...client.models.problem_details import ProblemDetails
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "protocol",
            "action",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "source_addresses": """The source addresses to match for this rule. Each address may be an individual IPv4 address or a range in IPv4 CIDR notation.""",
            "destination_addresses": """The destination addresses to match for this rule. Each address may be an individual IPv4 address or a range in IPv4 CIDR notation.""",
            "protocol": """
| Value | Description |
| ----- | ----------- |
| all | This rule will match any protocol. |
| icmp | This rule will match ICMP traffic only. |
| tcp | This rule will match TCP traffic only. |
| udp | This rule will match UDP traffic only. |

""",
            "action": """
| Value | Description |
| ----- | ----------- |
| drop | Traffic matching this rule will be dropped. |
| accept | Traffic matching this rule will be accepted. |

""",
            "destination_ports": """The destination ports to match for this rule. Leave null or empty to match on all ports.""",
            "description": """A description to assist in identifying this rule. Commonly used to record the reason for the rule or the intent behind it, e.g. "Block access to RDP" or "Allow access from HQ".""",
        }

    @property
    def name(self):
        return "list"

    @property
    def description(self):
        return """Fetch All Advanced Firewall Rules for a Server"""

    def configure(self, parser):
        """Add arguments for server_firewall_list"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server for which firewall rules should be listed.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Union[AdvancedFirewallRulesResponse, Any, ProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
        ).parsed
