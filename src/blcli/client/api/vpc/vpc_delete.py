from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    vpc_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v2/vpcs/{vpc_id}".format(client.base_url, vpc_id=vpc_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403
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
    vpc_id: int,
    *,
    client: Client,
) -> Response[Union[Any, ProblemDetails]]:
    """Delete an Existing VPC

    Args:
        vpc_id (int): The target vpc id.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        vpc_id=vpc_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    vpc_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, ProblemDetails]]:
    """Delete an Existing VPC

    Args:
        vpc_id (int): The target vpc id.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    return sync_detailed(
        vpc_id=vpc_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    vpc_id: int,
    *,
    client: Client,
) -> Response[Union[Any, ProblemDetails]]:
    """Delete an Existing VPC

    Args:
        vpc_id (int): The target vpc id.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        vpc_id=vpc_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    vpc_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, ProblemDetails]]:
    """Delete an Existing VPC

    Args:
        vpc_id (int): The target vpc id.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    return (
        await asyncio_detailed(
            vpc_id=vpc_id,
            client=client,
        )
    ).parsed
