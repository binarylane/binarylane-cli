from __future__ import annotations

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from binarylane import errors
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.resource_type import ResourceType
from binarylane.models.vpc_members_response import VpcMembersResponse
from binarylane.types import UNSET, Response, Unset


def _get_kwargs(
    vpc_id: int,
    *,
    client: Client,
    resource_type: Union[Unset, None, ResourceType] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Dict[str, Any]:
    url = "{}/v2/vpcs/{vpc_id}/members".format(client.base_url, vpc_id=vpc_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_resource_type: Union[Unset, None, str] = UNSET
    if not isinstance(resource_type, Unset):
        json_resource_type = resource_type.value if resource_type else None

    params["resource_type"] = json_resource_type

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
) -> Optional[Union[Any, ProblemDetails, VpcMembersResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = VpcMembersResponse.from_dict(response.json())

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
) -> Response[Union[Any, ProblemDetails, VpcMembersResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vpc_id: int,
    *,
    client: Client,
    resource_type: Union[Unset, None, ResourceType] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Response[Union[Any, ProblemDetails, VpcMembersResponse]]:
    """List All Members of an Existing VPC

     Only resource type 'server' is currently supported.

    Args:
        vpc_id (int): The target vpc id.
        resource_type (Union[Unset, None, ResourceType]):
            | Value | Description |
            | ----- | ----------- |
            | server | Server |
            | load-balancer | Load Balancer |
            | ssh-key | SSH Key |
            | vpc | Virtual Private Network |
            | image | Backup or Operating System Image |
            | registered-domain-name | Registered Domain Name |

        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, VpcMembersResponse]]
    """

    kwargs = _get_kwargs(
        vpc_id=vpc_id,
        client=client,
        resource_type=resource_type,
        page=page,
        per_page=per_page,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vpc_id: int,
    *,
    client: Client,
    resource_type: Union[Unset, None, ResourceType] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Optional[Union[Any, ProblemDetails, VpcMembersResponse]]:
    """List All Members of an Existing VPC

     Only resource type 'server' is currently supported.

    Args:
        vpc_id (int): The target vpc id.
        resource_type (Union[Unset, None, ResourceType]):
            | Value | Description |
            | ----- | ----------- |
            | server | Server |
            | load-balancer | Load Balancer |
            | ssh-key | SSH Key |
            | vpc | Virtual Private Network |
            | image | Backup or Operating System Image |
            | registered-domain-name | Registered Domain Name |

        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, VpcMembersResponse]]
    """

    return sync_detailed(
        vpc_id=vpc_id,
        client=client,
        resource_type=resource_type,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    vpc_id: int,
    *,
    client: Client,
    resource_type: Union[Unset, None, ResourceType] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Response[Union[Any, ProblemDetails, VpcMembersResponse]]:
    """List All Members of an Existing VPC

     Only resource type 'server' is currently supported.

    Args:
        vpc_id (int): The target vpc id.
        resource_type (Union[Unset, None, ResourceType]):
            | Value | Description |
            | ----- | ----------- |
            | server | Server |
            | load-balancer | Load Balancer |
            | ssh-key | SSH Key |
            | vpc | Virtual Private Network |
            | image | Backup or Operating System Image |
            | registered-domain-name | Registered Domain Name |

        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, VpcMembersResponse]]
    """

    kwargs = _get_kwargs(
        vpc_id=vpc_id,
        client=client,
        resource_type=resource_type,
        page=page,
        per_page=per_page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vpc_id: int,
    *,
    client: Client,
    resource_type: Union[Unset, None, ResourceType] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Optional[Union[Any, ProblemDetails, VpcMembersResponse]]:
    """List All Members of an Existing VPC

     Only resource type 'server' is currently supported.

    Args:
        vpc_id (int): The target vpc id.
        resource_type (Union[Unset, None, ResourceType]):
            | Value | Description |
            | ----- | ----------- |
            | server | Server |
            | load-balancer | Load Balancer |
            | ssh-key | SSH Key |
            | vpc | Virtual Private Network |
            | image | Backup or Operating System Image |
            | registered-domain-name | Registered Domain Name |

        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, VpcMembersResponse]]
    """

    return (
        await asyncio_detailed(
            vpc_id=vpc_id,
            client=client,
            resource_type=resource_type,
            page=page,
            per_page=per_page,
        )
    ).parsed
