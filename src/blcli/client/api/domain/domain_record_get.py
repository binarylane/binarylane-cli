from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.domain_record_response import DomainRecordResponse
from ...models.problem_details import ProblemDetails
from ...types import Response


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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, DomainRecordResponse, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = DomainRecordResponse.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, DomainRecordResponse, ProblemDetails]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    domain_name: str,
    record_id: int,
    *,
    client: Client,
) -> Response[Union[Any, DomainRecordResponse, ProblemDetails]]:
    """Fetch an Existing Domain Record

    Args:
        domain_name (str):
        record_id (int):

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

    return _build_response(response=response)


def sync(
    domain_name: str,
    record_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, DomainRecordResponse, ProblemDetails]]:
    """Fetch an Existing Domain Record

    Args:
        domain_name (str):
        record_id (int):

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
        domain_name (str):
        record_id (int):

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

    return _build_response(response=response)


async def asyncio(
    domain_name: str,
    record_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, DomainRecordResponse, ProblemDetails]]:
    """Fetch an Existing Domain Record

    Args:
        domain_name (str):
        record_id (int):

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
