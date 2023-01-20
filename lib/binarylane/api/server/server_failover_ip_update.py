from __future__ import annotations

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from binarylane import errors
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.failover_ips_request import FailoverIpsRequest
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Response


def _get_kwargs(
    server_id: int,
    *,
    client: Client,
    json_body: FailoverIpsRequest,
) -> Dict[str, Any]:
    url = "{}/v2/failover_ips/{server_id}".format(client.base_url, server_id=server_id)

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
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
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
    json_body: FailoverIpsRequest,
) -> Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Sets the List of Failover IPs that are Assigned to a Server

     This overwrites the current list, i.e. submit the entire list, not just updates.
    If NoContent is returned no changes were made.
    If an action is returned the changes have been saved but the effect may not be complete until the
    action is complete. If the action does not complete the network changes can be forced by rebooting
    the server.

    Args:
        server_id (int): The target server id.
        json_body (FailoverIpsRequest):

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
    json_body: FailoverIpsRequest,
) -> Optional[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Sets the List of Failover IPs that are Assigned to a Server

     This overwrites the current list, i.e. submit the entire list, not just updates.
    If NoContent is returned no changes were made.
    If an action is returned the changes have been saved but the effect may not be complete until the
    action is complete. If the action does not complete the network changes can be forced by rebooting
    the server.

    Args:
        server_id (int): The target server id.
        json_body (FailoverIpsRequest):

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
    json_body: FailoverIpsRequest,
) -> Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Sets the List of Failover IPs that are Assigned to a Server

     This overwrites the current list, i.e. submit the entire list, not just updates.
    If NoContent is returned no changes were made.
    If an action is returned the changes have been saved but the effect may not be complete until the
    action is complete. If the action does not complete the network changes can be forced by rebooting
    the server.

    Args:
        server_id (int): The target server id.
        json_body (FailoverIpsRequest):

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
    json_body: FailoverIpsRequest,
) -> Optional[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Sets the List of Failover IPs that are Assigned to a Server

     This overwrites the current list, i.e. submit the entire list, not just updates.
    If NoContent is returned no changes were made.
    If an action is returned the changes have been saved but the effect may not be complete until the
    action is complete. If the action does not complete the network changes can be forced by rebooting
    the server.

    Args:
        server_id (int): The target server id.
        json_body (FailoverIpsRequest):

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
