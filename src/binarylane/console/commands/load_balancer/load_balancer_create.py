from __future__ import annotations

from http import HTTPStatus
from typing import List, Tuple, Union

from binarylane.api.load_balancer.load_balancer_create import sync_detailed
from binarylane.client import Client
from binarylane.models.create_load_balancer_request import CreateLoadBalancerRequest
from binarylane.models.create_load_balancer_response import CreateLoadBalancerResponse
from binarylane.models.forwarding_rule import ForwardingRule
from binarylane.models.health_check import HealthCheck
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "create"

    @property
    def description(self) -> str:
        return """Create a New Load Balancer"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for load-balancer_create"""

        parser.cli_argument(
            "--name",
            str,
            dest="name",
            required=True,
            description="""The hostname of the load balancer.""",
        )

        parser.cli_argument(
            "--forwarding-rules",
            Union[Unset, None, List[ForwardingRule]],
            dest="forwarding_rules",
            required=False,
            description="""The rules that control which traffic the load balancer will forward to servers in the pool. Leave null to accept a default "HTTP" only forwarding rule.""",
        )

        parser.cli_argument(
            "--health-check",
            Union[Unset, None, HealthCheck],
            dest="health_check",
            required=False,
            description="""""",
        )

        parser.cli_argument(
            "--server-ids",
            Union[Unset, None, List[int]],
            dest="server_ids",
            required=False,
            description="""A list of server IDs to assign to this load balancer.""",
        )

        parser.cli_argument(
            "--region",
            Union[Unset, None, str],
            dest="region",
            required=False,
            description="""Leave null to create an anycast load balancer.""",
        )

    @property
    def ok_response_type(self) -> type:
        return CreateLoadBalancerResponse

    def request(
        self,
        client: Client,
        name: str,
        forwarding_rules: Union[Unset, None, List[ForwardingRule]] = UNSET,
        health_check: Union[Unset, None, HealthCheck] = UNSET,
        server_ids: Union[Unset, None, List[int]] = UNSET,
        region: Union[Unset, None, str] = UNSET,
    ) -> Tuple[HTTPStatus, Union[None, CreateLoadBalancerResponse, ProblemDetails, ValidationProblemDetails]]:

        # HTTPStatus.OK: CreateLoadBalancerResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.UNPROCESSABLE_ENTITY: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
            json_body=CreateLoadBalancerRequest(
                name=name,
                forwarding_rules=forwarding_rules,
                health_check=health_check,
                server_ids=server_ids,
                region=region,
            ),
        )
        return page_response.status_code, page_response.parsed
