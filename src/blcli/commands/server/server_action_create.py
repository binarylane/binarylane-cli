from typing import Any, Union

from ...client.api.server.server_action_create import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_action_create"

    @property
    def description(self):
        return """Perform an Action on a Server"""

    def configure(self, parser):
        """Add arguments for server_action_create"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        # Unknown Union['AddDisk', 'AttachBackup', 'ChangeAdvancedFeatures', 'ChangeAdvancedFirewallRules', 'ChangeBackupSchedule', 'ChangeIpv6', 'ChangeIpv6ReverseNameservers', 'ChangeKernel', 'ChangeManageOffsiteBackupCopies', 'ChangeNetwork', 'ChangeOffsiteBackupLocation', 'ChangePartner', 'ChangePortBlocking', 'ChangeReverseName', 'ChangeSeparatePrivateNetworkInterface', 'ChangeSourceAndDestinationCheck', 'ChangeThresholdAlerts', 'ChangeVpcIpv4', 'CloneUsingBackup', 'DeleteDisk', 'DetachBackup', 'DisableBackups', 'DisableSelinux', 'EnableBackups', 'EnableIpv6', 'IsRunning', 'PasswordReset', 'Ping', 'PowerCycle', 'PowerOff', 'PowerOn', 'Reboot', 'Rebuild', 'Rename', 'Resize', 'ResizeDisk', 'Restore', 'Shutdown', 'TakeBackup', 'Uncancel', 'Uptime'] union_property.py.jinja

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
        ).parsed
