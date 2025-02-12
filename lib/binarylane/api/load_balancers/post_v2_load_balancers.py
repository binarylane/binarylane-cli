from __future__ import annotations

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from binarylane import errors
from binarylane.client import Client
from binarylane.models.create_load_balancer_request import CreateLoadBalancerRequest
from binarylane.models.create_load_balancer_response import CreateLoadBalancerResponse
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateLoadBalancerRequest,
) -> Dict[str, Any]:
    url = "{}/v2/load_balancers".format(client.base_url)

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
) -> Optional[Union[Any, CreateLoadBalancerResponse, ValidationProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateLoadBalancerResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ValidationProblemDetails.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, CreateLoadBalancerResponse, ValidationProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateLoadBalancerRequest,
) -> Response[Union[Any, CreateLoadBalancerResponse, ValidationProblemDetails]]:
    """Create a New Load Balancer

    Args:
        json_body (CreateLoadBalancerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateLoadBalancerResponse, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: CreateLoadBalancerRequest,
) -> Optional[Union[Any, CreateLoadBalancerResponse, ValidationProblemDetails]]:
    """Create a New Load Balancer

    Args:
        json_body (CreateLoadBalancerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateLoadBalancerResponse, ValidationProblemDetails]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateLoadBalancerRequest,
) -> Response[Union[Any, CreateLoadBalancerResponse, ValidationProblemDetails]]:
    """Create a New Load Balancer

    Args:
        json_body (CreateLoadBalancerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateLoadBalancerResponse, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CreateLoadBalancerRequest,
) -> Optional[Union[Any, CreateLoadBalancerResponse, ValidationProblemDetails]]:
    """Create a New Load Balancer

    Args:
        json_body (CreateLoadBalancerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateLoadBalancerResponse, ValidationProblemDetails]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
