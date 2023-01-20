from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.load_balancer.load_balancer_rule_delete import sync_detailed
from binarylane.models.forwarding_rule import ForwardingRule
from binarylane.models.forwarding_rules_request import ForwardingRulesRequest
from binarylane.models.load_balancer_rule_protocol import LoadBalancerRuleProtocol
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import ListAttribute, Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    load_balancer_id: int
    json_body: ForwardingRulesRequest

    def __init__(self, load_balancer_id: int, json_body: ForwardingRulesRequest) -> None:
        self.load_balancer_id = load_balancer_id
        self.json_body = json_body


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "delete"

    @property
    def description(self) -> str:
        return """Remove Forwarding Rules from an Existing Load Balancer"""

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "load_balancer_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the load balancer for which forwarding rules should be removed.""",
        )

        json_body = mapping.add_json_body(ForwardingRulesRequest)

        json_body_forwarding_rule = json_body.add(
            ListAttribute(
                "forwarding_rules",
                ForwardingRule,
                option_name="forwarding-rules",
                description="""The rules that control which traffic the load balancer will forward to servers in the pool.""",
                required=True,
            )
        )

        json_body_forwarding_rule.add_primitive(
            "entry_protocol",
            LoadBalancerRuleProtocol,
            option_name="entry-protocol",
            required=True,
            description="""
| Value | Description |
| ----- | ----------- |
| http | The load balancer will forward HTTP traffic that matches this rule. |
| https | The load balancer will forward HTTPS traffic that matches this rule. |

""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return type(None)

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.NO_CONTENT: Any
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            load_balancer_id=request.load_balancer_id,
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
