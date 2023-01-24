from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, List, Tuple, Union

from binarylane.api.load_balancers.post_v2_load_balancers import sync_detailed
from binarylane.models.create_load_balancer_request import CreateLoadBalancerRequest
from binarylane.models.create_load_balancer_response import CreateLoadBalancerResponse
from binarylane.models.forwarding_rule import ForwardingRule
from binarylane.models.health_check import HealthCheck
from binarylane.models.health_check_protocol import HealthCheckProtocol
from binarylane.models.load_balancer_rule_protocol import LoadBalancerRuleProtocol
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import ListAttribute, Mapping, ObjectAttribute
from binarylane.console.runners.actionlink import ActionLinkRunner


class CommandRequest:
    json_body: CreateLoadBalancerRequest

    def __init__(self, json_body: CreateLoadBalancerRequest) -> None:
        self.json_body = json_body


class Command(ActionLinkRunner):
    @property
    def name(self) -> str:
        return "create"

    @property
    def description(self) -> str:
        return """Create a New Load Balancer"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/LoadBalancers/paths/~1v2~1load_balancers/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        json_body = mapping.add_json_body(CreateLoadBalancerRequest)

        json_body.add_primitive(
            "name",
            str,
            option_name="name",
            required=True,
            description="""The hostname of the load balancer.""",
        )

        json_body_forwarding_rule = json_body.add(
            ListAttribute(
                "forwarding_rules",
                ForwardingRule,
                option_name="forwarding-rules",
                description="""The rules that control which traffic the load balancer will forward to servers in the pool. Leave null to accept a default "HTTP" only forwarding rule.""",
                required=False,
            )
        )

        json_body_forwarding_rule.add_primitive(
            "entry_protocol",
            LoadBalancerRuleProtocol,
            option_name="entry-protocol",
            required=True,
            description="""The protocol that traffic must match for this load balancer to forward traffic according to this rule.""",
        )

        json_body_health_check = json_body.add(
            ObjectAttribute(
                "health_check",
                HealthCheck,
                option_name="health-check",
                required=False,
                description="""The rules that determine which servers are considered 'healthy' and in the server pool for the load balancer. Leave this null to accept appropriate defaults based on the forwarding_rules.""",
            )
        )

        json_body_health_check.add_primitive(
            "protocol",
            Union[Unset, None, HealthCheckProtocol],
            option_name="protocol",
            required=False,
            description="""Leave null to accept the default HTTP protocol.""",
        )

        json_body_health_check.add_primitive(
            "path",
            Union[Unset, None, str],
            option_name="path",
            required=False,
            description="""Leave null to accept the default '/' path.""",
        )

        json_body.add_primitive(
            "server_ids",
            Union[Unset, None, List[int]],
            option_name="server-ids",
            required=False,
            description="""A list of server IDs to assign to this load balancer.""",
        )

        json_body.add_primitive(
            "region",
            Union[Unset, None, str],
            option_name="region",
            required=False,
            description="""Leave null to create an anycast load balancer.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return CreateLoadBalancerResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, CreateLoadBalancerResponse, ProblemDetails, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: CreateLoadBalancerResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.UNPROCESSABLE_ENTITY: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
