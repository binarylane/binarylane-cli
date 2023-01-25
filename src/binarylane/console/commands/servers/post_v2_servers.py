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

from binarylane.console.parser import ListAttribute, Mapping, ObjectAttribute
from binarylane.console.runners.actionlink import ActionLinkRunner


class CommandRequest:
    json_body: CreateServerRequest

    def __init__(self, json_body: CreateServerRequest) -> None:
        self.json_body = json_body


class Command(ActionLinkRunner):
    @property
    def name(self) -> str:
        return "create"

    @property
    def description(self) -> str:
        return """Create a New Server"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Servers/paths/~1v2~1servers/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        json_body = mapping.add_json_body(CreateServerRequest)

        json_body.add_primitive(
            "size",
            str,
            option_name="size",
            required=True,
            description="""The slug of the selected size.""",
        )

        json_body.add_primitive(
            "image",
            Union[int, str],
            option_name="image",
            required=True,
            description="""The slug or id of the selected operating system.""",
        )

        json_body.add_primitive(
            "region",
            str,
            option_name="region",
            required=True,
            description="""The slug of the selected region.""",
        )

        json_body.add_primitive(
            "name",
            Union[Unset, None, str],
            option_name="name",
            required=False,
            description="""The hostname of your server, such as vps01.yourcompany.com. If not provided, the server will be created with a random name.""",
        )

        json_body.add_primitive(
            "backups",
            Union[Unset, None, bool],
            option_name="backups",
            required=False,
            description="""If true this will enable two daily backups for the server. Options.daily_backups will override this value if provided. Setting this to false has no effect.""",
        )

        json_body.add_primitive(
            "ipv6",
            Union[Unset, None, bool],
            option_name="ipv6",
            required=False,
            description="""If true this will enable IPv6 for this server.""",
        )

        json_body.add_primitive(
            "vpc_id",
            Union[Unset, None, int],
            option_name="vpc-id",
            required=False,
            description="""Leave null to use default (public) network for the selected region.""",
        )

        json_body.add_primitive(
            "ssh_keys",
            Union[Unset, None, List[Union[int, str]]],
            option_name="ssh-keys",
            required=False,
            description="""This may be either the SSH keys Ids or fingerprints. If this is null or not provided any SSH keys that have been marked as default will be deployed (if the operating system supports SSH keys). Submit an empty array to disable deployment of default keys.""",
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

        json_body_size_options_request.add_primitive(
            "daily_backups",
            Union[Unset, None, int],
            option_name="daily-backups",
            required=False,
            description="""Leave null to accept the default for the size if this is a new server or to keep the current value if this is a resize of an existing server.""",
        )

        json_body_size_options_request.add_primitive(
            "weekly_backups",
            Union[Unset, None, int],
            option_name="weekly-backups",
            required=False,
            description="""Leave null to accept the default for the size if this is a new server or to keep the current value if this is a resize of an existing server.""",
        )

        json_body_size_options_request.add_primitive(
            "monthly_backups",
            Union[Unset, None, int],
            option_name="monthly-backups",
            required=False,
            description="""Leave null to accept the default for the size if this is a new server or to keep the current value if this is a resize of an existing server.""",
        )

        json_body_size_options_request.add_primitive(
            "offsite_backups",
            Union[Unset, None, bool],
            option_name="offsite-backups",
            required=False,
            description="""Leave null to accept the default for the size if this is a new server or to keep the current value if this is a resize of an existing server.""",
        )

        json_body_size_options_request.add_primitive(
            "ipv4_addresses",
            Union[Unset, None, int],
            option_name="ipv4-addresses",
            required=False,
            description="""The total count of IPv4 addresses for this server. If specified this is the absolute value, not just the additional IPv4 addresses above what is included in the size. Leave null to accept the default for the size if this is a new server or to keep the current value if this is a resize of an existing server. Must not exceed the size.ipv4_addresses_max value.""",
        )

        json_body_size_options_request.add_primitive(
            "memory",
            Union[Unset, None, int],
            option_name="memory",
            required=False,
            description="""The total memory in MB for this server.
If specified this is the absolute value, not just the additional memory above what is included in the size.
Leave null to accept the default for the size if this is a new server or a resize to a different base size, or to keep the current value if this a resize with the same base size but different options.

Valid values:
- must be a multiple of 128
- &gt; 2048MB must be a multiple of 1024
- &gt; 16384MB must be a multiple of 2048
- &gt; 24576MB must be a multiple of 4096""",
        )

        json_body_size_options_request.add_primitive(
            "disk",
            Union[Unset, None, int],
            option_name="disk",
            required=False,
            description="""The total storage in GB for this server.
If specified this is the absolute value, not just the additional storage above what is included in the size.
Leave null to accept the default for the size if this is a new server or a resize to a different base size, or to keep the current value if this a resize with the same base size but different options.

Valid values for sizes that do not provide a value for options.restricted_storage_values_gb:
- must be a multiple of 5
- &gt; 60GB must be a multiple of 10
- &gt; 200GB must be a multiple of 100""",
        )

        json_body_size_options_request.add_primitive(
            "transfer",
            Union[Unset, None, float],
            option_name="transfer",
            required=False,
            description="""The total transfer per month in TB for this server.
If specified this is the absolute value, not just the additional transfer above what is included in the size.
Leave null to accept the default for the size if this is a new server or a resize to a different base size, or to keep the current value if this a resize with the same base size but different options.

Valid values (when converted to GB by multiplying the value provided by 1024):
- must be a multiple of 5GB
- &gt; 30GB must be a multiple of 10
- &gt; 200GB must be a multiple of 100
- &gt; 2000GB must be a multiple of 1000""",
        )

        json_body_license_ = json_body.add(
            ListAttribute(
                "licenses",
                License,
                option_name="licenses",
                description="""The desired set of licenses.""",
                required=False,
            )
        )

        json_body_license_.add_primitive(
            "software_id",
            str,
            option_name="software-id",
            required=True,
            description="""The ID of the software to license.""",
        )

        json_body_license_.add_primitive(
            "count",
            int,
            option_name="count",
            required=True,
            description="""The number of licences.""",
        )

        json_body.add_primitive(
            "user_data",
            Union[Unset, None, str],
            option_name="user-data",
            required=False,
            description="""If provided this will be used to initialise the new server. This must be left null if the Image does not support UserData, see DistributionInfo.Features for more information.""",
        )

        json_body.add_primitive(
            "port_blocking",
            Union[Unset, None, bool],
            option_name="port-blocking",
            required=False,
            description="""Port blocking of outgoing connections for email, SSH and Remote Desktop (TCP ports 22, 25, and 3389) is enabled by default for all new servers. If this is false port blocking will be disabled. Disabling port blocking is only available to reviewed accounts.""",
        )

        json_body.add_primitive(
            "password",
            Union[Unset, None, str],
            option_name="password",
            required=False,
            description="""If this is provided the default remote user account's password will be set to this value. If this is null a random password will be generated and emailed to the account email address.""",
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
