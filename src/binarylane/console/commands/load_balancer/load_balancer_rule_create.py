from __future__ import annotations

from http import HTTPStatus
from typing import List, Tuple, Union

from binarylane.api.load_balancer.load_balancer_rule_create import sync_detailed
from binarylane.client import Client
from binarylane.models.forwarding_rule import ForwardingRule
from binarylane.models.forwarding_rules_request import ForwardingRulesRequest
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "create"

    @property
    def description(self) -> str:
        return """Add Forwarding Rules to an Existing Load Balancer"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for load-balancer_rule_create"""
        parser.cli_argument(
            "load_balancer_id",
            int,
            description="""The ID of the load balancer to which forwarding rules should be added.""",
        )

        parser.cli_argument(
            "--forwarding-rules",
            List[ForwardingRule],
            dest="forwarding_rules",
            required=True,
            description="""The rules that control which traffic the load balancer will forward to servers in the pool.""",
        )

    @property
    def ok_response_type(self) -> type:
        return type(None)

    def request(
        self,
        load_balancer_id: int,
        client: Client,
        forwarding_rules: List[ForwardingRule],
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, ValidationProblemDetails]]:

        # HTTPStatus.NO_CONTENT: Any
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            load_balancer_id=load_balancer_id,
            client=client,
            json_body=ForwardingRulesRequest(
                forwarding_rules=forwarding_rules,
            ),
        )
        return page_response.status_code, page_response.parsed
