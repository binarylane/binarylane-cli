from __future__ import annotations

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from binarylane import errors
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.software_response import SoftwareResponse
from binarylane.types import Response


def _get_kwargs(
    software_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v2/software/{software_id}".format(client.base_url, software_id=software_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ProblemDetails, SoftwareResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SoftwareResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ProblemDetails, SoftwareResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    software_id: str,
    *,
    client: Client,
) -> Response[Union[ProblemDetails, SoftwareResponse]]:
    """Fetch Existing Software

    Args:
        software_id (str): The ID of the software to fetch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, SoftwareResponse]]
    """

    kwargs = _get_kwargs(
        software_id=software_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    software_id: str,
    *,
    client: Client,
) -> Optional[Union[ProblemDetails, SoftwareResponse]]:
    """Fetch Existing Software

    Args:
        software_id (str): The ID of the software to fetch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, SoftwareResponse]]
    """

    return sync_detailed(
        software_id=software_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    software_id: str,
    *,
    client: Client,
) -> Response[Union[ProblemDetails, SoftwareResponse]]:
    """Fetch Existing Software

    Args:
        software_id (str): The ID of the software to fetch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, SoftwareResponse]]
    """

    kwargs = _get_kwargs(
        software_id=software_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    software_id: str,
    *,
    client: Client,
) -> Optional[Union[ProblemDetails, SoftwareResponse]]:
    """Fetch Existing Software

    Args:
        software_id (str): The ID of the software to fetch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, SoftwareResponse]]
    """

    return (
        await asyncio_detailed(
            software_id=software_id,
            client=client,
        )
    ).parsed
