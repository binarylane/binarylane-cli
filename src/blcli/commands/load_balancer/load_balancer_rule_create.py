from typing import Any, List, Union

from ...client.api.load_balancer.load_balancer_rule_create import sync_detailed
from ...client.client import Client
from ...client.models.forwarding_rule import ForwardingRule
from ...client.models.forwarding_rules_request import ForwardingRulesRequest
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "create"

    @property
    def description(self):
        return """Add Forwarding Rules to an Existing Load Balancer"""

    def configure(self, parser):
        """Add arguments for load-balancer_rule_create"""
        parser.cli_argument(
            "load_balancer_id",
            type=int,
        )

        parser.cli_argument(
            "--forwarding-rules",
            dest="forwarding_rules",
            type=List["ForwardingRule"],
            required=True,
            description="""The rules that control which traffic the load balancer will forward to servers in the pool.""",
        )

    def request(
        self,
        load_balancer_id: int,
        client: Client,
        forwarding_rules: List["ForwardingRule"],
    ) -> Union[Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            load_balancer_id=load_balancer_id,
            client=client,
            json_body=ForwardingRulesRequest(
                forwarding_rules=forwarding_rules,
            ),
        ).parsed
