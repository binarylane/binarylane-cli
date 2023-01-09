from __future__ import annotations

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from binarylane import errors
from binarylane.client import Client
from binarylane.models.sizes_response import SizesResponse
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    server_id: Union[Unset, None, int] = UNSET,
    image: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Dict[str, Any]:
    url = "{}/v2/sizes".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["server_id"] = server_id

    params["image"] = image

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
) -> Optional[Union[SizesResponse, ValidationProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SizesResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ValidationProblemDetails.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[SizesResponse, ValidationProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    server_id: Union[Unset, None, int] = UNSET,
    image: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Response[Union[SizesResponse, ValidationProblemDetails]]:
    """List All Available Sizes

    Args:
        server_id (Union[Unset, None, int]): If supplied only sizes available for a resize the
            specified server will be returned. This parameter is only available when authenticated.
        image (Union[Unset, None, str]): If null or not provided regions that support the size are
            included in the returned objects regardless of operating system. If this is provided it
            must be the id or slug of an operating system image and will cause only valid regions for
            the size and operating system to be included in the returned objects.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SizesResponse, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        client=client,
        server_id=server_id,
        image=image,
        page=page,
        per_page=per_page,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    server_id: Union[Unset, None, int] = UNSET,
    image: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Optional[Union[SizesResponse, ValidationProblemDetails]]:
    """List All Available Sizes

    Args:
        server_id (Union[Unset, None, int]): If supplied only sizes available for a resize the
            specified server will be returned. This parameter is only available when authenticated.
        image (Union[Unset, None, str]): If null or not provided regions that support the size are
            included in the returned objects regardless of operating system. If this is provided it
            must be the id or slug of an operating system image and will cause only valid regions for
            the size and operating system to be included in the returned objects.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SizesResponse, ValidationProblemDetails]]
    """

    return sync_detailed(
        client=client,
        server_id=server_id,
        image=image,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    server_id: Union[Unset, None, int] = UNSET,
    image: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Response[Union[SizesResponse, ValidationProblemDetails]]:
    """List All Available Sizes

    Args:
        server_id (Union[Unset, None, int]): If supplied only sizes available for a resize the
            specified server will be returned. This parameter is only available when authenticated.
        image (Union[Unset, None, str]): If null or not provided regions that support the size are
            included in the returned objects regardless of operating system. If this is provided it
            must be the id or slug of an operating system image and will cause only valid regions for
            the size and operating system to be included in the returned objects.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SizesResponse, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        client=client,
        server_id=server_id,
        image=image,
        page=page,
        per_page=per_page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    server_id: Union[Unset, None, int] = UNSET,
    image: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Optional[Union[SizesResponse, ValidationProblemDetails]]:
    """List All Available Sizes

    Args:
        server_id (Union[Unset, None, int]): If supplied only sizes available for a resize the
            specified server will be returned. This parameter is only available when authenticated.
        image (Union[Unset, None, str]): If null or not provided regions that support the size are
            included in the returned objects regardless of operating system. If this is provided it
            must be the id or slug of an operating system image and will cause only valid regions for
            the size and operating system to be included in the returned objects.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SizesResponse, ValidationProblemDetails]]
    """

    return (
        await asyncio_detailed(
            client=client,
            server_id=server_id,
            image=image,
            page=page,
            per_page=per_page,
        )
    ).parsed
