from typing import Any, Union

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
        )

    def request(
        self,
        load_balancer_id: int,
        client: Client,
    ) -> Union[Any, LoadBalancerResponse, ProblemDetails]:

        return sync_detailed(
            load_balancer_id=load_balancer_id,
            client=client,
        ).parsed
