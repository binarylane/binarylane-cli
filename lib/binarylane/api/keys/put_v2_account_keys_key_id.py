from __future__ import annotations

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from binarylane import errors
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.ssh_key_response import SshKeyResponse
from binarylane.models.update_ssh_key_request import UpdateSshKeyRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Response


def _get_kwargs(
    key_id: str,
    *,
    client: Client,
    json_body: UpdateSshKeyRequest,
) -> Dict[str, Any]:
    url = "{}/v2/account/keys/{key_id}".format(client.base_url, key_id=key_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ProblemDetails, SshKeyResponse, ValidationProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SshKeyResponse.from_dict(response.json())

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
) -> Response[Union[Any, ProblemDetails, SshKeyResponse, ValidationProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key_id: str,
    *,
    client: Client,
    json_body: UpdateSshKeyRequest,
) -> Response[Union[Any, ProblemDetails, SshKeyResponse, ValidationProblemDetails]]:
    """Update an Existing SSH Key

     The key_id may be either the Id or the key fingerprint.

    Args:
        key_id (str): The ID or fingerprint of the SSH Key to update.
        json_body (UpdateSshKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, SshKeyResponse, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key_id: str,
    *,
    client: Client,
    json_body: UpdateSshKeyRequest,
) -> Optional[Union[Any, ProblemDetails, SshKeyResponse, ValidationProblemDetails]]:
    """Update an Existing SSH Key

     The key_id may be either the Id or the key fingerprint.

    Args:
        key_id (str): The ID or fingerprint of the SSH Key to update.
        json_body (UpdateSshKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, SshKeyResponse, ValidationProblemDetails]]
    """

    return sync_detailed(
        key_id=key_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    key_id: str,
    *,
    client: Client,
    json_body: UpdateSshKeyRequest,
) -> Response[Union[Any, ProblemDetails, SshKeyResponse, ValidationProblemDetails]]:
    """Update an Existing SSH Key

     The key_id may be either the Id or the key fingerprint.

    Args:
        key_id (str): The ID or fingerprint of the SSH Key to update.
        json_body (UpdateSshKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, SshKeyResponse, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key_id: str,
    *,
    client: Client,
    json_body: UpdateSshKeyRequest,
) -> Optional[Union[Any, ProblemDetails, SshKeyResponse, ValidationProblemDetails]]:
    """Update an Existing SSH Key

     The key_id may be either the Id or the key fingerprint.

    Args:
        key_id (str): The ID or fingerprint of the SSH Key to update.
        json_body (UpdateSshKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, SshKeyResponse, ValidationProblemDetails]]
    """

    return (
        await asyncio_detailed(
            key_id=key_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
