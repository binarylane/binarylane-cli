from typing import Any, Union

from ...client.api.server_action.server_action_change_vpc_ipv4 import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.change_vpc_ipv_4 import ChangeVpcIpv4
from ...client.models.change_vpc_ipv_4_type import ChangeVpcIpv4Type
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_change-vpc-ipv4"

    @property
    def description(self):
        return """Change the IPv4 Address for a Server in a VPC"""

    def configure(self, parser):
        """Add arguments for server-action_change-vpc-ipv4"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ChangeVpcIpv4Type,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--current-ipv4-address",
            dest="current_ipv4_address",
            type=str,
            required=True,
            description="""The existing Ipv4 address for the private VPC network adapter you wish to change.""",
        )

        parser.cli_argument(
            "--new-ipv4-address",
            dest="new_ipv4_address",
            type=str,
            required=True,
            description="""The new Ipv4 address for the private VPC network adapter.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeVpcIpv4Type,
        current_ipv4_address: str,
        new_ipv4_address: str,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeVpcIpv4(
                type=type,
                current_ipv4_address=current_ipv4_address,
                new_ipv4_address=new_ipv4_address,
            ),
        ).parsed
