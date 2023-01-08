from typing import Any, Type, Union

from ...client.api.load_balancer.load_balancer_get import sync_detailed
from ...client.client import Client
from ...client.models.load_balancer_response import LoadBalancerResponse
from ...client.models.problem_details import ProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "get"

    @property
    def description(self):
        return """Fetch an Existing Load Balancer"""

    def configure(self, parser):
        """Add arguments for load-balancer_get"""
        parser.cli_argument(
            "load_balancer_id",
            type=int,
            description="""The ID of the load balancer to fetch.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return LoadBalancerResponse

    def request(
        self,
        load_balancer_id: int,
        client: Client,
    ) -> Union[Any, LoadBalancerResponse, ProblemDetails]:

        page_response = sync_detailed(
            load_balancer_id=load_balancer_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
