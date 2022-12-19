from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.create_load_balancer_request import CreateLoadBalancerRequest
from ...models.create_load_balancer_response import CreateLoadBalancerResponse
from ...models.problem_details import ProblemDetails
from ...models.validation_problem_details import ValidationProblemDetails
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateLoadBalancerRequest,
) -> Dict[str, Any]:
    url = "{}/v2/load_balancers".format(client.base_url)

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
) -> Optional[Union[Any, CreateLoadBalancerResponse, ProblemDetails, ValidationProblemDetails]]:
    if response.status_code == 200:
        response_200 = CreateLoadBalancerResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ValidationProblemDetails.from_dict(response.json())

        return response_400
    if response.status_code == 422:
        response_422 = ProblemDetails.from_dict(response.json())

        return response_422
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, CreateLoadBalancerResponse, ProblemDetails, ValidationProblemDetails]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateLoadBalancerRequest,
) -> Response[Union[Any, CreateLoadBalancerResponse, ProblemDetails, ValidationProblemDetails]]:
    """Create a New Load Balancer

    Args:
        json_body (CreateLoadBalancerRequest):

    Returns:
        Response[Union[Any, CreateLoadBalancerResponse, ProblemDetails, ValidationProblemDetails]]
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
    json_body: CreateLoadBalancerRequest,
) -> Optional[Union[Any, CreateLoadBalancerResponse, ProblemDetails, ValidationProblemDetails]]:
    """Create a New Load Balancer

    Args:
        json_body (CreateLoadBalancerRequest):

    Returns:
        Response[Union[Any, CreateLoadBalancerResponse, ProblemDetails, ValidationProblemDetails]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateLoadBalancerRequest,
) -> Response[Union[Any, CreateLoadBalancerResponse, ProblemDetails, ValidationProblemDetails]]:
    """Create a New Load Balancer

    Args:
        json_body (CreateLoadBalancerRequest):

    Returns:
        Response[Union[Any, CreateLoadBalancerResponse, ProblemDetails, ValidationProblemDetails]]
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
    json_body: CreateLoadBalancerRequest,
) -> Optional[Union[Any, CreateLoadBalancerResponse, ProblemDetails, ValidationProblemDetails]]:
    """Create a New Load Balancer

    Args:
        json_body (CreateLoadBalancerRequest):

    Returns:
        Response[Union[Any, CreateLoadBalancerResponse, ProblemDetails, ValidationProblemDetails]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
