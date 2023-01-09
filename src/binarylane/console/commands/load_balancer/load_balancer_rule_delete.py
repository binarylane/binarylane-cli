from __future__ import annotations

from typing import Any, List, Type, Union

from binarylane.api.load_balancer.load_balancer_rule_delete import sync_detailed
from binarylane.client import Client
from binarylane.models.forwarding_rule import ForwardingRule
from binarylane.models.forwarding_rules_request import ForwardingRulesRequest
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "delete"

    @property
    def description(self):
        return """Remove Forwarding Rules from an Existing Load Balancer"""

    def configure(self, parser):
        """Add arguments for load-balancer_rule_delete"""
        parser.cli_argument(
            "load_balancer_id",
            type=int,
            description="""The ID of the load balancer for which forwarding rules should be removed.""",
        )

        parser.cli_argument(
            "--forwarding-rules",
            dest="forwarding_rules",
            type=List["ForwardingRule"],
            required=True,
            description="""The rules that control which traffic the load balancer will forward to servers in the pool.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return type(None)

    def request(
        self,
        load_balancer_id: int,
        client: Client,
        forwarding_rules: List["ForwardingRule"],
    ) -> Union[Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            load_balancer_id=load_balancer_id,
            client=client,
            json_body=ForwardingRulesRequest(
                forwarding_rules=forwarding_rules,
            ),
        )
        return page_response.status_code, page_response.parsed
