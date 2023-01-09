from __future__ import annotations

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from binarylane import errors
from binarylane.client import Client
from binarylane.models.domain_record_response import DomainRecordResponse
from binarylane.models.problem_details import ProblemDetails
from binarylane.types import Response


def _get_kwargs(
    domain_name: str,
    record_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v2/domains/{domain_name}/records/{record_id}".format(
        client.base_url, domain_name=domain_name, record_id=record_id
    )

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
) -> Optional[Union[Any, DomainRecordResponse, ProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DomainRecordResponse.from_dict(response.json())

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
) -> Response[Union[Any, DomainRecordResponse, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    domain_name: str,
    record_id: int,
    *,
    client: Client,
) -> Response[Union[Any, DomainRecordResponse, ProblemDetails]]:
    """Fetch an Existing Domain Record

    Args:
        domain_name (str): The domain name for which the record should be fetched.
        record_id (int): The ID of the record to fetch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainRecordResponse, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        domain_name=domain_name,
        record_id=record_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    domain_name: str,
    record_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, DomainRecordResponse, ProblemDetails]]:
    """Fetch an Existing Domain Record

    Args:
        domain_name (str): The domain name for which the record should be fetched.
        record_id (int): The ID of the record to fetch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainRecordResponse, ProblemDetails]]
    """

    return sync_detailed(
        domain_name=domain_name,
        record_id=record_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    domain_name: str,
    record_id: int,
    *,
    client: Client,
) -> Response[Union[Any, DomainRecordResponse, ProblemDetails]]:
    """Fetch an Existing Domain Record

    Args:
        domain_name (str): The domain name for which the record should be fetched.
        record_id (int): The ID of the record to fetch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainRecordResponse, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        domain_name=domain_name,
        record_id=record_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain_name: str,
    record_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, DomainRecordResponse, ProblemDetails]]:
    """Fetch an Existing Domain Record

    Args:
        domain_name (str): The domain name for which the record should be fetched.
        record_id (int): The ID of the record to fetch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainRecordResponse, ProblemDetails]]
    """

    return (
        await asyncio_detailed(
            domain_name=domain_name,
            record_id=record_id,
            client=client,
        )
    ).parsed
