from __future__ import annotations

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from binarylane import errors
from binarylane.client import Client
from binarylane.models.domain_record_type import DomainRecordType
from binarylane.models.domain_records_response import DomainRecordsResponse
from binarylane.models.problem_details import ProblemDetails
from binarylane.types import UNSET, Response, Unset


def _get_kwargs(
    domain_name: str,
    *,
    client: Client,
    type: Union[Unset, None, DomainRecordType] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Dict[str, Any]:
    url = "{}/v2/domains/{domain_name}/records".format(client.base_url, domain_name=domain_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

    params["name"] = name

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, DomainRecordsResponse, ProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DomainRecordsResponse.from_dict(response.json())

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
) -> Response[Union[Any, DomainRecordsResponse, ProblemDetails]]:
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
    type: Union[Unset, None, DomainRecordType] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Response[Union[Any, DomainRecordsResponse, ProblemDetails]]:
    """List All Domain Records for a Domain

    Args:
        domain_name (str): The domain name for which records should be listed.
        type (Union[Unset, None, DomainRecordType]):
            | Value | Description |
            | ----- | ----------- |
            | A | Map an IPv4 address to a hostname. |
            | AAAA | Map an IPv6 address to a hostname. |
            | CAA | Restrict which certificate authorities are permitted to issue certificates for a
            domain. |
            | CNAME | Define an alias for your canonical hostname. |
            | MX | Define the mail exchanges that handle mail for the domain. |
            | NS | Define the nameservers that manage the domain. |
            | SOA | The Start of Authority record for the zone. |
            | SRV | Specify a server by hostname and port to handle a service or services. |
            | TXT | Define a string of text that is associated with a hostname. |

        name (Union[Unset, None, str]): Only return records for this subdomain name.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainRecordsResponse, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        domain_name=domain_name,
        client=client,
        type=type,
        name=name,
        page=page,
        per_page=per_page,
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
    type: Union[Unset, None, DomainRecordType] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Optional[Union[Any, DomainRecordsResponse, ProblemDetails]]:
    """List All Domain Records for a Domain

    Args:
        domain_name (str): The domain name for which records should be listed.
        type (Union[Unset, None, DomainRecordType]):
            | Value | Description |
            | ----- | ----------- |
            | A | Map an IPv4 address to a hostname. |
            | AAAA | Map an IPv6 address to a hostname. |
            | CAA | Restrict which certificate authorities are permitted to issue certificates for a
            domain. |
            | CNAME | Define an alias for your canonical hostname. |
            | MX | Define the mail exchanges that handle mail for the domain. |
            | NS | Define the nameservers that manage the domain. |
            | SOA | The Start of Authority record for the zone. |
            | SRV | Specify a server by hostname and port to handle a service or services. |
            | TXT | Define a string of text that is associated with a hostname. |

        name (Union[Unset, None, str]): Only return records for this subdomain name.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainRecordsResponse, ProblemDetails]]
    """

    return sync_detailed(
        domain_name=domain_name,
        client=client,
        type=type,
        name=name,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    domain_name: str,
    *,
    client: Client,
    type: Union[Unset, None, DomainRecordType] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Response[Union[Any, DomainRecordsResponse, ProblemDetails]]:
    """List All Domain Records for a Domain

    Args:
        domain_name (str): The domain name for which records should be listed.
        type (Union[Unset, None, DomainRecordType]):
            | Value | Description |
            | ----- | ----------- |
            | A | Map an IPv4 address to a hostname. |
            | AAAA | Map an IPv6 address to a hostname. |
            | CAA | Restrict which certificate authorities are permitted to issue certificates for a
            domain. |
            | CNAME | Define an alias for your canonical hostname. |
            | MX | Define the mail exchanges that handle mail for the domain. |
            | NS | Define the nameservers that manage the domain. |
            | SOA | The Start of Authority record for the zone. |
            | SRV | Specify a server by hostname and port to handle a service or services. |
            | TXT | Define a string of text that is associated with a hostname. |

        name (Union[Unset, None, str]): Only return records for this subdomain name.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainRecordsResponse, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        domain_name=domain_name,
        client=client,
        type=type,
        name=name,
        page=page,
        per_page=per_page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain_name: str,
    *,
    client: Client,
    type: Union[Unset, None, DomainRecordType] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Optional[Union[Any, DomainRecordsResponse, ProblemDetails]]:
    """List All Domain Records for a Domain

    Args:
        domain_name (str): The domain name for which records should be listed.
        type (Union[Unset, None, DomainRecordType]):
            | Value | Description |
            | ----- | ----------- |
            | A | Map an IPv4 address to a hostname. |
            | AAAA | Map an IPv6 address to a hostname. |
            | CAA | Restrict which certificate authorities are permitted to issue certificates for a
            domain. |
            | CNAME | Define an alias for your canonical hostname. |
            | MX | Define the mail exchanges that handle mail for the domain. |
            | NS | Define the nameservers that manage the domain. |
            | SOA | The Start of Authority record for the zone. |
            | SRV | Specify a server by hostname and port to handle a service or services. |
            | TXT | Define a string of text that is associated with a hostname. |

        name (Union[Unset, None, str]): Only return records for this subdomain name.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainRecordsResponse, ProblemDetails]]
    """

    return (
        await asyncio_detailed(
            domain_name=domain_name,
            client=client,
            type=type,
            name=name,
            page=page,
            per_page=per_page,
        )
    ).parsed
