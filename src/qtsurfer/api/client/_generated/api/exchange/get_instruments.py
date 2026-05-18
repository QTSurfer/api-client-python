from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.instrument_detail import InstrumentDetail
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    exchange_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/exchange/{exchange_id}/instruments".format(
            exchange_id=quote(str(exchange_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ResponseError | list[InstrumentDetail] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = InstrumentDetail.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 404:
        response_404 = ResponseError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ResponseError | list[InstrumentDetail]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    exchange_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ResponseError | list[InstrumentDetail]]:
    """Get a list of Instruments from a specific exchange

    Args:
        exchange_id (str):  Example: binance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError | list[InstrumentDetail]]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    exchange_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ResponseError | list[InstrumentDetail] | None:
    """Get a list of Instruments from a specific exchange

    Args:
        exchange_id (str):  Example: binance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError | list[InstrumentDetail]
    """

    return sync_detailed(
        exchange_id=exchange_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    exchange_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ResponseError | list[InstrumentDetail]]:
    """Get a list of Instruments from a specific exchange

    Args:
        exchange_id (str):  Example: binance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError | list[InstrumentDetail]]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    exchange_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ResponseError | list[InstrumentDetail] | None:
    """Get a list of Instruments from a specific exchange

    Args:
        exchange_id (str):  Example: binance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError | list[InstrumentDetail]
    """

    return (
        await asyncio_detailed(
            exchange_id=exchange_id,
            client=client,
        )
    ).parsed
