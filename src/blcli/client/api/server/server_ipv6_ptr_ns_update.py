from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.action import Action
from ...models.problem_details import ProblemDetails
from ...models.reverse_nameservers_request import ReverseNameserversRequest
from ...models.validation_problem_details import ValidationProblemDetails
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: ReverseNameserversRequest,
) -> Dict[str, Any]:
    url = "{}/v2/reverse_names/ipv6".format(client.base_url)

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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Action, Any, ProblemDetails, ValidationProblemDetails]]:
    if response.status_code == 200:
        response_200 = Action.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ValidationProblemDetails.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Action, Any, ProblemDetails, ValidationProblemDetails]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: ReverseNameserversRequest,
) -> Response[Union[Action, Any, ProblemDetails, ValidationProblemDetails]]:
    """Create New or Update Existing IPv6 Name Server Records

    Args:
        json_body (ReverseNameserversRequest):

    Returns:
        Response[Union[Action, Any, ProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: ReverseNameserversRequest,
) -> Optional[Union[Action, Any, ProblemDetails, ValidationProblemDetails]]:
    """Create New or Update Existing IPv6 Name Server Records

    Args:
        json_body (ReverseNameserversRequest):

    Returns:
        Response[Union[Action, Any, ProblemDetails, ValidationProblemDetails]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: ReverseNameserversRequest,
) -> Response[Union[Action, Any, ProblemDetails, ValidationProblemDetails]]:
    """Create New or Update Existing IPv6 Name Server Records

    Args:
        json_body (ReverseNameserversRequest):

    Returns:
        Response[Union[Action, Any, ProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: ReverseNameserversRequest,
) -> Optional[Union[Action, Any, ProblemDetails, ValidationProblemDetails]]:
    """Create New or Update Existing IPv6 Name Server Records

    Args:
        json_body (ReverseNameserversRequest):

    Returns:
        Response[Union[Action, Any, ProblemDetails, ValidationProblemDetails]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
