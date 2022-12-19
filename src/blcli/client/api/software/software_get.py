from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.problem_details import ProblemDetails
from ...models.software_response import SoftwareResponse
from ...types import Response


def _get_kwargs(
    software_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v2/software/{software_id}".format(client.base_url, software_id=software_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ProblemDetails, SoftwareResponse]]:
    if response.status_code == 200:
        response_200 = SoftwareResponse.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ProblemDetails, SoftwareResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    software_id: str,
    *,
    client: Client,
) -> Response[Union[ProblemDetails, SoftwareResponse]]:
    """Fetch Existing Software

    Args:
        software_id (str):

    Returns:
        Response[Union[ProblemDetails, SoftwareResponse]]
    """

    kwargs = _get_kwargs(
        software_id=software_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    software_id: str,
    *,
    client: Client,
) -> Optional[Union[ProblemDetails, SoftwareResponse]]:
    """Fetch Existing Software

    Args:
        software_id (str):

    Returns:
        Response[Union[ProblemDetails, SoftwareResponse]]
    """

    return sync_detailed(
        software_id=software_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    software_id: str,
    *,
    client: Client,
) -> Response[Union[ProblemDetails, SoftwareResponse]]:
    """Fetch Existing Software

    Args:
        software_id (str):

    Returns:
        Response[Union[ProblemDetails, SoftwareResponse]]
    """

    kwargs = _get_kwargs(
        software_id=software_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    software_id: str,
    *,
    client: Client,
) -> Optional[Union[ProblemDetails, SoftwareResponse]]:
    """Fetch Existing Software

    Args:
        software_id (str):

    Returns:
        Response[Union[ProblemDetails, SoftwareResponse]]
    """

    return (
        await asyncio_detailed(
            software_id=software_id,
            client=client,
        )
    ).parsed
