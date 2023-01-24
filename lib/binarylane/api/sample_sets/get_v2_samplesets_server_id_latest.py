from __future__ import annotations

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from binarylane import errors
from binarylane.client import Client
from binarylane.models.data_interval import DataInterval
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.sample_set_response import SampleSetResponse
from binarylane.types import UNSET, Response, Unset


def _get_kwargs(
    server_id: int,
    *,
    client: Client,
    data_interval: Union[Unset, None, DataInterval] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v2/samplesets/{server_id}/latest".format(client.base_url, server_id=server_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_data_interval: Union[Unset, None, str] = UNSET
    if not isinstance(data_interval, Unset):
        json_data_interval = data_interval.value if data_interval else None

    params["data_interval"] = json_data_interval

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
) -> Optional[Union[Any, ProblemDetails, SampleSetResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SampleSetResponse.from_dict(response.json())

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


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ProblemDetails, SampleSetResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server_id: int,
    *,
    client: Client,
    data_interval: Union[Unset, None, DataInterval] = UNSET,
) -> Response[Union[Any, ProblemDetails, SampleSetResponse]]:
    """Fetch the Latest Performance and Usage Data Sample Set for a Server

     Returns the latest performance and usage sample set.

    Args:
        server_id (int): The target server id.
        data_interval (Union[Unset, None, DataInterval]):
            | Value | Description |
            | ----- | ----------- |
            | five-minute | 5 Minutes |
            | half-hour | 30 Minutes |
            | four-hour | 4 Hours |
            | day | 1 Day |
            | week | 7 Days |
            | month | 1 Month |


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, SampleSetResponse]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
        data_interval=data_interval,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server_id: int,
    *,
    client: Client,
    data_interval: Union[Unset, None, DataInterval] = UNSET,
) -> Optional[Union[Any, ProblemDetails, SampleSetResponse]]:
    """Fetch the Latest Performance and Usage Data Sample Set for a Server

     Returns the latest performance and usage sample set.

    Args:
        server_id (int): The target server id.
        data_interval (Union[Unset, None, DataInterval]):
            | Value | Description |
            | ----- | ----------- |
            | five-minute | 5 Minutes |
            | half-hour | 30 Minutes |
            | four-hour | 4 Hours |
            | day | 1 Day |
            | week | 7 Days |
            | month | 1 Month |


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, SampleSetResponse]]
    """

    return sync_detailed(
        server_id=server_id,
        client=client,
        data_interval=data_interval,
    ).parsed


async def asyncio_detailed(
    server_id: int,
    *,
    client: Client,
    data_interval: Union[Unset, None, DataInterval] = UNSET,
) -> Response[Union[Any, ProblemDetails, SampleSetResponse]]:
    """Fetch the Latest Performance and Usage Data Sample Set for a Server

     Returns the latest performance and usage sample set.

    Args:
        server_id (int): The target server id.
        data_interval (Union[Unset, None, DataInterval]):
            | Value | Description |
            | ----- | ----------- |
            | five-minute | 5 Minutes |
            | half-hour | 30 Minutes |
            | four-hour | 4 Hours |
            | day | 1 Day |
            | week | 7 Days |
            | month | 1 Month |


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, SampleSetResponse]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
        data_interval=data_interval,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server_id: int,
    *,
    client: Client,
    data_interval: Union[Unset, None, DataInterval] = UNSET,
) -> Optional[Union[Any, ProblemDetails, SampleSetResponse]]:
    """Fetch the Latest Performance and Usage Data Sample Set for a Server

     Returns the latest performance and usage sample set.

    Args:
        server_id (int): The target server id.
        data_interval (Union[Unset, None, DataInterval]):
            | Value | Description |
            | ----- | ----------- |
            | five-minute | 5 Minutes |
            | half-hour | 30 Minutes |
            | four-hour | 4 Hours |
            | day | 1 Day |
            | week | 7 Days |
            | month | 1 Month |


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, SampleSetResponse]]
    """

    return (
        await asyncio_detailed(
            server_id=server_id,
            client=client,
            data_interval=data_interval,
        )
    ).parsed
