from __future__ import annotations

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from binarylane import errors
from binarylane.client import Client
from binarylane.models.domain_record_request import DomainRecordRequest
from binarylane.models.domain_record_response import DomainRecordResponse
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Response


def _get_kwargs(
    domain_name: str,
    *,
    client: Client,
    json_body: DomainRecordRequest,
) -> Dict[str, Any]:
    url = "{}/v2/domains/{domain_name}/records".format(client.base_url, domain_name=domain_name)

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
) -> Optional[Union[Any, DomainRecordResponse, ProblemDetails, ValidationProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DomainRecordResponse.from_dict(response.json())

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
) -> Response[Union[Any, DomainRecordResponse, ProblemDetails, ValidationProblemDetails]]:
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
    json_body: DomainRecordRequest,
) -> Response[Union[Any, DomainRecordResponse, ProblemDetails, ValidationProblemDetails]]:
    """Create a New Domain Record

    Args:
        domain_name (str): The domain name for which the record should be created.
        json_body (DomainRecordRequest): If this is used to update an existing DomainRecord any
            values not provided will be retained. Provide empty strings to clear existing string
            values, nulls to retain the existing values.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainRecordResponse, ProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        domain_name=domain_name,
        client=client,
        json_body=json_body,
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
    json_body: DomainRecordRequest,
) -> Optional[Union[Any, DomainRecordResponse, ProblemDetails, ValidationProblemDetails]]:
    """Create a New Domain Record

    Args:
        domain_name (str): The domain name for which the record should be created.
        json_body (DomainRecordRequest): If this is used to update an existing DomainRecord any
            values not provided will be retained. Provide empty strings to clear existing string
            values, nulls to retain the existing values.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainRecordResponse, ProblemDetails, ValidationProblemDetails]]
    """

    return sync_detailed(
        domain_name=domain_name,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    domain_name: str,
    *,
    client: Client,
    json_body: DomainRecordRequest,
) -> Response[Union[Any, DomainRecordResponse, ProblemDetails, ValidationProblemDetails]]:
    """Create a New Domain Record

    Args:
        domain_name (str): The domain name for which the record should be created.
        json_body (DomainRecordRequest): If this is used to update an existing DomainRecord any
            values not provided will be retained. Provide empty strings to clear existing string
            values, nulls to retain the existing values.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainRecordResponse, ProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        domain_name=domain_name,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain_name: str,
    *,
    client: Client,
    json_body: DomainRecordRequest,
) -> Optional[Union[Any, DomainRecordResponse, ProblemDetails, ValidationProblemDetails]]:
    """Create a New Domain Record

    Args:
        domain_name (str): The domain name for which the record should be created.
        json_body (DomainRecordRequest): If this is used to update an existing DomainRecord any
            values not provided will be retained. Provide empty strings to clear existing string
            values, nulls to retain the existing values.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainRecordResponse, ProblemDetails, ValidationProblemDetails]]
    """

    return (
        await asyncio_detailed(
            domain_name=domain_name,
            client=client,
            json_body=json_body,
        )
    ).parsed
