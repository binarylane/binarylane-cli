from __future__ import annotations

import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from binarylane import errors
from binarylane.client import Client
from binarylane.models.data_interval import DataInterval
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.sample_sets_response import SampleSetsResponse
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Response, Unset


def _get_kwargs(
    server_id: int,
    *,
    client: Client,
    data_interval: Union[Unset, None, DataInterval] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Dict[str, Any]:
    url = "{}/v2/samplesets/{server_id}".format(client.base_url, server_id=server_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_data_interval: Union[Unset, None, str] = UNSET
    if not isinstance(data_interval, Unset):
        json_data_interval = data_interval.value if data_interval else None

    params["data_interval"] = json_data_interval

    json_start: Union[Unset, None, str] = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat() if start else None

    params["start"] = json_start

    json_end: Union[Unset, None, str] = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat() if end else None

    params["end"] = json_end

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
) -> Optional[Union[Any, ProblemDetails, SampleSetsResponse, ValidationProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SampleSetsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ValidationProblemDetails.from_dict(response.json())

        return response_400
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
) -> Response[Union[Any, ProblemDetails, SampleSetsResponse, ValidationProblemDetails]]:
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
    start: Union[Unset, None, datetime.datetime] = UNSET,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Response[Union[Any, ProblemDetails, SampleSetsResponse, ValidationProblemDetails]]:
    """Fetch all of the Performance and Usage Data Sample Sets for a Server

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

        start (Union[Unset, None, datetime.datetime]): The start of the window of samples to
            retrieve, ISO8601 format (eg 2022-12-30T22:50:00Z). Defaults to 1 week before end for
            intervals larger than 5 minutes, or 1 day for 5 minute intervals.
        end (Union[Unset, None, datetime.datetime]): The start of the window of samples to
            retrieve, ISO8601 format (eg 2022-12-30T22:50:00Z). Defaults to 1 week or 1 day after
            start date depending on the selected data interval (or the current time if start is not
            provided). Can't be more than 1 year from start.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, SampleSetsResponse, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
        data_interval=data_interval,
        start=start,
        end=end,
        page=page,
        per_page=per_page,
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
    start: Union[Unset, None, datetime.datetime] = UNSET,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Optional[Union[Any, ProblemDetails, SampleSetsResponse, ValidationProblemDetails]]:
    """Fetch all of the Performance and Usage Data Sample Sets for a Server

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

        start (Union[Unset, None, datetime.datetime]): The start of the window of samples to
            retrieve, ISO8601 format (eg 2022-12-30T22:50:00Z). Defaults to 1 week before end for
            intervals larger than 5 minutes, or 1 day for 5 minute intervals.
        end (Union[Unset, None, datetime.datetime]): The start of the window of samples to
            retrieve, ISO8601 format (eg 2022-12-30T22:50:00Z). Defaults to 1 week or 1 day after
            start date depending on the selected data interval (or the current time if start is not
            provided). Can't be more than 1 year from start.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, SampleSetsResponse, ValidationProblemDetails]]
    """

    return sync_detailed(
        server_id=server_id,
        client=client,
        data_interval=data_interval,
        start=start,
        end=end,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    server_id: int,
    *,
    client: Client,
    data_interval: Union[Unset, None, DataInterval] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Response[Union[Any, ProblemDetails, SampleSetsResponse, ValidationProblemDetails]]:
    """Fetch all of the Performance and Usage Data Sample Sets for a Server

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

        start (Union[Unset, None, datetime.datetime]): The start of the window of samples to
            retrieve, ISO8601 format (eg 2022-12-30T22:50:00Z). Defaults to 1 week before end for
            intervals larger than 5 minutes, or 1 day for 5 minute intervals.
        end (Union[Unset, None, datetime.datetime]): The start of the window of samples to
            retrieve, ISO8601 format (eg 2022-12-30T22:50:00Z). Defaults to 1 week or 1 day after
            start date depending on the selected data interval (or the current time if start is not
            provided). Can't be more than 1 year from start.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, SampleSetsResponse, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
        data_interval=data_interval,
        start=start,
        end=end,
        page=page,
        per_page=per_page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server_id: int,
    *,
    client: Client,
    data_interval: Union[Unset, None, DataInterval] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Optional[Union[Any, ProblemDetails, SampleSetsResponse, ValidationProblemDetails]]:
    """Fetch all of the Performance and Usage Data Sample Sets for a Server

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

        start (Union[Unset, None, datetime.datetime]): The start of the window of samples to
            retrieve, ISO8601 format (eg 2022-12-30T22:50:00Z). Defaults to 1 week before end for
            intervals larger than 5 minutes, or 1 day for 5 minute intervals.
        end (Union[Unset, None, datetime.datetime]): The start of the window of samples to
            retrieve, ISO8601 format (eg 2022-12-30T22:50:00Z). Defaults to 1 week or 1 day after
            start date depending on the selected data interval (or the current time if start is not
            provided). Can't be more than 1 year from start.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, SampleSetsResponse, ValidationProblemDetails]]
    """

    return (
        await asyncio_detailed(
            server_id=server_id,
            client=client,
            data_interval=data_interval,
            start=start,
            end=end,
            page=page,
            per_page=per_page,
        )
    ).parsed
