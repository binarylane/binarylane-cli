from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.server_actions.post_v_2_servers_server_id_actions_change_offsite_backup_location import (
    sync_detailed,
)
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_offsite_backup_location import ChangeOffsiteBackupLocation
from binarylane.models.change_offsite_backup_location_type import ChangeOffsiteBackupLocationType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.action import ActionRunner


class CommandRequest:
    server_id: int
    json_body: ChangeOffsiteBackupLocation

    def __init__(self, server_id: int, json_body: ChangeOffsiteBackupLocation) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "change-offsite-backup-location"

    @property
    def description(self) -> str:
        return """Change the Offsite Backup Location of a Server"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/ServerActions/paths/~1v2~1servers~1%7Bserver_id%7D~1actions#ChangeOffsiteBackupLocation/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the server on which the action should be performed.""",
        )

        json_body = mapping.add_json_body(ChangeOffsiteBackupLocation)

        json_body.add_primitive(
            "type",
            ChangeOffsiteBackupLocationType,
            option_name="type",
            required=True,
        )

        json_body.add_primitive(
            "offsite_backup_location",
            Union[Unset, None, str],
            option_name="offsite-backup-location",
            required=False,
            description="""Do not provide or set to null to use the internal offsite backup location, otherwise this must be a valid Amazon S3 bucket address. If this is provided Amazon will charge your S3 account at their standard rate for every backup stored.""",
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
