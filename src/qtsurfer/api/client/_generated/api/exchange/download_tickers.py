from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.download_tickers_format import DownloadTickersFormat
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    exchange_id: str,
    base: str,
    quote: str,
    *,
    hour: str,
    format_: DownloadTickersFormat | Unset = DownloadTickersFormat.LASTRA,
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
        "url": "/exchange/{exchange_id}/tickers/{base}/{quote}".format(
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
    format_: DownloadTickersFormat | Unset = DownloadTickersFormat.LASTRA,
) -> Response[ResponseError]:
    """Download one hour of tickers for an instrument as a Lastra segment

     Serves exactly one hour of raw ticker data for the given instrument on the
    requested exchange. The payload is a native [Lastra](https://github.com/QTSurfer/lastra-java)
    file — QTSurfer's columnar format for tick-precision timeseries — with
    no JSON envelope.

    One segment = one hour, aligned to UTC. The `hour` query parameter selects
    the segment and must match `YYYY-MM-DDTHH` (no minutes/seconds, no timezone
    suffix). Example: `hour=2026-01-15T10` returns `h10.lastra` for
    2026-01-15, covering `[10:00:00Z, 11:00:00Z)`. Hours not yet available
    return `404`.

    A `format=parquet` query parameter switches the response to on-the-fly
    Parquet conversion via [lastra-convert](https://github.com/QTSurfer/lastra-convert)
    for clients that don't yet read Lastra. Lastra is the primary format
    and cheaper when the client can consume it.

    Clients:
    - [lastra-java](https://github.com/QTSurfer/lastra-java) — reference
      Java reader/writer with per-column codecs (ALP, Gorilla, delta-varint,
      ZSTD) and CRC32 integrity.
    - [lastra-ts](https://github.com/QTSurfer/lastra-ts) — TypeScript reader
      (~4 kB bundle, browser + Node.js).
    - [duckdb-lastra](https://github.com/QTSurfer/duckdb-lastra) — DuckDB
      extension for ad-hoc SQL over Lastra files.
    - [lastra-convert](https://github.com/QTSurfer/lastra-convert) — CLI + Java
      API for converting to/from Parquet, Reef, and CSV.
    - `curl -OJ` for offline dumps (the `Content-Disposition` header sets a
      descriptive filename).

    Args:
        exchange_id (str):  Example: binance.
        base (str):  Example: BTC.
        quote (str):  Example: USDT.
        hour (str):  Example: 2026-01-15T10.
        format_ (DownloadTickersFormat | Unset):  Default: DownloadTickersFormat.LASTRA. Example:
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
    format_: DownloadTickersFormat | Unset = DownloadTickersFormat.LASTRA,
) -> ResponseError | None:
    """Download one hour of tickers for an instrument as a Lastra segment

     Serves exactly one hour of raw ticker data for the given instrument on the
    requested exchange. The payload is a native [Lastra](https://github.com/QTSurfer/lastra-java)
    file — QTSurfer's columnar format for tick-precision timeseries — with
    no JSON envelope.

    One segment = one hour, aligned to UTC. The `hour` query parameter selects
    the segment and must match `YYYY-MM-DDTHH` (no minutes/seconds, no timezone
    suffix). Example: `hour=2026-01-15T10` returns `h10.lastra` for
    2026-01-15, covering `[10:00:00Z, 11:00:00Z)`. Hours not yet available
    return `404`.

    A `format=parquet` query parameter switches the response to on-the-fly
    Parquet conversion via [lastra-convert](https://github.com/QTSurfer/lastra-convert)
    for clients that don't yet read Lastra. Lastra is the primary format
    and cheaper when the client can consume it.

    Clients:
    - [lastra-java](https://github.com/QTSurfer/lastra-java) — reference
      Java reader/writer with per-column codecs (ALP, Gorilla, delta-varint,
      ZSTD) and CRC32 integrity.
    - [lastra-ts](https://github.com/QTSurfer/lastra-ts) — TypeScript reader
      (~4 kB bundle, browser + Node.js).
    - [duckdb-lastra](https://github.com/QTSurfer/duckdb-lastra) — DuckDB
      extension for ad-hoc SQL over Lastra files.
    - [lastra-convert](https://github.com/QTSurfer/lastra-convert) — CLI + Java
      API for converting to/from Parquet, Reef, and CSV.
    - `curl -OJ` for offline dumps (the `Content-Disposition` header sets a
      descriptive filename).

    Args:
        exchange_id (str):  Example: binance.
        base (str):  Example: BTC.
        quote (str):  Example: USDT.
        hour (str):  Example: 2026-01-15T10.
        format_ (DownloadTickersFormat | Unset):  Default: DownloadTickersFormat.LASTRA. Example:
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
    format_: DownloadTickersFormat | Unset = DownloadTickersFormat.LASTRA,
) -> Response[ResponseError]:
    """Download one hour of tickers for an instrument as a Lastra segment

     Serves exactly one hour of raw ticker data for the given instrument on the
    requested exchange. The payload is a native [Lastra](https://github.com/QTSurfer/lastra-java)
    file — QTSurfer's columnar format for tick-precision timeseries — with
    no JSON envelope.

    One segment = one hour, aligned to UTC. The `hour` query parameter selects
    the segment and must match `YYYY-MM-DDTHH` (no minutes/seconds, no timezone
    suffix). Example: `hour=2026-01-15T10` returns `h10.lastra` for
    2026-01-15, covering `[10:00:00Z, 11:00:00Z)`. Hours not yet available
    return `404`.

    A `format=parquet` query parameter switches the response to on-the-fly
    Parquet conversion via [lastra-convert](https://github.com/QTSurfer/lastra-convert)
    for clients that don't yet read Lastra. Lastra is the primary format
    and cheaper when the client can consume it.

    Clients:
    - [lastra-java](https://github.com/QTSurfer/lastra-java) — reference
      Java reader/writer with per-column codecs (ALP, Gorilla, delta-varint,
      ZSTD) and CRC32 integrity.
    - [lastra-ts](https://github.com/QTSurfer/lastra-ts) — TypeScript reader
      (~4 kB bundle, browser + Node.js).
    - [duckdb-lastra](https://github.com/QTSurfer/duckdb-lastra) — DuckDB
      extension for ad-hoc SQL over Lastra files.
    - [lastra-convert](https://github.com/QTSurfer/lastra-convert) — CLI + Java
      API for converting to/from Parquet, Reef, and CSV.
    - `curl -OJ` for offline dumps (the `Content-Disposition` header sets a
      descriptive filename).

    Args:
        exchange_id (str):  Example: binance.
        base (str):  Example: BTC.
        quote (str):  Example: USDT.
        hour (str):  Example: 2026-01-15T10.
        format_ (DownloadTickersFormat | Unset):  Default: DownloadTickersFormat.LASTRA. Example:
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
    format_: DownloadTickersFormat | Unset = DownloadTickersFormat.LASTRA,
) -> ResponseError | None:
    """Download one hour of tickers for an instrument as a Lastra segment

     Serves exactly one hour of raw ticker data for the given instrument on the
    requested exchange. The payload is a native [Lastra](https://github.com/QTSurfer/lastra-java)
    file — QTSurfer's columnar format for tick-precision timeseries — with
    no JSON envelope.

    One segment = one hour, aligned to UTC. The `hour` query parameter selects
    the segment and must match `YYYY-MM-DDTHH` (no minutes/seconds, no timezone
    suffix). Example: `hour=2026-01-15T10` returns `h10.lastra` for
    2026-01-15, covering `[10:00:00Z, 11:00:00Z)`. Hours not yet available
    return `404`.

    A `format=parquet` query parameter switches the response to on-the-fly
    Parquet conversion via [lastra-convert](https://github.com/QTSurfer/lastra-convert)
    for clients that don't yet read Lastra. Lastra is the primary format
    and cheaper when the client can consume it.

    Clients:
    - [lastra-java](https://github.com/QTSurfer/lastra-java) — reference
      Java reader/writer with per-column codecs (ALP, Gorilla, delta-varint,
      ZSTD) and CRC32 integrity.
    - [lastra-ts](https://github.com/QTSurfer/lastra-ts) — TypeScript reader
      (~4 kB bundle, browser + Node.js).
    - [duckdb-lastra](https://github.com/QTSurfer/duckdb-lastra) — DuckDB
      extension for ad-hoc SQL over Lastra files.
    - [lastra-convert](https://github.com/QTSurfer/lastra-convert) — CLI + Java
      API for converting to/from Parquet, Reef, and CSV.
    - `curl -OJ` for offline dumps (the `Content-Disposition` header sets a
      descriptive filename).

    Args:
        exchange_id (str):  Example: binance.
        base (str):  Example: BTC.
        quote (str):  Example: USDT.
        hour (str):  Example: 2026-01-15T10.
        format_ (DownloadTickersFormat | Unset):  Default: DownloadTickersFormat.LASTRA. Example:
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
