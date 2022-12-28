from typing import Any, List, Union

from ... import cli
from ...client.api.server.server_create import sync_detailed
from ...client.client import Client
from ...client.models.create_server_request import CreateServerRequest
from ...client.models.create_server_response import CreateServerResponse
from ...client.models.license_ import License
from ...client.models.size_options_request import SizeOptionsRequest
from ...client.models.ssh_key_request import SshKeyRequest
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.types import UNSET, Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_create"

    @property
    def description(self):
        return """Create a New Server"""

    def configure(self, parser):
        """Add arguments for server_create"""

        parser.cli_argument(
            "--size",
            dest="size",
            type=str,
            required=True,
            description="""The slug of the selected size.""",
        )

        parser.cli_argument(
            "--image",
            dest="image",
            type=Union[int, str],
            required=True,
            description="""The slug or id of the selected operating system.""",
        )

        parser.cli_argument(
            "--region",
            dest="region",
            type=str,
            required=True,
            description="""The slug of the selected region.""",
        )

        parser.cli_argument(
            "--name",
            dest="name",
            type=Union[Unset, None, str],
            required=False,
            description="""None""",
        )

        parser.cli_argument(
            "--backups",
            dest="backups",
            type=Union[Unset, None, bool],
            required=False,
            description="""If true this will enable two daily backups for the server. Options.daily_backups will override this value if provided. Setting this to false has no effect.""",
            action=cli.BooleanOptionalAction,
        )

        parser.cli_argument(
            "--ipv6",
            dest="ipv6",
            type=Union[Unset, None, bool],
            required=False,
            description="""If true this will enable IPv6 for this server.""",
            action=cli.BooleanOptionalAction,
        )

        parser.cli_argument(
            "--vpc-id",
            dest="vpc_id",
            type=Union[Unset, None, int],
            required=False,
            description="""Leave null to use default (public) network for the selected region.""",
        )

        parser.cli_argument(
            "--ssh-keys",
            dest="ssh_keys",
            type=Union[Unset, None, List[Union[int, str]]],
            required=False,
            description="""This may be either the SSH keys Ids or fingerprints. If this is null or not provided any SSH keys that have been marked as default will be deployed (if the operating system supports SSH keys). Submit an empty array to disable deployment of default keys.""",
        )

        parser.cli_argument(
            "--new-ssh-key",
            dest="new_ssh_key",
            type=Union[Unset, None, SshKeyRequest],
            required=False,
            description="""""",
        )

        parser.cli_argument(
            "--options",
            dest="options",
            type=Union[Unset, None, SizeOptionsRequest],
            required=False,
            description="""""",
        )

        parser.cli_argument(
            "--licenses",
            dest="licenses",
            type=Union[Unset, None, List[License]],
            required=False,
            description="""None""",
        )

        parser.cli_argument(
            "--user-data",
            dest="user_data",
            type=Union[Unset, None, str],
            required=False,
            description="""If provided this will be used to initialise the new server. This must be left null if the Image does not support UserData, see DistributionInfo.Features for more information.""",
        )

        parser.cli_argument(
            "--port-blocking",
            dest="port_blocking",
            type=Union[Unset, None, bool],
            required=False,
            description="""Port blocking of outgoing connections for email, SSH and Remote Desktop (TCP ports 22, 25, and 3389) is enabled by default for all new servers. If this is false port blocking will be disabled. Disabling port blocking is only available to reviewed accounts.""",
            action=cli.BooleanOptionalAction,
        )

    def request(
        self,
        client: Client,
        size: str,
        image: Union[int, str],
        region: str,
        name: Union[Unset, None, str] = UNSET,
        backups: Union[Unset, None, bool] = UNSET,
        ipv6: Union[Unset, None, bool] = UNSET,
        vpc_id: Union[Unset, None, int] = UNSET,
        ssh_keys: Union[Unset, None, List[Union[int, str]]] = UNSET,
        new_ssh_key: Union[Unset, None, SshKeyRequest] = UNSET,
        options: Union[Unset, None, SizeOptionsRequest] = UNSET,
        licenses: Union[Unset, None, List[License]] = UNSET,
        user_data: Union[Unset, None, str] = UNSET,
        port_blocking: Union[Unset, None, bool] = UNSET,
    ) -> Union[Any, CreateServerResponse, ValidationProblemDetails]:

        return sync_detailed(
            client=client,
            json_body=CreateServerRequest(
                size=size,
                image=image,
                region=region,
                name=name,
                backups=backups,
                ipv6=ipv6,
                vpc_id=vpc_id,
                ssh_keys=ssh_keys,
                new_ssh_key=new_ssh_key,
                options=options,
                licenses=licenses,
                user_data=user_data,
                port_blocking=port_blocking,
            ),
        ).parsed
