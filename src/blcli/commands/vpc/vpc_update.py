from typing import Any, List, Union

from ...client.api.vpc.vpc_update import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.route_entry_request import RouteEntryRequest
from ...client.models.update_vpc_request import UpdateVpcRequest
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.models.vpc_response import VpcResponse
from ...client.types import UNSET, Unset
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "vpc_update"

    @property
    def description(self):
        return """Update an Existing VPC"""

    def configure(self, parser):
        """Add arguments for vpc_update"""
        parser.cli_argument(
            "vpc_id",
            description="""The target vpc id.""",
        )

        parser.cli_argument(
            "--name",
            dest="name",
            type=str,
            required=True,
            description="""A name to help identify this VPC.""",
        )

        parser.cli_argument(
            "--route-entries",
            dest="route_entries",
            type=Union[Unset, None, List["RouteEntryRequest"]],
            required=False,
            description="""The route entries that control how network traffic is directed through the VPC environment.""",
        )

    def request(
        self,
        vpc_id: int,
        client: Client,
        name: str,
        route_entries: Union[Unset, None, List["RouteEntryRequest"]] = UNSET,
    ) -> Union[Any, ProblemDetails, ValidationProblemDetails, VpcResponse]:

        return sync_detailed(
            vpc_id=vpc_id,
            client=client,
            json_body=UpdateVpcRequest(
                name=name,
                route_entries=route_entries,
            ),
        ).parsed
