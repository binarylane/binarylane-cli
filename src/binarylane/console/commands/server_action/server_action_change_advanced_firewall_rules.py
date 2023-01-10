from __future__ import annotations

from typing import Any, List, Type, Union

from binarylane.api.server_action.server_action_change_advanced_firewall_rules import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.advanced_firewall_rule import AdvancedFirewallRule
from binarylane.models.change_advanced_firewall_rules import ChangeAdvancedFirewallRules
from binarylane.models.change_advanced_firewall_rules_type import ChangeAdvancedFirewallRulesType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.runners import ActionRunner


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
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            ChangeAdvancedFirewallRulesType,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--firewall-rules",
            List[AdvancedFirewallRule],
            dest="firewall_rules",
            required=True,
            description="""A list of rules for the server. NB: that any existing rules that are not included will be removed. Submit an empty list to clear all rules.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeAdvancedFirewallRulesType,
        firewall_rules: List[AdvancedFirewallRule],
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
