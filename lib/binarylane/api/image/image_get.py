from __future__ import annotations

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from binarylane import errors
from binarylane.client import Client
from binarylane.models.image_response import ImageResponse
from binarylane.models.problem_details import ProblemDetails
from binarylane.types import Response


def _get_kwargs(
    image_id_or_slug: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v2/images/{image_id_or_slug}".format(client.base_url, image_id_or_slug=image_id_or_slug)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ImageResponse, ProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ImageResponse.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ImageResponse, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    image_id_or_slug: str,
    *,
    client: Client,
) -> Response[Union[Any, ImageResponse, ProblemDetails]]:
    """Fetch an Existing Image

    Args:
        image_id_or_slug (str): The ID or Slug (if an operating system) of the image to retrieve.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ImageResponse, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        image_id_or_slug=image_id_or_slug,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    image_id_or_slug: str,
    *,
    client: Client,
) -> Optional[Union[Any, ImageResponse, ProblemDetails]]:
    """Fetch an Existing Image

    Args:
        image_id_or_slug (str): The ID or Slug (if an operating system) of the image to retrieve.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ImageResponse, ProblemDetails]]
    """

    return sync_detailed(
        image_id_or_slug=image_id_or_slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    image_id_or_slug: str,
    *,
    client: Client,
) -> Response[Union[Any, ImageResponse, ProblemDetails]]:
    """Fetch an Existing Image

    Args:
        image_id_or_slug (str): The ID or Slug (if an operating system) of the image to retrieve.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ImageResponse, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        image_id_or_slug=image_id_or_slug,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    image_id_or_slug: str,
    *,
    client: Client,
) -> Optional[Union[Any, ImageResponse, ProblemDetails]]:
    """Fetch an Existing Image

    Args:
        image_id_or_slug (str): The ID or Slug (if an operating system) of the image to retrieve.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ImageResponse, ProblemDetails]]
    """

    return (
        await asyncio_detailed(
            image_id_or_slug=image_id_or_slug,
            client=client,
        )
    ).parsed
