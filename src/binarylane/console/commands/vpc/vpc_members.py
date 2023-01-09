from __future__ import annotations

from typing import Any, Dict, List, Type, Union

from binarylane.api.vpc.vpc_members import sync_detailed
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.resource_type import ResourceType
from binarylane.models.vpc_members_response import VpcMembersResponse
from binarylane.types import UNSET, Unset

from binarylane.console.runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "name",
            "resource_type",
            "resource_id",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "name": """The name of this VPC member.""",
            "resource_type": """
| Value | Description |
| ----- | ----------- |
| server | Server |
| load-balancer | Load Balancer |
| ssh-key | SSH Key |
| vpc | Virtual Private Network |
| image | Backup or Operating System Image |
| registered-domain-name | Registered Domain Name |

""",
            "resource_id": """The resource ID of this VPC member.""",
            "created_at": """The date and time in ISO8601 format of this resource's initial creation.""",
        }

    @property
    def name(self):
        return "members"

    @property
    def description(self):
        return """List All Members of an Existing VPC"""

    def configure(self, parser):
        """Add arguments for vpc_members"""
        parser.cli_argument(
            "vpc_id",
            type=int,
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

    @property
    def ok_response_type(self) -> Type:
        return VpcMembersResponse

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

            status_code = page_response.status_code
            if status_code != 200:
                response = page_response.parsed
                break

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.members += page_response.parsed.members

        return status_code, response
