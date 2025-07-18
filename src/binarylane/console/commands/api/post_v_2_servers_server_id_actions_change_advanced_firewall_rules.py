from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, List, Tuple, Union

from binarylane.api.server_actions.post_v_2_servers_server_id_actions_change_advanced_firewall_rules import (
    sync_detailed,
)
from binarylane.models.action_response import ActionResponse
from binarylane.models.advanced_firewall_rule_action import AdvancedFirewallRuleAction
from binarylane.models.advanced_firewall_rule_protocol import AdvancedFirewallRuleProtocol
from binarylane.models.advanced_firewall_rule_request import AdvancedFirewallRuleRequest
from binarylane.models.change_advanced_firewall_rules import ChangeAdvancedFirewallRules
from binarylane.models.change_advanced_firewall_rules_type import ChangeAdvancedFirewallRulesType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

import binarylane.console.commands.api.get_v2_servers as api_get_v2_servers
from binarylane.console.parser import ListAttribute, Mapping, PrimitiveAttribute
from binarylane.console.runners.action import ActionRunner


class CommandRequest:
    server_id: int
    json_body: ChangeAdvancedFirewallRules

    def __init__(self, server_id: int, json_body: ChangeAdvancedFirewallRules) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/ServerActions/paths/~1v2~1servers~1%7Bserver_id%7D~1actions#ChangeAdvancedFirewallRules/post"

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
                description="""The ID or name of the server on which the action should be performed.""",
                lookup=lookup_server_id,
            )
        )

        json_body = mapping.add_json_body(ChangeAdvancedFirewallRules)

        json_body.add(
            PrimitiveAttribute(
                "type",
                ChangeAdvancedFirewallRulesType,
                required=True,
                option_name="type",
            )
        )

        json_body_advanced_firewall_rule_request = json_body.add(
            ListAttribute(
                "firewall_rules",
                AdvancedFirewallRuleRequest,
                required=True,
                option_name="firewall-rules",
                description="""A list of rules for the server. NB: that any existing rules that are not included will be removed. Submit an empty list to clear all rules.""",
            )
        )

        json_body_advanced_firewall_rule_request.add(
            PrimitiveAttribute(
                "source_addresses",
                List[str],
                required=True,
                option_name="source-addresses",
                description="""The source addresses to match for this rule. Each address may be an individual IPv4 address or a range in IPv4 CIDR notation.""",
            )
        )

        json_body_advanced_firewall_rule_request.add(
            PrimitiveAttribute(
                "destination_addresses",
                List[str],
                required=True,
                option_name="destination-addresses",
                description="""The destination addresses to match for this rule. Each address may be an individual IPv4 address or a range in IPv4 CIDR notation.""",
            )
        )

        json_body_advanced_firewall_rule_request.add(
            PrimitiveAttribute(
                "protocol",
                AdvancedFirewallRuleProtocol,
                required=True,
                option_name="protocol",
                description="""The protocol to match for this rule.

| Value | Description |
| ----- | ----------- |
| all | This rule will match any protocol. |
| icmp | This rule will match ICMP traffic only. |
| tcp | This rule will match TCP traffic only. |
| udp | This rule will match UDP traffic only. |

""",
            )
        )

        json_body_advanced_firewall_rule_request.add(
            PrimitiveAttribute(
                "action",
                AdvancedFirewallRuleAction,
                required=True,
                option_name="action",
                description="""The action to take when there is a match on this rule.

| Value | Description |
| ----- | ----------- |
| drop | Traffic matching this rule will be dropped. |
| accept | Traffic matching this rule will be accepted. |

""",
            )
        )

        json_body_advanced_firewall_rule_request.add(
            PrimitiveAttribute(
                "destination_ports",
                Union[Unset, None, List[str]],
                required=False,
                option_name="destination-ports",
                description="""The destination ports to match for this rule. Leave null or empty to match on all ports.""",
            )
        )

        json_body_advanced_firewall_rule_request.add(
            PrimitiveAttribute(
                "description",
                Union[Unset, None, str],
                required=False,
                option_name="description",
                description="""A description to assist in identifying this rule. Commonly used to record the reason for the rule or the intent behind it, e.g. "Block access to RDP" or "Allow access from HQ".""",
            )
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[ActionResponse, None, ProblemDetails, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: ActionResponse
        # HTTPStatus.ACCEPTED: Any
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=request.server_id,
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
