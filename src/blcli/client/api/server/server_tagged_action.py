from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.actions_response import ActionsResponse
from ...models.add_disk import AddDisk
from ...models.attach_backup import AttachBackup
from ...models.change_advanced_features import ChangeAdvancedFeatures
from ...models.change_advanced_firewall_rules import ChangeAdvancedFirewallRules
from ...models.change_backup_schedule import ChangeBackupSchedule
from ...models.change_ipv_6 import ChangeIpv6
from ...models.change_ipv_6_reverse_nameservers import ChangeIpv6ReverseNameservers
from ...models.change_kernel import ChangeKernel
from ...models.change_manage_offsite_backup_copies import ChangeManageOffsiteBackupCopies
from ...models.change_network import ChangeNetwork
from ...models.change_offsite_backup_location import ChangeOffsiteBackupLocation
from ...models.change_partner import ChangePartner
from ...models.change_port_blocking import ChangePortBlocking
from ...models.change_reverse_name import ChangeReverseName
from ...models.change_separate_private_network_interface import ChangeSeparatePrivateNetworkInterface
from ...models.change_source_and_destination_check import ChangeSourceAndDestinationCheck
from ...models.change_threshold_alerts import ChangeThresholdAlerts
from ...models.change_vpc_ipv_4 import ChangeVpcIpv4
from ...models.clone_using_backup import CloneUsingBackup
from ...models.delete_disk import DeleteDisk
from ...models.detach_backup import DetachBackup
from ...models.disable_backups import DisableBackups
from ...models.disable_selinux import DisableSelinux
from ...models.enable_backups import EnableBackups
from ...models.enable_ipv_6 import EnableIpv6
from ...models.is_running import IsRunning
from ...models.password_reset import PasswordReset
from ...models.ping import Ping
from ...models.power_cycle import PowerCycle
from ...models.power_off import PowerOff
from ...models.power_on import PowerOn
from ...models.problem_details import ProblemDetails
from ...models.reboot import Reboot
from ...models.rebuild import Rebuild
from ...models.rename import Rename
from ...models.resize import Resize
from ...models.resize_disk import ResizeDisk
from ...models.restore import Restore
from ...models.shutdown import Shutdown
from ...models.take_backup import TakeBackup
from ...models.uncancel import Uncancel
from ...models.uptime import Uptime
from ...models.validation_problem_details import ValidationProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: Union[
        "AddDisk",
        "AttachBackup",
        "ChangeAdvancedFeatures",
        "ChangeAdvancedFirewallRules",
        "ChangeBackupSchedule",
        "ChangeIpv6",
        "ChangeIpv6ReverseNameservers",
        "ChangeKernel",
        "ChangeManageOffsiteBackupCopies",
        "ChangeNetwork",
        "ChangeOffsiteBackupLocation",
        "ChangePartner",
        "ChangePortBlocking",
        "ChangeReverseName",
        "ChangeSeparatePrivateNetworkInterface",
        "ChangeSourceAndDestinationCheck",
        "ChangeThresholdAlerts",
        "ChangeVpcIpv4",
        "CloneUsingBackup",
        "DeleteDisk",
        "DetachBackup",
        "DisableBackups",
        "DisableSelinux",
        "EnableBackups",
        "EnableIpv6",
        "IsRunning",
        "PasswordReset",
        "Ping",
        "PowerCycle",
        "PowerOff",
        "PowerOn",
        "Reboot",
        "Rebuild",
        "Rename",
        "Resize",
        "ResizeDisk",
        "Restore",
        "Shutdown",
        "TakeBackup",
        "Uncancel",
        "Uptime",
    ],
    tag_name: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v2/servers/actions".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["tag_name"] = tag_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body: Dict[str, Any]

    if isinstance(json_body, ChangeThresholdAlerts):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, IsRunning):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, Ping):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, Uncancel):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, Uptime):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, AttachBackup):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, ChangeBackupSchedule):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, ChangeManageOffsiteBackupCopies):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, ChangeOffsiteBackupLocation):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, CloneUsingBackup):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, DetachBackup):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, DisableBackups):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, EnableBackups):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, Restore):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, TakeBackup):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, PasswordReset):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, PowerCycle):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, PowerOff):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, PowerOn):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, Reboot):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, Shutdown):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, ChangeAdvancedFeatures):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, ChangeAdvancedFirewallRules):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, ChangeKernel):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, ChangePartner):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, DisableSelinux):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, Rebuild):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, Resize):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, AddDisk):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, ResizeDisk):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, DeleteDisk):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, ChangeIpv6ReverseNameservers):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, ChangeReverseName):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, Rename):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, ChangeIpv6):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, ChangePortBlocking):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, EnableIpv6):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, ChangeNetwork):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, ChangeSeparatePrivateNetworkInterface):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, ChangeSourceAndDestinationCheck):
        json_json_body = json_body.to_dict()

    else:
        json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[ActionsResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = ActionsResponse.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ValidationProblemDetails.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = ProblemDetails.from_dict(response.json())

        return response_422
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[ActionsResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: Union[
        "AddDisk",
        "AttachBackup",
        "ChangeAdvancedFeatures",
        "ChangeAdvancedFirewallRules",
        "ChangeBackupSchedule",
        "ChangeIpv6",
        "ChangeIpv6ReverseNameservers",
        "ChangeKernel",
        "ChangeManageOffsiteBackupCopies",
        "ChangeNetwork",
        "ChangeOffsiteBackupLocation",
        "ChangePartner",
        "ChangePortBlocking",
        "ChangeReverseName",
        "ChangeSeparatePrivateNetworkInterface",
        "ChangeSourceAndDestinationCheck",
        "ChangeThresholdAlerts",
        "ChangeVpcIpv4",
        "CloneUsingBackup",
        "DeleteDisk",
        "DetachBackup",
        "DisableBackups",
        "DisableSelinux",
        "EnableBackups",
        "EnableIpv6",
        "IsRunning",
        "PasswordReset",
        "Ping",
        "PowerCycle",
        "PowerOff",
        "PowerOn",
        "Reboot",
        "Rebuild",
        "Rename",
        "Resize",
        "ResizeDisk",
        "Restore",
        "Shutdown",
        "TakeBackup",
        "Uncancel",
        "Uptime",
    ],
    tag_name: Union[Unset, None, str] = UNSET,
) -> Response[Union[ActionsResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Perform an Action on Servers by Tag

     Tags are not currently supported and this endpoint will not perform an action on any servers.

    Args:
        tag_name (Union[Unset, None, str]):
        json_body (Union['AddDisk', 'AttachBackup', 'ChangeAdvancedFeatures',
            'ChangeAdvancedFirewallRules', 'ChangeBackupSchedule', 'ChangeIpv6',
            'ChangeIpv6ReverseNameservers', 'ChangeKernel', 'ChangeManageOffsiteBackupCopies',
            'ChangeNetwork', 'ChangeOffsiteBackupLocation', 'ChangePartner', 'ChangePortBlocking',
            'ChangeReverseName', 'ChangeSeparatePrivateNetworkInterface',
            'ChangeSourceAndDestinationCheck', 'ChangeThresholdAlerts', 'ChangeVpcIpv4',
            'CloneUsingBackup', 'DeleteDisk', 'DetachBackup', 'DisableBackups', 'DisableSelinux',
            'EnableBackups', 'EnableIpv6', 'IsRunning', 'PasswordReset', 'Ping', 'PowerCycle',
            'PowerOff', 'PowerOn', 'Reboot', 'Rebuild', 'Rename', 'Resize', 'ResizeDisk', 'Restore',
            'Shutdown', 'TakeBackup', 'Uncancel', 'Uptime']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionsResponse, Any, ProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        tag_name=tag_name,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: Union[
        "AddDisk",
        "AttachBackup",
        "ChangeAdvancedFeatures",
        "ChangeAdvancedFirewallRules",
        "ChangeBackupSchedule",
        "ChangeIpv6",
        "ChangeIpv6ReverseNameservers",
        "ChangeKernel",
        "ChangeManageOffsiteBackupCopies",
        "ChangeNetwork",
        "ChangeOffsiteBackupLocation",
        "ChangePartner",
        "ChangePortBlocking",
        "ChangeReverseName",
        "ChangeSeparatePrivateNetworkInterface",
        "ChangeSourceAndDestinationCheck",
        "ChangeThresholdAlerts",
        "ChangeVpcIpv4",
        "CloneUsingBackup",
        "DeleteDisk",
        "DetachBackup",
        "DisableBackups",
        "DisableSelinux",
        "EnableBackups",
        "EnableIpv6",
        "IsRunning",
        "PasswordReset",
        "Ping",
        "PowerCycle",
        "PowerOff",
        "PowerOn",
        "Reboot",
        "Rebuild",
        "Rename",
        "Resize",
        "ResizeDisk",
        "Restore",
        "Shutdown",
        "TakeBackup",
        "Uncancel",
        "Uptime",
    ],
    tag_name: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ActionsResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Perform an Action on Servers by Tag

     Tags are not currently supported and this endpoint will not perform an action on any servers.

    Args:
        tag_name (Union[Unset, None, str]):
        json_body (Union['AddDisk', 'AttachBackup', 'ChangeAdvancedFeatures',
            'ChangeAdvancedFirewallRules', 'ChangeBackupSchedule', 'ChangeIpv6',
            'ChangeIpv6ReverseNameservers', 'ChangeKernel', 'ChangeManageOffsiteBackupCopies',
            'ChangeNetwork', 'ChangeOffsiteBackupLocation', 'ChangePartner', 'ChangePortBlocking',
            'ChangeReverseName', 'ChangeSeparatePrivateNetworkInterface',
            'ChangeSourceAndDestinationCheck', 'ChangeThresholdAlerts', 'ChangeVpcIpv4',
            'CloneUsingBackup', 'DeleteDisk', 'DetachBackup', 'DisableBackups', 'DisableSelinux',
            'EnableBackups', 'EnableIpv6', 'IsRunning', 'PasswordReset', 'Ping', 'PowerCycle',
            'PowerOff', 'PowerOn', 'Reboot', 'Rebuild', 'Rename', 'Resize', 'ResizeDisk', 'Restore',
            'Shutdown', 'TakeBackup', 'Uncancel', 'Uptime']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionsResponse, Any, ProblemDetails, ValidationProblemDetails]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        tag_name=tag_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Union[
        "AddDisk",
        "AttachBackup",
        "ChangeAdvancedFeatures",
        "ChangeAdvancedFirewallRules",
        "ChangeBackupSchedule",
        "ChangeIpv6",
        "ChangeIpv6ReverseNameservers",
        "ChangeKernel",
        "ChangeManageOffsiteBackupCopies",
        "ChangeNetwork",
        "ChangeOffsiteBackupLocation",
        "ChangePartner",
        "ChangePortBlocking",
        "ChangeReverseName",
        "ChangeSeparatePrivateNetworkInterface",
        "ChangeSourceAndDestinationCheck",
        "ChangeThresholdAlerts",
        "ChangeVpcIpv4",
        "CloneUsingBackup",
        "DeleteDisk",
        "DetachBackup",
        "DisableBackups",
        "DisableSelinux",
        "EnableBackups",
        "EnableIpv6",
        "IsRunning",
        "PasswordReset",
        "Ping",
        "PowerCycle",
        "PowerOff",
        "PowerOn",
        "Reboot",
        "Rebuild",
        "Rename",
        "Resize",
        "ResizeDisk",
        "Restore",
        "Shutdown",
        "TakeBackup",
        "Uncancel",
        "Uptime",
    ],
    tag_name: Union[Unset, None, str] = UNSET,
) -> Response[Union[ActionsResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Perform an Action on Servers by Tag

     Tags are not currently supported and this endpoint will not perform an action on any servers.

    Args:
        tag_name (Union[Unset, None, str]):
        json_body (Union['AddDisk', 'AttachBackup', 'ChangeAdvancedFeatures',
            'ChangeAdvancedFirewallRules', 'ChangeBackupSchedule', 'ChangeIpv6',
            'ChangeIpv6ReverseNameservers', 'ChangeKernel', 'ChangeManageOffsiteBackupCopies',
            'ChangeNetwork', 'ChangeOffsiteBackupLocation', 'ChangePartner', 'ChangePortBlocking',
            'ChangeReverseName', 'ChangeSeparatePrivateNetworkInterface',
            'ChangeSourceAndDestinationCheck', 'ChangeThresholdAlerts', 'ChangeVpcIpv4',
            'CloneUsingBackup', 'DeleteDisk', 'DetachBackup', 'DisableBackups', 'DisableSelinux',
            'EnableBackups', 'EnableIpv6', 'IsRunning', 'PasswordReset', 'Ping', 'PowerCycle',
            'PowerOff', 'PowerOn', 'Reboot', 'Rebuild', 'Rename', 'Resize', 'ResizeDisk', 'Restore',
            'Shutdown', 'TakeBackup', 'Uncancel', 'Uptime']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionsResponse, Any, ProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        tag_name=tag_name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: Union[
        "AddDisk",
        "AttachBackup",
        "ChangeAdvancedFeatures",
        "ChangeAdvancedFirewallRules",
        "ChangeBackupSchedule",
        "ChangeIpv6",
        "ChangeIpv6ReverseNameservers",
        "ChangeKernel",
        "ChangeManageOffsiteBackupCopies",
        "ChangeNetwork",
        "ChangeOffsiteBackupLocation",
        "ChangePartner",
        "ChangePortBlocking",
        "ChangeReverseName",
        "ChangeSeparatePrivateNetworkInterface",
        "ChangeSourceAndDestinationCheck",
        "ChangeThresholdAlerts",
        "ChangeVpcIpv4",
        "CloneUsingBackup",
        "DeleteDisk",
        "DetachBackup",
        "DisableBackups",
        "DisableSelinux",
        "EnableBackups",
        "EnableIpv6",
        "IsRunning",
        "PasswordReset",
        "Ping",
        "PowerCycle",
        "PowerOff",
        "PowerOn",
        "Reboot",
        "Rebuild",
        "Rename",
        "Resize",
        "ResizeDisk",
        "Restore",
        "Shutdown",
        "TakeBackup",
        "Uncancel",
        "Uptime",
    ],
    tag_name: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ActionsResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Perform an Action on Servers by Tag

     Tags are not currently supported and this endpoint will not perform an action on any servers.

    Args:
        tag_name (Union[Unset, None, str]):
        json_body (Union['AddDisk', 'AttachBackup', 'ChangeAdvancedFeatures',
            'ChangeAdvancedFirewallRules', 'ChangeBackupSchedule', 'ChangeIpv6',
            'ChangeIpv6ReverseNameservers', 'ChangeKernel', 'ChangeManageOffsiteBackupCopies',
            'ChangeNetwork', 'ChangeOffsiteBackupLocation', 'ChangePartner', 'ChangePortBlocking',
            'ChangeReverseName', 'ChangeSeparatePrivateNetworkInterface',
            'ChangeSourceAndDestinationCheck', 'ChangeThresholdAlerts', 'ChangeVpcIpv4',
            'CloneUsingBackup', 'DeleteDisk', 'DetachBackup', 'DisableBackups', 'DisableSelinux',
            'EnableBackups', 'EnableIpv6', 'IsRunning', 'PasswordReset', 'Ping', 'PowerCycle',
            'PowerOff', 'PowerOn', 'Reboot', 'Rebuild', 'Rename', 'Resize', 'ResizeDisk', 'Restore',
            'Shutdown', 'TakeBackup', 'Uncancel', 'Uptime']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionsResponse, Any, ProblemDetails, ValidationProblemDetails]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            tag_name=tag_name,
        )
    ).parsed
