from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    server_id: int,
    *,
    client: Client,
    reason: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v2/servers/{server_id}".format(client.base_url, server_id=server_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["reason"] = reason

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ProblemDetails]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    server_id: int,
    *,
    client: Client,
    reason: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    """Cancel an Existing Server

    Args:
        server_id (int): The target server id.
        reason (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
        reason=reason,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    server_id: int,
    *,
    client: Client,
    reason: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    """Cancel an Existing Server

    Args:
        server_id (int): The target server id.
        reason (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    return sync_detailed(
        server_id=server_id,
        client=client,
        reason=reason,
    ).parsed


async def asyncio_detailed(
    server_id: int,
    *,
    client: Client,
    reason: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    """Cancel an Existing Server

    Args:
        server_id (int): The target server id.
        reason (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
        reason=reason,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    server_id: int,
    *,
    client: Client,
    reason: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    """Cancel an Existing Server

    Args:
        server_id (int): The target server id.
        reason (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    return (
        await asyncio_detailed(
            server_id=server_id,
            client=client,
            reason=reason,
        )
    ).parsed
