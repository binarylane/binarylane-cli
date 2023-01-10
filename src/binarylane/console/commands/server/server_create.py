from __future__ import annotations

from typing import Any, List, Type, Union

from binarylane.api.server.server_create import sync_detailed
from binarylane.client import Client
from binarylane.models.create_server_request import CreateServerRequest
from binarylane.models.create_server_response import CreateServerResponse
from binarylane.models.license_ import License
from binarylane.models.size_options_request import SizeOptionsRequest
from binarylane.models.ssh_key_request import SshKeyRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.actions import BooleanOptionalAction
from binarylane.console.runners import ActionLinkRunner


class Command(ActionLinkRunner):
    @property
    def name(self):
        return "create"

    @property
    def description(self):
        return """Create a New Server"""

    def configure(self, parser):
        """Add arguments for server_create"""

        parser.cli_argument(
            "--size",
            str,
            dest="size",
            required=True,
            description="""The slug of the selected size.""",
        )

        parser.cli_argument(
            "--image",
            Union[int, str],
            dest="image",
            required=True,
            description="""The slug or id of the selected operating system.""",
        )

        parser.cli_argument(
            "--region",
            str,
            dest="region",
            required=True,
            description="""The slug of the selected region.""",
        )

        parser.cli_argument(
            "--name",
            Union[Unset, None, str],
            dest="name",
            required=False,
            description="""The hostname of your server, such as vps01.yourcompany.com. If not provided, the server will be created with a random name.""",
        )

        parser.cli_argument(
            "--backups",
            Union[Unset, None, bool],
            dest="backups",
            required=False,
            description="""If true this will enable two daily backups for the server. Options.daily_backups will override this value if provided. Setting this to false has no effect.""",
            action=BooleanOptionalAction,
        )

        parser.cli_argument(
            "--ipv6",
            Union[Unset, None, bool],
            dest="ipv6",
            required=False,
            description="""If true this will enable IPv6 for this server.""",
            action=BooleanOptionalAction,
        )

        parser.cli_argument(
            "--vpc-id",
            Union[Unset, None, int],
            dest="vpc_id",
            required=False,
            description="""Leave null to use default (public) network for the selected region.""",
        )

        parser.cli_argument(
            "--ssh-keys",
            Union[Unset, None, List[Union[int, str]]],
            dest="ssh_keys",
            required=False,
            description="""This may be either the SSH keys Ids or fingerprints. If this is null or not provided any SSH keys that have been marked as default will be deployed (if the operating system supports SSH keys). Submit an empty array to disable deployment of default keys.""",
        )

        parser.cli_argument(
            "--new-ssh-key",
            Union[Unset, None, SshKeyRequest],
            dest="new_ssh_key",
            required=False,
            description="""""",
        )

        parser.cli_argument(
            "--options",
            Union[Unset, None, SizeOptionsRequest],
            dest="options",
            required=False,
            description="""""",
        )

        parser.cli_argument(
            "--licenses",
            Union[Unset, None, List[License]],
            dest="licenses",
            required=False,
            description="""None""",
        )

        parser.cli_argument(
            "--user-data",
            Union[Unset, None, str],
            dest="user_data",
            required=False,
            description="""If provided this will be used to initialise the new server. This must be left null if the Image does not support UserData, see DistributionInfo.Features for more information.""",
        )

        parser.cli_argument(
            "--port-blocking",
            Union[Unset, None, bool],
            dest="port_blocking",
            required=False,
            description="""Port blocking of outgoing connections for email, SSH and Remote Desktop (TCP ports 22, 25, and 3389) is enabled by default for all new servers. If this is false port blocking will be disabled. Disabling port blocking is only available to reviewed accounts.""",
            action=BooleanOptionalAction,
        )

    @property
    def ok_response_type(self) -> Type:
        return CreateServerResponse

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

        page_response = sync_detailed(
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
        )
        return page_response.status_code, page_response.parsed
