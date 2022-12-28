from typing import Any, Union

from ...client.api.vpc.vpc_members import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.resource_type import ResourceType
from ...client.models.vpc_members_response import VpcMembersResponse
from ...client.types import UNSET, Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "vpc_members"

    @property
    def description(self):
        return """List All Members of an Existing VPC"""

    def configure(self, parser):
        """Add arguments for vpc_members"""
        parser.cli_argument(
            "vpc_id",
            description="""The target vpc id.""",
        )

        parser.cli_argument(
            "--resource-type",
            dest="resource_type",
            type=Union[Unset, None, ResourceType],
            required=False,
            description="""
| Value | Description |
| ----- | ----------- |
| server | Server |
| load-balancer | Load Balancer |
| ssh-key | SSH Key |
| vpc | Virtual Private Network |
| image | Backup or Operating System Image |
| registered-domain-name | Registered Domain Name |

""",
        )

    def request(
        self,
        vpc_id: int,
        client: Client,
        resource_type: Union[Unset, None, ResourceType] = UNSET,
    ) -> Union[Any, ProblemDetails, VpcMembersResponse]:

        page = 0
        per_page = 25
        has_next = True
        response: VpcMembersResponse = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                vpc_id=vpc_id,
                client=client,
                resource_type=resource_type,
                page=page,
                per_page=per_page,
            )

            if page_response.status_code != 200:
                return page_response.parsed

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.members += page_response.parsed.members

        return response
