from __future__ import annotations

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from binarylane import errors
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.vpc_response import VpcResponse
from binarylane.types import Response


def _get_kwargs(
    vpc_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v2/vpcs/{vpc_id}".format(client.base_url, vpc_id=vpc_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ProblemDetails, VpcResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = VpcResponse.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ProblemDetails, VpcResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vpc_id: int,
    *,
    client: Client,
) -> Response[Union[Any, ProblemDetails, VpcResponse]]:
    """Fetch an Existing VPC

    Args:
        vpc_id (int): The target vpc id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, VpcResponse]]
    """

    kwargs = _get_kwargs(
        vpc_id=vpc_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vpc_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, ProblemDetails, VpcResponse]]:
    """Fetch an Existing VPC

    Args:
        vpc_id (int): The target vpc id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, VpcResponse]]
    """

    return sync_detailed(
        vpc_id=vpc_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    vpc_id: int,
    *,
    client: Client,
) -> Response[Union[Any, ProblemDetails, VpcResponse]]:
    """Fetch an Existing VPC

    Args:
        vpc_id (int): The target vpc id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, VpcResponse]]
    """

    kwargs = _get_kwargs(
        vpc_id=vpc_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vpc_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, ProblemDetails, VpcResponse]]:
    """Fetch an Existing VPC

    Args:
        vpc_id (int): The target vpc id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, VpcResponse]]
    """

    return (
        await asyncio_detailed(
            vpc_id=vpc_id,
            client=client,
        )
    ).parsed
