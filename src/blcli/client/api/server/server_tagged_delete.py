from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    tag_name: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v2/servers".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["tag_name"] = tag_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    tag_name: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Cancel Existing Servers by Tag

     Tags are not currently supported and this endpoint will not cancel any servers.

    Args:
        tag_name (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        tag_name=tag_name,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    tag_name: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Cancel Existing Servers by Tag

     Tags are not currently supported and this endpoint will not cancel any servers.

    Args:
        tag_name (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        tag_name=tag_name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
