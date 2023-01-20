from __future__ import annotations

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from binarylane import errors
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.reverse_nameservers_request import ReverseNameserversRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: ReverseNameserversRequest,
) -> Dict[str, Any]:
    url = "{}/v2/reverse_names/ipv6".format(client.base_url)

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
    *,
    client: Client,
    json_body: ReverseNameserversRequest,
) -> Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Create New or Update Existing IPv6 Name Server Records

    Args:
        json_body (ReverseNameserversRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]
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
    json_body: ReverseNameserversRequest,
) -> Optional[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Create New or Update Existing IPv6 Name Server Records

    Args:
        json_body (ReverseNameserversRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: ReverseNameserversRequest,
) -> Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Create New or Update Existing IPv6 Name Server Records

    Args:
        json_body (ReverseNameserversRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]
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
    json_body: ReverseNameserversRequest,
) -> Optional[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Create New or Update Existing IPv6 Name Server Records

    Args:
        json_body (ReverseNameserversRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
