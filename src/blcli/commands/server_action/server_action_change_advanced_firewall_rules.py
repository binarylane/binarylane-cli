from typing import Any, List, Union

from ...client.api.server_action.server_action_change_advanced_firewall_rules import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.advanced_firewall_rule import AdvancedFirewallRule
from ...client.models.change_advanced_firewall_rules import ChangeAdvancedFirewallRules
from ...client.models.change_advanced_firewall_rules_type import ChangeAdvancedFirewallRulesType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "change-advanced-firewall-rules"

    @property
    def description(self):
        return """Change the Advanced Firewall Rules for a Server"""

    def configure(self, parser):
        """Add arguments for server-action_change-advanced-firewall-rules"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
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
            type=List["AdvancedFirewallRule"],
            required=True,
            description="""A list of rules for the server. NB: that any existing rules that are not included will be removed. Submit an empty list to clear all rules.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeAdvancedFirewallRulesType,
        firewall_rules: List["AdvancedFirewallRule"],
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeAdvancedFirewallRules(
                type=type,
                firewall_rules=firewall_rules,
            ),
        )
        return page_response.status_code, page_response.parsed
