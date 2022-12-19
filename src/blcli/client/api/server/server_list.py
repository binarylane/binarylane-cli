from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.servers_response import ServersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    tag_name: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Dict[str, Any]:
    url = "{}/v2/servers".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["tag_name"] = tag_name

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ServersResponse]]:
    if response.status_code == 200:
        response_200 = ServersResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ServersResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    tag_name: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Response[Union[Any, ServersResponse]]:
    """List All Servers

    Args:
        tag_name (Union[Unset, None, str]):
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Returns:
        Response[Union[Any, ServersResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        tag_name=tag_name,
        page=page,
        per_page=per_page,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    tag_name: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Optional[Union[Any, ServersResponse]]:
    """List All Servers

    Args:
        tag_name (Union[Unset, None, str]):
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Returns:
        Response[Union[Any, ServersResponse]]
    """

    return sync_detailed(
        client=client,
        tag_name=tag_name,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    tag_name: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Response[Union[Any, ServersResponse]]:
    """List All Servers

    Args:
        tag_name (Union[Unset, None, str]):
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Returns:
        Response[Union[Any, ServersResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        tag_name=tag_name,
        page=page,
        per_page=per_page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    tag_name: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Optional[Union[Any, ServersResponse]]:
    """List All Servers

    Args:
        tag_name (Union[Unset, None, str]):
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Returns:
        Response[Union[Any, ServersResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            tag_name=tag_name,
            page=page,
            per_page=per_page,
        )
    ).parsed
