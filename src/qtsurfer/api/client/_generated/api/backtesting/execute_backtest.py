from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.accepted_job import AcceptedJob
from ...models.data_source_type import DataSourceType
from ...models.execute_backtest_body import ExecuteBacktestBody
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    exchange_id: str,
    type_: DataSourceType,
    *,
    body: ExecuteBacktestBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/backtest/{exchange_id}/{type_}/execute".format(
            exchange_id=quote(str(exchange_id), safe=""),
            type_=quote(str(type_), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AcceptedJob | ResponseError | None:
    if response.status_code == 202:
        response_202 = AcceptedJob.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ResponseError.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ResponseError.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ResponseError.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AcceptedJob | ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    exchange_id: str,
    type_: DataSourceType,
    *,
    client: AuthenticatedClient,
    body: ExecuteBacktestBody,
) -> Response[AcceptedJob | ResponseError]:
    """Execute a compiled strategy against a prepared dataset

     Enqueues an execute task that runs the strategy identified by `strategyId` over the data
    prepared by the prepare job identified by `prepareJobId`. The instrument and date range are
    recovered from the prepare job — they do not need to be sent again.

    Returns immediately with a `jobId`; poll `GET /backtest/{exchangeId}/{type}/execute/{jobId}`
    for the result.

    `type` must be a source that can be executed: `ticker` or `kline`. A `kline` strategy is fed
    bars of the cadence its `prepareJobId` was prepared at — chosen by you when preparing, not by
    the strategy. `funding` can be prepared but not executed yet: it is rejected with `400`
    before anything is queued.

    Optionally takes `params`: strategy properties for this one run, applied without
    recompiling. This is how a sweep leaderboard winner gets re-run for its `equityCurve` —
    a sweep row carries the ten ranking metrics but never a curve, whatever its size. Compile
    once, call this endpoint N times with different `params`, and each response is an ordinary
    backtest result with the curve included.

    The same request (same `prepareJobId`, `strategyId`, `storeSignals`, `equityCurve`,
    `baseConfig`, `params`) always returns the same `jobId` (idempotent) — a request that omits
    `equityCurve`, `baseConfig` or `params` dedupes exactly as it did before those fields
    existed. Two different `params` vectors over one prepare are two different jobs, and `9`
    and `9.0` are the same one.

    The re-run is an independent execution rather than a replay of the sweep trial — the two
    paths do not share a simulator — but they are pinned to agree: one vector run both ways
    matches on every leaderboard metric, asserted as a regression test. Treat a difference as a
    bug worth reporting, not as expected behaviour.

    Optionally takes `baseConfig`, the same `SweepBaseConfig` shape `executeSweep` accepts —
    `initialFunding`, `feeRate`, `percentAmountToLock`, etc. — so the same object can be reused
    against either endpoint. This endpoint has one effective fee rate rather than a sweep's
    independent buy/sell legs: a `baseConfig` that resolves to different buy/sell rates, or sets
    a non-default `feeLeg`, is rejected with `400` rather than silently collapsed to one side.

    Works unchanged for a dataset-backed prepare (`exchangeId: user`) — the request body is
    identical either way, since the instrument and range are recovered from `prepareJobId`.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting.

            * `ticker` — trades. Can be prepared, executed and swept.
            * `kline` — aggregated bars (candlesticks). Can be prepared, executed and swept. A run
            reads
              bars of the `cadence` the data was prepared at: you choose the bar width when you
            prepare,
              and the strategy does not fix it. See `PrepareRequest.cadence` for the accepted values.
            * `funding` — funding rates. Can be **prepared but not executed or swept yet**: a
            `funding`
              request to `execute` or `executeSweep` is rejected with `400` before anything is queued,
              and the message names the sources that can be run.
             Example: ticker.
        body (ExecuteBacktestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AcceptedJob | ResponseError]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        type_=type_,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    exchange_id: str,
    type_: DataSourceType,
    *,
    client: AuthenticatedClient,
    body: ExecuteBacktestBody,
) -> AcceptedJob | ResponseError | None:
    """Execute a compiled strategy against a prepared dataset

     Enqueues an execute task that runs the strategy identified by `strategyId` over the data
    prepared by the prepare job identified by `prepareJobId`. The instrument and date range are
    recovered from the prepare job — they do not need to be sent again.

    Returns immediately with a `jobId`; poll `GET /backtest/{exchangeId}/{type}/execute/{jobId}`
    for the result.

    `type` must be a source that can be executed: `ticker` or `kline`. A `kline` strategy is fed
    bars of the cadence its `prepareJobId` was prepared at — chosen by you when preparing, not by
    the strategy. `funding` can be prepared but not executed yet: it is rejected with `400`
    before anything is queued.

    Optionally takes `params`: strategy properties for this one run, applied without
    recompiling. This is how a sweep leaderboard winner gets re-run for its `equityCurve` —
    a sweep row carries the ten ranking metrics but never a curve, whatever its size. Compile
    once, call this endpoint N times with different `params`, and each response is an ordinary
    backtest result with the curve included.

    The same request (same `prepareJobId`, `strategyId`, `storeSignals`, `equityCurve`,
    `baseConfig`, `params`) always returns the same `jobId` (idempotent) — a request that omits
    `equityCurve`, `baseConfig` or `params` dedupes exactly as it did before those fields
    existed. Two different `params` vectors over one prepare are two different jobs, and `9`
    and `9.0` are the same one.

    The re-run is an independent execution rather than a replay of the sweep trial — the two
    paths do not share a simulator — but they are pinned to agree: one vector run both ways
    matches on every leaderboard metric, asserted as a regression test. Treat a difference as a
    bug worth reporting, not as expected behaviour.

    Optionally takes `baseConfig`, the same `SweepBaseConfig` shape `executeSweep` accepts —
    `initialFunding`, `feeRate`, `percentAmountToLock`, etc. — so the same object can be reused
    against either endpoint. This endpoint has one effective fee rate rather than a sweep's
    independent buy/sell legs: a `baseConfig` that resolves to different buy/sell rates, or sets
    a non-default `feeLeg`, is rejected with `400` rather than silently collapsed to one side.

    Works unchanged for a dataset-backed prepare (`exchangeId: user`) — the request body is
    identical either way, since the instrument and range are recovered from `prepareJobId`.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting.

            * `ticker` — trades. Can be prepared, executed and swept.
            * `kline` — aggregated bars (candlesticks). Can be prepared, executed and swept. A run
            reads
              bars of the `cadence` the data was prepared at: you choose the bar width when you
            prepare,
              and the strategy does not fix it. See `PrepareRequest.cadence` for the accepted values.
            * `funding` — funding rates. Can be **prepared but not executed or swept yet**: a
            `funding`
              request to `execute` or `executeSweep` is rejected with `400` before anything is queued,
              and the message names the sources that can be run.
             Example: ticker.
        body (ExecuteBacktestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AcceptedJob | ResponseError
    """

    return sync_detailed(
        exchange_id=exchange_id,
        type_=type_,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    exchange_id: str,
    type_: DataSourceType,
    *,
    client: AuthenticatedClient,
    body: ExecuteBacktestBody,
) -> Response[AcceptedJob | ResponseError]:
    """Execute a compiled strategy against a prepared dataset

     Enqueues an execute task that runs the strategy identified by `strategyId` over the data
    prepared by the prepare job identified by `prepareJobId`. The instrument and date range are
    recovered from the prepare job — they do not need to be sent again.

    Returns immediately with a `jobId`; poll `GET /backtest/{exchangeId}/{type}/execute/{jobId}`
    for the result.

    `type` must be a source that can be executed: `ticker` or `kline`. A `kline` strategy is fed
    bars of the cadence its `prepareJobId` was prepared at — chosen by you when preparing, not by
    the strategy. `funding` can be prepared but not executed yet: it is rejected with `400`
    before anything is queued.

    Optionally takes `params`: strategy properties for this one run, applied without
    recompiling. This is how a sweep leaderboard winner gets re-run for its `equityCurve` —
    a sweep row carries the ten ranking metrics but never a curve, whatever its size. Compile
    once, call this endpoint N times with different `params`, and each response is an ordinary
    backtest result with the curve included.

    The same request (same `prepareJobId`, `strategyId`, `storeSignals`, `equityCurve`,
    `baseConfig`, `params`) always returns the same `jobId` (idempotent) — a request that omits
    `equityCurve`, `baseConfig` or `params` dedupes exactly as it did before those fields
    existed. Two different `params` vectors over one prepare are two different jobs, and `9`
    and `9.0` are the same one.

    The re-run is an independent execution rather than a replay of the sweep trial — the two
    paths do not share a simulator — but they are pinned to agree: one vector run both ways
    matches on every leaderboard metric, asserted as a regression test. Treat a difference as a
    bug worth reporting, not as expected behaviour.

    Optionally takes `baseConfig`, the same `SweepBaseConfig` shape `executeSweep` accepts —
    `initialFunding`, `feeRate`, `percentAmountToLock`, etc. — so the same object can be reused
    against either endpoint. This endpoint has one effective fee rate rather than a sweep's
    independent buy/sell legs: a `baseConfig` that resolves to different buy/sell rates, or sets
    a non-default `feeLeg`, is rejected with `400` rather than silently collapsed to one side.

    Works unchanged for a dataset-backed prepare (`exchangeId: user`) — the request body is
    identical either way, since the instrument and range are recovered from `prepareJobId`.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting.

            * `ticker` — trades. Can be prepared, executed and swept.
            * `kline` — aggregated bars (candlesticks). Can be prepared, executed and swept. A run
            reads
              bars of the `cadence` the data was prepared at: you choose the bar width when you
            prepare,
              and the strategy does not fix it. See `PrepareRequest.cadence` for the accepted values.
            * `funding` — funding rates. Can be **prepared but not executed or swept yet**: a
            `funding`
              request to `execute` or `executeSweep` is rejected with `400` before anything is queued,
              and the message names the sources that can be run.
             Example: ticker.
        body (ExecuteBacktestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AcceptedJob | ResponseError]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        type_=type_,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    exchange_id: str,
    type_: DataSourceType,
    *,
    client: AuthenticatedClient,
    body: ExecuteBacktestBody,
) -> AcceptedJob | ResponseError | None:
    """Execute a compiled strategy against a prepared dataset

     Enqueues an execute task that runs the strategy identified by `strategyId` over the data
    prepared by the prepare job identified by `prepareJobId`. The instrument and date range are
    recovered from the prepare job — they do not need to be sent again.

    Returns immediately with a `jobId`; poll `GET /backtest/{exchangeId}/{type}/execute/{jobId}`
    for the result.

    `type` must be a source that can be executed: `ticker` or `kline`. A `kline` strategy is fed
    bars of the cadence its `prepareJobId` was prepared at — chosen by you when preparing, not by
    the strategy. `funding` can be prepared but not executed yet: it is rejected with `400`
    before anything is queued.

    Optionally takes `params`: strategy properties for this one run, applied without
    recompiling. This is how a sweep leaderboard winner gets re-run for its `equityCurve` —
    a sweep row carries the ten ranking metrics but never a curve, whatever its size. Compile
    once, call this endpoint N times with different `params`, and each response is an ordinary
    backtest result with the curve included.

    The same request (same `prepareJobId`, `strategyId`, `storeSignals`, `equityCurve`,
    `baseConfig`, `params`) always returns the same `jobId` (idempotent) — a request that omits
    `equityCurve`, `baseConfig` or `params` dedupes exactly as it did before those fields
    existed. Two different `params` vectors over one prepare are two different jobs, and `9`
    and `9.0` are the same one.

    The re-run is an independent execution rather than a replay of the sweep trial — the two
    paths do not share a simulator — but they are pinned to agree: one vector run both ways
    matches on every leaderboard metric, asserted as a regression test. Treat a difference as a
    bug worth reporting, not as expected behaviour.

    Optionally takes `baseConfig`, the same `SweepBaseConfig` shape `executeSweep` accepts —
    `initialFunding`, `feeRate`, `percentAmountToLock`, etc. — so the same object can be reused
    against either endpoint. This endpoint has one effective fee rate rather than a sweep's
    independent buy/sell legs: a `baseConfig` that resolves to different buy/sell rates, or sets
    a non-default `feeLeg`, is rejected with `400` rather than silently collapsed to one side.

    Works unchanged for a dataset-backed prepare (`exchangeId: user`) — the request body is
    identical either way, since the instrument and range are recovered from `prepareJobId`.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting.

            * `ticker` — trades. Can be prepared, executed and swept.
            * `kline` — aggregated bars (candlesticks). Can be prepared, executed and swept. A run
            reads
              bars of the `cadence` the data was prepared at: you choose the bar width when you
            prepare,
              and the strategy does not fix it. See `PrepareRequest.cadence` for the accepted values.
            * `funding` — funding rates. Can be **prepared but not executed or swept yet**: a
            `funding`
              request to `execute` or `executeSweep` is rejected with `400` before anything is queued,
              and the message names the sources that can be run.
             Example: ticker.
        body (ExecuteBacktestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AcceptedJob | ResponseError
    """

    return (
        await asyncio_detailed(
            exchange_id=exchange_id,
            type_=type_,
            client=client,
            body=body,
        )
    ).parsed
