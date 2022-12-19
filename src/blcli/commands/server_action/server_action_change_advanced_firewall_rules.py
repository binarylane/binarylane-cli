from typing import List

from ...client.api.server_action.server_action_change_advanced_firewall_rules import sync
from ...client.client import Client
from ...client.models.change_advanced_firewall_rules import ChangeAdvancedFirewallRules
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_change-advanced-firewall-rules"

    @property
    def description(self):
        return """Change the Advanced Firewall Rules for a Server"""

    def configure(self, parser):
        """Add arguments for server-action_change-advanced-firewall-rules"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ChangeAdvancedFirewallRulesType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--firewall-rules",
            dest="firewall_rules",
            type=List[AdvancedFirewallRule],
            required=True,
            description="""A list of rules for the server. NB: that any existing rules that are not included will be removed. Submit an empty list to clear all rules.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeAdvancedFirewallRulesType,
        firewall_rules: List[AdvancedFirewallRule],
    ):
        return sync(
            server_id=server_id,
            client=client,
            json_body=ChangeAdvancedFirewallRules(
                type=type,
                firewall_rules=firewall_rules,
            ),
        )
