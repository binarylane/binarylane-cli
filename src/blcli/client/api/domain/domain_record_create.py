from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.domain_record_request import DomainRecordRequest
from ...models.domain_record_response import DomainRecordResponse
from ...models.problem_details import ProblemDetails
from ...models.validation_problem_details import ValidationProblemDetails
from ...types import Response


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
    *, response: httpx.Response
) -> Optional[Union[Any, DomainRecordResponse, ProblemDetails, ValidationProblemDetails]]:
    if response.status_code == 200:
        response_200 = DomainRecordResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ValidationProblemDetails.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, DomainRecordResponse, ProblemDetails, ValidationProblemDetails]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    domain_name: str,
    *,
    client: Client,
    json_body: DomainRecordRequest,
) -> Response[Union[Any, DomainRecordResponse, ProblemDetails, ValidationProblemDetails]]:
    """Create a New Domain Record

    Args:
        domain_name (str):
        json_body (DomainRecordRequest): If this is used to update an existing DomainRecord any
            values not provided will be retained. Provide empty strings to clear existing string
            values, nulls to retain the existing values.

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

    return _build_response(response=response)


def sync(
    domain_name: str,
    *,
    client: Client,
    json_body: DomainRecordRequest,
) -> Optional[Union[Any, DomainRecordResponse, ProblemDetails, ValidationProblemDetails]]:
    """Create a New Domain Record

    Args:
        domain_name (str):
        json_body (DomainRecordRequest): If this is used to update an existing DomainRecord any
            values not provided will be retained. Provide empty strings to clear existing string
            values, nulls to retain the existing values.

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
        domain_name (str):
        json_body (DomainRecordRequest): If this is used to update an existing DomainRecord any
            values not provided will be retained. Provide empty strings to clear existing string
            values, nulls to retain the existing values.

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

    return _build_response(response=response)


async def asyncio(
    domain_name: str,
    *,
    client: Client,
    json_body: DomainRecordRequest,
) -> Optional[Union[Any, DomainRecordResponse, ProblemDetails, ValidationProblemDetails]]:
    """Create a New Domain Record

    Args:
        domain_name (str):
        json_body (DomainRecordRequest): If this is used to update an existing DomainRecord any
            values not provided will be retained. Provide empty strings to clear existing string
            values, nulls to retain the existing values.

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
