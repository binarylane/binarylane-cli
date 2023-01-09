from __future__ import annotations

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from binarylane import errors
from binarylane.client import Client
from binarylane.models.domain_response import DomainResponse
from binarylane.models.problem_details import ProblemDetails
from binarylane.types import Response


def _get_kwargs(
    domain_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v2/domains/{domain_name}".format(client.base_url, domain_name=domain_name)

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
) -> Optional[Union[Any, DomainResponse, ProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DomainResponse.from_dict(response.json())

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
) -> Response[Union[Any, DomainResponse, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    domain_name: str,
    *,
    client: Client,
) -> Response[Union[Any, DomainResponse, ProblemDetails]]:
    """Fetch an Existing Domain

    Args:
        domain_name (str): The name of the domain to fetch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainResponse, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        domain_name=domain_name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    domain_name: str,
    *,
    client: Client,
) -> Optional[Union[Any, DomainResponse, ProblemDetails]]:
    """Fetch an Existing Domain

    Args:
        domain_name (str): The name of the domain to fetch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainResponse, ProblemDetails]]
    """

    return sync_detailed(
        domain_name=domain_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    domain_name: str,
    *,
    client: Client,
) -> Response[Union[Any, DomainResponse, ProblemDetails]]:
    """Fetch an Existing Domain

    Args:
        domain_name (str): The name of the domain to fetch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainResponse, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        domain_name=domain_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain_name: str,
    *,
    client: Client,
) -> Optional[Union[Any, DomainResponse, ProblemDetails]]:
    """Fetch an Existing Domain

    Args:
        domain_name (str): The name of the domain to fetch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainResponse, ProblemDetails]]
    """

    return (
        await asyncio_detailed(
            domain_name=domain_name,
            client=client,
        )
    ).parsed
