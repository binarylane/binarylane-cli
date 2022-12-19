from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.problem_details import ProblemDetails
from ...models.softwares_response import SoftwaresResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    operating_system_id_or_slug: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Dict[str, Any]:
    url = "{}/v2/software/operating_system/{operating_system_id_or_slug}".format(
        client.base_url, operating_system_id_or_slug=operating_system_id_or_slug
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ProblemDetails, SoftwaresResponse]]:
    if response.status_code == 200:
        response_200 = SoftwaresResponse.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ProblemDetails, SoftwaresResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    operating_system_id_or_slug: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Response[Union[ProblemDetails, SoftwaresResponse]]:
    """List All Available Software for an Existing Operating System

    Args:
        operating_system_id_or_slug (str):
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Returns:
        Response[Union[ProblemDetails, SoftwaresResponse]]
    """

    kwargs = _get_kwargs(
        operating_system_id_or_slug=operating_system_id_or_slug,
        client=client,
        page=page,
        per_page=per_page,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    operating_system_id_or_slug: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Optional[Union[ProblemDetails, SoftwaresResponse]]:
    """List All Available Software for an Existing Operating System

    Args:
        operating_system_id_or_slug (str):
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Returns:
        Response[Union[ProblemDetails, SoftwaresResponse]]
    """

    return sync_detailed(
        operating_system_id_or_slug=operating_system_id_or_slug,
        client=client,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    operating_system_id_or_slug: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Response[Union[ProblemDetails, SoftwaresResponse]]:
    """List All Available Software for an Existing Operating System

    Args:
        operating_system_id_or_slug (str):
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Returns:
        Response[Union[ProblemDetails, SoftwaresResponse]]
    """

    kwargs = _get_kwargs(
        operating_system_id_or_slug=operating_system_id_or_slug,
        client=client,
        page=page,
        per_page=per_page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    operating_system_id_or_slug: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Optional[Union[ProblemDetails, SoftwaresResponse]]:
    """List All Available Software for an Existing Operating System

    Args:
        operating_system_id_or_slug (str):
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Returns:
        Response[Union[ProblemDetails, SoftwaresResponse]]
    """

    return (
        await asyncio_detailed(
            operating_system_id_or_slug=operating_system_id_or_slug,
            client=client,
            page=page,
            per_page=per_page,
        )
    ).parsed
