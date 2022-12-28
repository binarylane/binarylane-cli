from typing import Union

from ...client.api.vpc.vpc_members import sync
from ...client.client import Client
from ...client.models.resource_type import ResourceType
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
        parser.cli_argument(
            "--page",
            dest="page",
            type=Union[Unset, None, int],
            required=False,
            description="""The selected page. Page numbering starts at 1""",
        )
        parser.cli_argument(
            "--per-page",
            dest="per_page",
            type=Union[Unset, None, int],
            required=False,
            description="""The number of results to show per page.""",
        )

    def request(
        self,
        vpc_id: int,
        client: Client,
        resource_type: Union[Unset, None, ResourceType] = UNSET,
        page: Union[Unset, None, int] = 1,
        per_page: Union[Unset, None, int] = 20,
    ):
        return sync(
            vpc_id=vpc_id,
            client=client,
            resource_type=resource_type,
            page=page,
            per_page=per_page,
        )
