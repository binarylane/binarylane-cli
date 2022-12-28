from typing import Any, Union

from ...client.api.server.server_firewall_list import sync_detailed
from ...client.client import Client
from ...client.models.advanced_firewall_rules_response import AdvancedFirewallRulesResponse
from ...client.models.problem_details import ProblemDetails
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_firewall_list"

    @property
    def description(self):
        return """Fetch All Advanced Firewall Rules for a Server"""

    def configure(self, parser):
        """Add arguments for server_firewall_list"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
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
