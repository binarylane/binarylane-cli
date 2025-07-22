from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, List, Tuple, Union

from binarylane.api.servers.post_v2_servers import sync_detailed
from binarylane.models.create_server_request import CreateServerRequest
from binarylane.models.create_server_response import CreateServerResponse
from binarylane.models.license_ import License
from binarylane.models.size_options_request import SizeOptionsRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

import binarylane.console.commands.api.get_v2_vpcs as api_get_v2_vpcs
from binarylane.console.parser import ListAttribute, Mapping, ObjectAttribute, PrimitiveAttribute
from binarylane.console.runners.actionlink import ActionLinkRunner


class CommandRequest:
    json_body: CreateServerRequest

    def __init__(self, json_body: CreateServerRequest) -> None:
        self.json_body = json_body


class Command(ActionLinkRunner):
    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Servers/paths/~1v2~1servers/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        json_body = mapping.add_json_body(CreateServerRequest)

        json_body.add(
            PrimitiveAttribute(
                "size",
                str,
                required=True,
                option_name="size",
                description="""The slug of the selected size.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "image",
                Union[int, str],
                required=True,
                option_name="image",
                description="""The slug or id of the selected operating system.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "region",
                str,
                required=True,
                option_name="region",
                description="""The slug of the selected region.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "name",
                Union[Unset, None, str],
                required=False,
                option_name="name",
                description="""The hostname of your server, such as vps01.yourcompany.com. If not provided, the server will be created with a random name.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "backups",
                Union[Unset, None, bool],
                required=False,
                option_name="backups",
                description="""If true this will enable two daily backups for the server. Options.daily_backups will override this value if provided. Setting this to false has no effect.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "ipv6",
                Union[Unset, None, bool],
                required=False,
                option_name="ipv6",
                description="""If true this will enable IPv6 for this server.""",
            )
        )

        def lookup_vpc_id(ref: str) -> Union[None, int]:
            return api_get_v2_vpcs.Command(self._context).lookup(ref)

        json_body.add(
            PrimitiveAttribute(
                "vpc_id",
                Union[Unset, None, int],
                required=False,
                option_name=("vpc", "vpc-id"),
                metavar="vpc",
                description="""Leave null to use default (public) network for the selected region.""",
                lookup=lookup_vpc_id,
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "ssh_keys",
                Union[Unset, None, List[Union[int, str]]],
                required=False,
                option_name="ssh-keys",
                description="""This may be either the SSH keys Ids or fingerprints. If this is null or not provided any SSH keys that have been marked as default will be deployed (if the operating system supports SSH keys). Submit an empty array to disable deployment of default keys.""",
            )
        )

        json_body_size_options_request = json_body.add(
            ObjectAttribute(
                "options",
                SizeOptionsRequest,
                option_name="options",
                required=False,
                description="""This may be left null to accept all of the defaults for the selected size.""",
            )
        )

        json_body_size_options_request.add(
            PrimitiveAttribute(
                "daily_backups",
                Union[Unset, None, int],
                required=False,
                option_name="daily-backups",
                description="""Leave null to accept the default for the size if this is a new server or to keep the current value if this is a resize of an existing server.""",
            )
        )

        json_body_size_options_request.add(
            PrimitiveAttribute(
                "weekly_backups",
                Union[Unset, None, int],
                required=False,
                option_name="weekly-backups",
                description="""Leave null to accept the default for the size if this is a new server or to keep the current value if this is a resize of an existing server.""",
            )
        )

        json_body_size_options_request.add(
            PrimitiveAttribute(
                "monthly_backups",
                Union[Unset, None, int],
                required=False,
                option_name="monthly-backups",
                description="""Leave null to accept the default for the size if this is a new server or to keep the current value if this is a resize of an existing server.""",
            )
        )

        json_body_size_options_request.add(
            PrimitiveAttribute(
                "offsite_backups",
                Union[Unset, None, bool],
                required=False,
                option_name="offsite-backups",
                description="""Leave null to accept the default for the size if this is a new server or to keep the current value if this is a resize of an existing server.""",
            )
        )

        json_body_size_options_request.add(
            PrimitiveAttribute(
                "ipv4_addresses",
                Union[Unset, None, int],
                required=False,
                option_name="ipv4-addresses",
                description="""The total count of IPv4 addresses for this server. If specified this is the absolute value, not just the additional IPv4 addresses above what is included in the size. Leave null to accept the default for the size if this is a new server or to keep the current value if this is a resize of an existing server. Must not exceed the size.ipv4_addresses_max value.""",
            )
        )

        json_body_size_options_request.add(
            PrimitiveAttribute(
                "memory",
                Union[Unset, None, int],
                required=False,
                option_name="memory",
                description="""The total memory in MB for this server.
If specified this is the absolute value, not just the additional memory above what is included in the size.
Leave null to accept the default for the size if this is a new server or a resize to a different base size, or to keep the current value if this a resize with the same base size but different options.

Valid values:
- must be a multiple of 128
- &gt; 2048MB must be a multiple of 1024
- &gt; 16384MB must be a multiple of 2048
- &gt; 24576MB must be a multiple of 4096""",
            )
        )

        json_body_size_options_request.add(
            PrimitiveAttribute(
                "disk",
                Union[Unset, None, int],
                required=False,
                option_name="disk",
                description="""The total storage in GB for this server.
If specified this is the absolute value, not just the additional storage above what is included in the size.
Leave null to accept the default for the size if this is a new server or a resize to a different base size, or to keep the current value if this a resize with the same base size but different options.

Valid values for sizes that do not provide a value for options.restricted_storage_values_gb:
- must be a multiple of 5
- &gt; 60GB must be a multiple of 10
- &gt; 200GB must be a multiple of 100""",
            )
        )

        json_body_size_options_request.add(
            PrimitiveAttribute(
                "transfer",
                Union[Unset, None, float],
                required=False,
                option_name="transfer",
                description="""The total transfer per month in TB for this server.
If specified this is the absolute value, not just the additional transfer above what is included in the size.
Leave null to accept the default for the size if this is a new server or a resize to a different base size, or to keep the current value if this a resize with the same base size but different options.

Valid values (when converted to GB by multiplying the value provided by 1024):
- must be a multiple of 5GB
- &gt; 30GB must be a multiple of 10
- &gt; 200GB must be a multiple of 100
- &gt; 2000GB must be a multiple of 1000""",
            )
        )

        json_body_license_ = json_body.add(
            ListAttribute(
                "licenses",
                License,
                required=False,
                option_name="licenses",
                description="""The desired set of licenses.""",
            )
        )

        json_body_license_.add(
            PrimitiveAttribute(
                "software_id",
                int,
                required=True,
                option_name="software-id",
                description="""The ID of the software to license.""",
            )
        )

        json_body_license_.add(
            PrimitiveAttribute(
                "count",
                int,
                required=True,
                option_name="count",
                description="""The number of licences.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "user_data",
                Union[Unset, None, str],
                required=False,
                option_name="user-data",
                description="""If provided this will be used to initialise the new server. This must be left null if the Image does not support UserData, see DistributionInfo.Features for more information.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "port_blocking",
                Union[Unset, None, bool],
                required=False,
                option_name="port-blocking",
                description="""Port blocking of outgoing connections for email, SSH and Remote Desktop (TCP ports 22, 25, and 3389) is enabled by default for all new servers. If this is false port blocking will be disabled. Disabling port blocking is only available to reviewed accounts.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "password",
                Union[Unset, None, str],
                required=False,
                option_name="password",
                description="""If this is provided the default remote user account's password will be set to this value. If this is null a random password will be generated and emailed to the account email address.""",
            )
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return CreateServerResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, CreateServerResponse, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: CreateServerResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
