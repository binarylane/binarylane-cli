from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, List, Tuple, Union

from binarylane.api.server_actions.post_v_2_servers_server_id_actions_resize import sync_detailed
from binarylane.models.action_response import ActionResponse
from binarylane.models.backup_replacement_strategy import BackupReplacementStrategy
from binarylane.models.backup_slot import BackupSlot
from binarylane.models.change_image import ChangeImage
from binarylane.models.change_licenses import ChangeLicenses
from binarylane.models.change_size_options_request import ChangeSizeOptionsRequest
from binarylane.models.image_options import ImageOptions
from binarylane.models.license_ import License
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.resize import Resize
from binarylane.models.resize_type import ResizeType
from binarylane.models.take_backup import TakeBackup
from binarylane.models.take_backup_type import TakeBackupType
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import ListAttribute, Mapping, ObjectAttribute
from binarylane.console.runners.action import ActionRunner


class CommandRequest:
    server_id: int
    json_body: Resize

    def __init__(self, server_id: int, json_body: Resize) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "resize"

    @property
    def description(self) -> str:
        return """Update the Size and Related Options for a Server"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/ServerActions/paths/~1v2~1servers~1%7Bserver_id%7D~1actions#Resize/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the server on which the action should be performed.""",
        )

        json_body = mapping.add_json_body(Resize)

        json_body.add_primitive(
            "type",
            ResizeType,
            option_name="type",
            required=True,
        )

        json_body.add_primitive(
            "size",
            Union[Unset, None, str],
            option_name="size",
            required=False,
            description="""The slug of the selected size. Do not provide to keep the current size.""",
        )

        json_body_change_size_options_request = json_body.add(
            ObjectAttribute(
                "options",
                ChangeSizeOptionsRequest,
                option_name="options",
                required=False,
                description="""If this is null and the server has no selected size options the defaults for the size will be used. If this is null and the server has currently selected size options those will be preserved. If this is provided any option fields that are not included will be removed from the existing server.""",
            )
        )

        json_body_change_size_options_request.add_primitive(
            "daily_backups",
            Union[Unset, None, int],
            option_name="daily-backups",
            required=False,
            description="""Leave null to accept the default for the size if this is a new server or to keep the current value if this is a resize of an existing server.""",
        )

        json_body_change_size_options_request.add_primitive(
            "weekly_backups",
            Union[Unset, None, int],
            option_name="weekly-backups",
            required=False,
            description="""Leave null to accept the default for the size if this is a new server or to keep the current value if this is a resize of an existing server.""",
        )

        json_body_change_size_options_request.add_primitive(
            "monthly_backups",
            Union[Unset, None, int],
            option_name="monthly-backups",
            required=False,
            description="""Leave null to accept the default for the size if this is a new server or to keep the current value if this is a resize of an existing server.""",
        )

        json_body_change_size_options_request.add_primitive(
            "offsite_backups",
            Union[Unset, None, bool],
            option_name="offsite-backups",
            required=False,
            description="""Leave null to accept the default for the size if this is a new server or to keep the current value if this is a resize of an existing server.""",
        )

        json_body_change_size_options_request.add_primitive(
            "ipv4_addresses",
            Union[Unset, None, int],
            option_name="ipv4-addresses",
            required=False,
            description="""The total count of IPv4 addresses for this server. If specified this is the absolute value, not just the additional IPv4 addresses above what is included in the size. Leave null to accept the default for the size if this is a new server or to keep the current value if this is a resize of an existing server. Must not exceed the size.ipv4_addresses_max value.""",
        )

        json_body_change_size_options_request.add_primitive(
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

        json_body_change_size_options_request.add_primitive(
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

        json_body_change_size_options_request.add_primitive(
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

        json_body_change_size_options_request.add_primitive(
            "ipv4_addresses_to_remove",
            Union[Unset, None, List[str]],
            option_name="ipv4-addresses-to-remove",
            required=False,
            description="""If you are reducing the number of IPv4 addresses you must specify which addresses to remove. If you specify more IPv4 addresses to remove than the number of IPv4 addresses being removed the extra IPv4 addresses will be re-provisioned with new addresses.""",
        )

        json_body_change_image = json_body.add(
            ObjectAttribute(
                "change_image",
                ChangeImage,
                option_name="change-image",
                required=False,
                description="""This may be left null to keep the current base image for the server. If this is provided the server disks will be destroyed and the server will be rebuilt from the selected image.""",
            )
        )

        json_body_change_image.add_primitive(
            "image",
            Union[None, Unset, int, str],
            option_name="image",
            required=False,
            description="""The slug or ID of the selected image. What type of image is permitted here varies based on the server action.""",
        )

        json_body_change_image_image_options = json_body_change_image.add(
            ObjectAttribute(
                "options",
                ImageOptions,
                option_name="options",
                required=False,
                description="""Additional options for the server configuration after the image has been changed.""",
            )
        )

        json_body_change_image_image_options.add_primitive(
            "name",
            Union[Unset, None, str],
            option_name="name",
            required=False,
            description="""The hostname for the server. Leave null to accept the auto-generated permalink.""",
        )

        json_body_change_image_image_options.add_primitive(
            "ssh_keys",
            Union[Unset, None, List[Union[int, str]]],
            option_name="ssh-keys",
            required=False,
            description="""This may be either the existing SSH Keys IDs or fingerprints.
If this is null or not provided any SSH keys that have been marked as default will be deployed (if the operating system supports SSH Keys).
Submit an empty array to disable deployment of default keys.""",
        )

        json_body_change_image_image_options.add_primitive(
            "user_data",
            Union[Unset, None, str],
            option_name="user-data",
            required=False,
            description="""If provided this will be used to initialise the new server. This must be left null if the Image does not support UserData, see DistributionInfo.Features for more information.""",
        )

        json_body_change_image_image_options.add_primitive(
            "password",
            Union[Unset, None, str],
            option_name="password",
            required=False,
            description="""If this is provided the default remote user account's password will be set to this value. If this is null a random password will be generated and emailed to the account email address.""",
        )

        json_body_change_licenses = json_body.add(
            ObjectAttribute(
                "change_licenses",
                ChangeLicenses,
                option_name="change-licenses",
                required=False,
                description="""This may be left null to keep the current licenses for the server. If this is provided any licenses that are not included will be removed.""",
            )
        )

        json_body_change_licenses_license_ = json_body_change_licenses.add(
            ListAttribute(
                "licenses",
                License,
                option_name="licenses",
                description="""The desired set of licenses.""",
                required=True,
            )
        )

        json_body_change_licenses_license_.add_primitive(
            "software_id",
            str,
            option_name="software-id",
            required=True,
            description="""The ID of the software to license.""",
        )

        json_body_change_licenses_license_.add_primitive(
            "count",
            int,
            option_name="count",
            required=True,
            description="""The number of licences.""",
        )

        json_body_take_backup = json_body.add(
            ObjectAttribute(
                "pre_action_backup",
                TakeBackup,
                option_name="pre-action-backup",
                required=False,
                description="""Specify this to create a backup before any actions are taken, or leave null to skip.""",
            )
        )

        json_body_take_backup.add_primitive(
            "type",
            TakeBackupType,
            option_name="type",
            required=True,
        )

        json_body_take_backup.add_primitive(
            "replacement_strategy",
            BackupReplacementStrategy,
            option_name="replacement-strategy",
            required=True,
            description="""The strategy for selecting which backup to replace (if any).""",
        )

        json_body_take_backup.add_primitive(
            "backup_type",
            Union[Unset, None, BackupSlot],
            option_name="backup-type",
            required=False,
            description="""If replacement_strategy is anything other than 'specified', this must be provided.""",
        )

        json_body_take_backup.add_primitive(
            "backup_id_to_replace",
            Union[Unset, None, int],
            option_name="backup-id-to-replace",
            required=False,
            description="""If replacement_strategy is 'specified' this property must be set to an existing backup.""",
        )

        json_body_take_backup.add_primitive(
            "label",
            Union[Unset, None, str],
            option_name="label",
            required=False,
            description="""An optional label to identify the backup.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[ActionResponse, None, ProblemDetails, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: ActionResponse
        # HTTPStatus.ACCEPTED: Any
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNPROCESSABLE_ENTITY: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=request.server_id,
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
