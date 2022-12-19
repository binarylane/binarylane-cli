from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.create_vpc_request import CreateVpcRequest
from ...models.validation_problem_details import ValidationProblemDetails
from ...models.vpc_response import VpcResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateVpcRequest,
) -> Dict[str, Any]:
    url = "{}/v2/vpcs".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ValidationProblemDetails, VpcResponse]]:
    if response.status_code == 200:
        response_200 = VpcResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ValidationProblemDetails.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ValidationProblemDetails, VpcResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateVpcRequest,
) -> Response[Union[Any, ValidationProblemDetails, VpcResponse]]:
    """Create a New VPC

    Args:
        json_body (CreateVpcRequest):

    Returns:
        Response[Union[Any, ValidationProblemDetails, VpcResponse]]
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
    json_body: CreateVpcRequest,
) -> Optional[Union[Any, ValidationProblemDetails, VpcResponse]]:
    """Create a New VPC

    Args:
        json_body (CreateVpcRequest):

    Returns:
        Response[Union[Any, ValidationProblemDetails, VpcResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateVpcRequest,
) -> Response[Union[Any, ValidationProblemDetails, VpcResponse]]:
    """Create a New VPC

    Args:
        json_body (CreateVpcRequest):

    Returns:
        Response[Union[Any, ValidationProblemDetails, VpcResponse]]
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
    json_body: CreateVpcRequest,
) -> Optional[Union[Any, ValidationProblemDetails, VpcResponse]]:
    """Create a New VPC

    Args:
        json_body (CreateVpcRequest):

    Returns:
        Response[Union[Any, ValidationProblemDetails, VpcResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
