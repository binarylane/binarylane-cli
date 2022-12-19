from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.invoice_response import InvoiceResponse
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    invoice_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v2/customers/my/invoices/{invoice_id}".format(client.base_url, invoice_id=invoice_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, InvoiceResponse, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = InvoiceResponse.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, InvoiceResponse, ProblemDetails]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    invoice_id: int,
    *,
    client: Client,
) -> Response[Union[Any, InvoiceResponse, ProblemDetails]]:
    """Fetch an Invoice

    Args:
        invoice_id (int):

    Returns:
        Response[Union[Any, InvoiceResponse, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    invoice_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, InvoiceResponse, ProblemDetails]]:
    """Fetch an Invoice

    Args:
        invoice_id (int):

    Returns:
        Response[Union[Any, InvoiceResponse, ProblemDetails]]
    """

    return sync_detailed(
        invoice_id=invoice_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    invoice_id: int,
    *,
    client: Client,
) -> Response[Union[Any, InvoiceResponse, ProblemDetails]]:
    """Fetch an Invoice

    Args:
        invoice_id (int):

    Returns:
        Response[Union[Any, InvoiceResponse, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    invoice_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, InvoiceResponse, ProblemDetails]]:
    """Fetch an Invoice

    Args:
        invoice_id (int):

    Returns:
        Response[Union[Any, InvoiceResponse, ProblemDetails]]
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
        )
    ).parsed
