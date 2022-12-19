from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.problem_details import ProblemDetails
from ...models.ssh_key_response import SshKeyResponse
from ...types import Response


def _get_kwargs(
    key_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v2/account/keys/{key_id}".format(client.base_url, key_id=key_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ProblemDetails, SshKeyResponse]]:
    if response.status_code == 200:
        response_200 = SshKeyResponse.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ProblemDetails, SshKeyResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    key_id: str,
    *,
    client: Client,
) -> Response[Union[Any, ProblemDetails, SshKeyResponse]]:
    """Fetch an Existing SSH Key

     The key_id may be either the Id or the key fingerprint.

    Args:
        key_id (str):

    Returns:
        Response[Union[Any, ProblemDetails, SshKeyResponse]]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    key_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, ProblemDetails, SshKeyResponse]]:
    """Fetch an Existing SSH Key

     The key_id may be either the Id or the key fingerprint.

    Args:
        key_id (str):

    Returns:
        Response[Union[Any, ProblemDetails, SshKeyResponse]]
    """

    return sync_detailed(
        key_id=key_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    key_id: str,
    *,
    client: Client,
) -> Response[Union[Any, ProblemDetails, SshKeyResponse]]:
    """Fetch an Existing SSH Key

     The key_id may be either the Id or the key fingerprint.

    Args:
        key_id (str):

    Returns:
        Response[Union[Any, ProblemDetails, SshKeyResponse]]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    key_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, ProblemDetails, SshKeyResponse]]:
    """Fetch an Existing SSH Key

     The key_id may be either the Id or the key fingerprint.

    Args:
        key_id (str):

    Returns:
        Response[Union[Any, ProblemDetails, SshKeyResponse]]
    """

    return (
        await asyncio_detailed(
            key_id=key_id,
            client=client,
        )
    ).parsed
