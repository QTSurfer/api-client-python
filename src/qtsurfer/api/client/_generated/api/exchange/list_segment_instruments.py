from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.instrument_list_response import InstrumentListResponse
from ...models.list_segment_instruments_segment import ListSegmentInstrumentsSegment
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    exchange_id: str,
    segment: ListSegmentInstrumentsSegment,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/exchange/{exchange_id}/{segment}/instruments".format(
            exchange_id=quote(str(exchange_id), safe=""),
            segment=quote(str(segment), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InstrumentListResponse | ResponseError | None:
    if response.status_code == 200:
        response_200 = InstrumentListResponse.from_dict(response.json())

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
) -> Response[InstrumentListResponse | ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    exchange_id: str,
    segment: ListSegmentInstrumentsSegment,
    *,
    client: AuthenticatedClient | Client,
) -> Response[InstrumentListResponse | ResponseError]:
    """List an exchange segment's instruments

     Returns the instruments for one market segment of the exchange, each with
    per-data-type coverage and market info. HAL `_links` carry `self` plus the
    `spot` / `futures` segment-discovery links; the default-segment shortcut is
    `GET /exchange/{exchangeId}/instruments` (spot).

    Args:
        exchange_id (str):  Example: binance.
        segment (ListSegmentInstrumentsSegment):  Example: spot.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstrumentListResponse | ResponseError]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        segment=segment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    exchange_id: str,
    segment: ListSegmentInstrumentsSegment,
    *,
    client: AuthenticatedClient | Client,
) -> InstrumentListResponse | ResponseError | None:
    """List an exchange segment's instruments

     Returns the instruments for one market segment of the exchange, each with
    per-data-type coverage and market info. HAL `_links` carry `self` plus the
    `spot` / `futures` segment-discovery links; the default-segment shortcut is
    `GET /exchange/{exchangeId}/instruments` (spot).

    Args:
        exchange_id (str):  Example: binance.
        segment (ListSegmentInstrumentsSegment):  Example: spot.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstrumentListResponse | ResponseError
    """

    return sync_detailed(
        exchange_id=exchange_id,
        segment=segment,
        client=client,
    ).parsed


async def asyncio_detailed(
    exchange_id: str,
    segment: ListSegmentInstrumentsSegment,
    *,
    client: AuthenticatedClient | Client,
) -> Response[InstrumentListResponse | ResponseError]:
    """List an exchange segment's instruments

     Returns the instruments for one market segment of the exchange, each with
    per-data-type coverage and market info. HAL `_links` carry `self` plus the
    `spot` / `futures` segment-discovery links; the default-segment shortcut is
    `GET /exchange/{exchangeId}/instruments` (spot).

    Args:
        exchange_id (str):  Example: binance.
        segment (ListSegmentInstrumentsSegment):  Example: spot.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstrumentListResponse | ResponseError]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        segment=segment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    exchange_id: str,
    segment: ListSegmentInstrumentsSegment,
    *,
    client: AuthenticatedClient | Client,
) -> InstrumentListResponse | ResponseError | None:
    """List an exchange segment's instruments

     Returns the instruments for one market segment of the exchange, each with
    per-data-type coverage and market info. HAL `_links` carry `self` plus the
    `spot` / `futures` segment-discovery links; the default-segment shortcut is
    `GET /exchange/{exchangeId}/instruments` (spot).

    Args:
        exchange_id (str):  Example: binance.
        segment (ListSegmentInstrumentsSegment):  Example: spot.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstrumentListResponse | ResponseError
    """

    return (
        await asyncio_detailed(
            exchange_id=exchange_id,
            segment=segment,
            client=client,
        )
    ).parsed
