from __future__ import annotations

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from binarylane import errors
from binarylane.client import Client
from binarylane.models.image_query_type import ImageQueryType
from binarylane.models.images_response import ImagesResponse
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    type: Union[Unset, None, ImageQueryType] = UNSET,
    private: Union[Unset, None, bool] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Dict[str, Any]:
    url = "{}/v2/images".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

    params["private"] = private

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
) -> Optional[Union[Any, ImagesResponse, ValidationProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ImagesResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ValidationProblemDetails.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ImagesResponse, ValidationProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    type: Union[Unset, None, ImageQueryType] = UNSET,
    private: Union[Unset, None, bool] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Response[Union[Any, ImagesResponse, ValidationProblemDetails]]:
    """List All Images

    Args:
        type (Union[Unset, None, ImageQueryType]): Queries for distribution will include images
            that have pre-installed applications.
        private (Union[Unset, None, bool]): Provide 'true' to only list private images. 'false'
            has no effect.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ImagesResponse, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        client=client,
        type=type,
        private=private,
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
    type: Union[Unset, None, ImageQueryType] = UNSET,
    private: Union[Unset, None, bool] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Optional[Union[Any, ImagesResponse, ValidationProblemDetails]]:
    """List All Images

    Args:
        type (Union[Unset, None, ImageQueryType]): Queries for distribution will include images
            that have pre-installed applications.
        private (Union[Unset, None, bool]): Provide 'true' to only list private images. 'false'
            has no effect.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ImagesResponse, ValidationProblemDetails]]
    """

    return sync_detailed(
        client=client,
        type=type,
        private=private,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    type: Union[Unset, None, ImageQueryType] = UNSET,
    private: Union[Unset, None, bool] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Response[Union[Any, ImagesResponse, ValidationProblemDetails]]:
    """List All Images

    Args:
        type (Union[Unset, None, ImageQueryType]): Queries for distribution will include images
            that have pre-installed applications.
        private (Union[Unset, None, bool]): Provide 'true' to only list private images. 'false'
            has no effect.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ImagesResponse, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        client=client,
        type=type,
        private=private,
        page=page,
        per_page=per_page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    type: Union[Unset, None, ImageQueryType] = UNSET,
    private: Union[Unset, None, bool] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Optional[Union[Any, ImagesResponse, ValidationProblemDetails]]:
    """List All Images

    Args:
        type (Union[Unset, None, ImageQueryType]): Queries for distribution will include images
            that have pre-installed applications.
        private (Union[Unset, None, bool]): Provide 'true' to only list private images. 'false'
            has no effect.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ImagesResponse, ValidationProblemDetails]]
    """

    return (
        await asyncio_detailed(
            client=client,
            type=type,
            private=private,
            page=page,
            per_page=per_page,
        )
    ).parsed
