from __future__ import annotations

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from binarylane import errors
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.server_neighbors_response import ServerNeighborsResponse
from binarylane.types import Response


def _get_kwargs(
    server_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v2/servers/{server_id}/neighbors".format(client.base_url, server_id=server_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ProblemDetails, ServerNeighborsResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ServerNeighborsResponse.from_dict(response.json())

        return response_200
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
) -> Response[Union[Any, ProblemDetails, ServerNeighborsResponse]]:
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
) -> Response[Union[Any, ProblemDetails, ServerNeighborsResponse]]:
    """List All Servers That Share a Host with a Server

    Args:
        server_id (int): The ID of the server for which neighbours should be listed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, ServerNeighborsResponse]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
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
) -> Optional[Union[Any, ProblemDetails, ServerNeighborsResponse]]:
    """List All Servers That Share a Host with a Server

    Args:
        server_id (int): The ID of the server for which neighbours should be listed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, ServerNeighborsResponse]]
    """

    return sync_detailed(
        server_id=server_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    server_id: int,
    *,
    client: Client,
) -> Response[Union[Any, ProblemDetails, ServerNeighborsResponse]]:
    """List All Servers That Share a Host with a Server

    Args:
        server_id (int): The ID of the server for which neighbours should be listed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, ServerNeighborsResponse]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, ProblemDetails, ServerNeighborsResponse]]:
    """List All Servers That Share a Host with a Server

    Args:
        server_id (int): The ID of the server for which neighbours should be listed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, ServerNeighborsResponse]]
    """

    return (
        await asyncio_detailed(
            server_id=server_id,
            client=client,
        )
    ).parsed