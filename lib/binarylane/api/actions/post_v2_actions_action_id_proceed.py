from __future__ import annotations

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from binarylane import errors
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.proceed_request import ProceedRequest
from binarylane.types import Response


def _get_kwargs(
    action_id: int,
    *,
    client: Client,
    json_body: ProceedRequest,
) -> Dict[str, Any]:
    url = "{}/v2/actions/{action_id}/proceed".format(client.base_url, action_id=action_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    action_id: int,
    *,
    client: Client,
    json_body: ProceedRequest,
) -> Response[Union[Any, ProblemDetails]]:
    """Respond to a UserInteractionRequired Action

    Args:
        action_id (int): The ID of the action for which this is a response.
        json_body (ProceedRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    action_id: int,
    *,
    client: Client,
    json_body: ProceedRequest,
) -> Optional[Union[Any, ProblemDetails]]:
    """Respond to a UserInteractionRequired Action

    Args:
        action_id (int): The ID of the action for which this is a response.
        json_body (ProceedRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    return sync_detailed(
        action_id=action_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    action_id: int,
    *,
    client: Client,
    json_body: ProceedRequest,
) -> Response[Union[Any, ProblemDetails]]:
    """Respond to a UserInteractionRequired Action

    Args:
        action_id (int): The ID of the action for which this is a response.
        json_body (ProceedRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    action_id: int,
    *,
    client: Client,
    json_body: ProceedRequest,
) -> Optional[Union[Any, ProblemDetails]]:
    """Respond to a UserInteractionRequired Action

    Args:
        action_id (int): The ID of the action for which this is a response.
        json_body (ProceedRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    return (
        await asyncio_detailed(
            action_id=action_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
