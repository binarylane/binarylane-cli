from __future__ import annotations

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from binarylane import errors
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.disable_backups import DisableBackups
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Response


def _get_kwargs(
    server_id: int,
    *,
    client: Client,
    json_body: DisableBackups,
) -> Dict[str, Any]:
    url = "{}/v2/servers/{server_id}/actions#DisableBackups".format(client.base_url, server_id=server_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ActionResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = cast(Any, None)
        return response_202
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ValidationProblemDetails.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server_id: int,
    *,
    client: Client,
    json_body: DisableBackups,
) -> Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Disable Backups for an Existing Server

     This will disable backups for a server only if it has the backup configuration that is created by
    the EnabledBackups action, i.e. two daily backups.
    This is not a 'pause' for backups, this will change the server's options to remove the backups.
    For greater control over the backup options use Options property on the Resize action.
    **NB: This is a destructive operation (previous backups will no longer be available) and no further
    confirmation will be requested.**


    Args:
        server_id (int): The ID of the server on which the action should be performed.
        json_body (DisableBackups): Disable Backups for an Existing Server

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server_id: int,
    *,
    client: Client,
    json_body: DisableBackups,
) -> Optional[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Disable Backups for an Existing Server

     This will disable backups for a server only if it has the backup configuration that is created by
    the EnabledBackups action, i.e. two daily backups.
    This is not a 'pause' for backups, this will change the server's options to remove the backups.
    For greater control over the backup options use Options property on the Resize action.
    **NB: This is a destructive operation (previous backups will no longer be available) and no further
    confirmation will be requested.**


    Args:
        server_id (int): The ID of the server on which the action should be performed.
        json_body (DisableBackups): Disable Backups for an Existing Server

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]
    """

    return sync_detailed(
        server_id=server_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    server_id: int,
    *,
    client: Client,
    json_body: DisableBackups,
) -> Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Disable Backups for an Existing Server

     This will disable backups for a server only if it has the backup configuration that is created by
    the EnabledBackups action, i.e. two daily backups.
    This is not a 'pause' for backups, this will change the server's options to remove the backups.
    For greater control over the backup options use Options property on the Resize action.
    **NB: This is a destructive operation (previous backups will no longer be available) and no further
    confirmation will be requested.**


    Args:
        server_id (int): The ID of the server on which the action should be performed.
        json_body (DisableBackups): Disable Backups for an Existing Server

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server_id: int,
    *,
    client: Client,
    json_body: DisableBackups,
) -> Optional[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Disable Backups for an Existing Server

     This will disable backups for a server only if it has the backup configuration that is created by
    the EnabledBackups action, i.e. two daily backups.
    This is not a 'pause' for backups, this will change the server's options to remove the backups.
    For greater control over the backup options use Options property on the Resize action.
    **NB: This is a destructive operation (previous backups will no longer be available) and no further
    confirmation will be requested.**


    Args:
        server_id (int): The ID of the server on which the action should be performed.
        json_body (DisableBackups): Disable Backups for an Existing Server

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]
    """

    return (
        await asyncio_detailed(
            server_id=server_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
