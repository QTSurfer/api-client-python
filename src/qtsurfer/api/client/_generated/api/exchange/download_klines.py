from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.download_klines_format import DownloadKlinesFormat
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    exchange_id: str,
    base: str,
    quote: str,
    *,
    hour: str,
    format_: DownloadKlinesFormat | Unset = DownloadKlinesFormat.LASTRA,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["hour"] = hour

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/exchange/{exchange_id}/klines/{base}/{quote}".format(
            exchange_id=quote(str(exchange_id), safe=""),
            base=quote(str(base), safe=""),
            quote=quote(str(quote), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ResponseError | None:
    if response.status_code == 400:
        response_400 = ResponseError.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ResponseError.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ResponseError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    exchange_id: str,
    base: str,
    quote: str,
    *,
    client: AuthenticatedClient | Client,
    hour: str,
    format_: DownloadKlinesFormat | Unset = DownloadKlinesFormat.LASTRA,
) -> Response[ResponseError]:
    """Download one hour of klines for an instrument as a Lastra segment

     Same shape and semantics as `/exchange/{exchangeId}/tickers/{base}/{quote}`,
    but serves klines (aggregated bars) instead of raw ticks. One
    [Lastra](https://github.com/QTSurfer/lastra-java) segment = one hour of
    klines at the exchange's native kline cadence, aligned to UTC.

    Klines use the same columnar layout as tickers — readers that handle one
    format read the other with the same code. Use this endpoint when a
    per-tick payload would be too large for the window of interest.

    Args:
        exchange_id (str):  Example: binance.
        base (str):  Example: BTC.
        quote (str):  Example: USDT.
        hour (str):  Example: 2026-01-15T10.
        format_ (DownloadKlinesFormat | Unset):  Default: DownloadKlinesFormat.LASTRA. Example:
            lastra.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        base=base,
        quote=quote,
        hour=hour,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    exchange_id: str,
    base: str,
    quote: str,
    *,
    client: AuthenticatedClient | Client,
    hour: str,
    format_: DownloadKlinesFormat | Unset = DownloadKlinesFormat.LASTRA,
) -> ResponseError | None:
    """Download one hour of klines for an instrument as a Lastra segment

     Same shape and semantics as `/exchange/{exchangeId}/tickers/{base}/{quote}`,
    but serves klines (aggregated bars) instead of raw ticks. One
    [Lastra](https://github.com/QTSurfer/lastra-java) segment = one hour of
    klines at the exchange's native kline cadence, aligned to UTC.

    Klines use the same columnar layout as tickers — readers that handle one
    format read the other with the same code. Use this endpoint when a
    per-tick payload would be too large for the window of interest.

    Args:
        exchange_id (str):  Example: binance.
        base (str):  Example: BTC.
        quote (str):  Example: USDT.
        hour (str):  Example: 2026-01-15T10.
        format_ (DownloadKlinesFormat | Unset):  Default: DownloadKlinesFormat.LASTRA. Example:
            lastra.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError
    """

    return sync_detailed(
        exchange_id=exchange_id,
        base=base,
        quote=quote,
        client=client,
        hour=hour,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    exchange_id: str,
    base: str,
    quote: str,
    *,
    client: AuthenticatedClient | Client,
    hour: str,
    format_: DownloadKlinesFormat | Unset = DownloadKlinesFormat.LASTRA,
) -> Response[ResponseError]:
    """Download one hour of klines for an instrument as a Lastra segment

     Same shape and semantics as `/exchange/{exchangeId}/tickers/{base}/{quote}`,
    but serves klines (aggregated bars) instead of raw ticks. One
    [Lastra](https://github.com/QTSurfer/lastra-java) segment = one hour of
    klines at the exchange's native kline cadence, aligned to UTC.

    Klines use the same columnar layout as tickers — readers that handle one
    format read the other with the same code. Use this endpoint when a
    per-tick payload would be too large for the window of interest.

    Args:
        exchange_id (str):  Example: binance.
        base (str):  Example: BTC.
        quote (str):  Example: USDT.
        hour (str):  Example: 2026-01-15T10.
        format_ (DownloadKlinesFormat | Unset):  Default: DownloadKlinesFormat.LASTRA. Example:
            lastra.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        base=base,
        quote=quote,
        hour=hour,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    exchange_id: str,
    base: str,
    quote: str,
    *,
    client: AuthenticatedClient | Client,
    hour: str,
    format_: DownloadKlinesFormat | Unset = DownloadKlinesFormat.LASTRA,
) -> ResponseError | None:
    """Download one hour of klines for an instrument as a Lastra segment

     Same shape and semantics as `/exchange/{exchangeId}/tickers/{base}/{quote}`,
    but serves klines (aggregated bars) instead of raw ticks. One
    [Lastra](https://github.com/QTSurfer/lastra-java) segment = one hour of
    klines at the exchange's native kline cadence, aligned to UTC.

    Klines use the same columnar layout as tickers — readers that handle one
    format read the other with the same code. Use this endpoint when a
    per-tick payload would be too large for the window of interest.

    Args:
        exchange_id (str):  Example: binance.
        base (str):  Example: BTC.
        quote (str):  Example: USDT.
        hour (str):  Example: 2026-01-15T10.
        format_ (DownloadKlinesFormat | Unset):  Default: DownloadKlinesFormat.LASTRA. Example:
            lastra.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError
    """

    return (
        await asyncio_detailed(
            exchange_id=exchange_id,
            base=base,
            quote=quote,
            client=client,
            hour=hour,
            format_=format_,
        )
    ).parsed
