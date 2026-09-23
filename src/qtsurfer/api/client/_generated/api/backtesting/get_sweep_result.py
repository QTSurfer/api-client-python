from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_source_type import DataSourceType
from ...models.execute_sweep_result import ExecuteSweepResult
from ...models.get_sweep_result_objective import GetSweepResultObjective
from ...models.get_sweep_result_order import GetSweepResultOrder
from ...models.get_sweep_result_ranking import GetSweepResultRanking
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    exchange_id: str,
    type_: DataSourceType,
    request_id: str,
    sweep_id: str,
    *,
    objective: GetSweepResultObjective | Unset = UNSET,
    order: GetSweepResultOrder | Unset = GetSweepResultOrder.RANKED,
    ranking: GetSweepResultRanking | Unset = GetSweepResultRanking.PLATEAU,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_objective: str | Unset = UNSET
    if not isinstance(objective, Unset):
        json_objective = objective.value

    params["objective"] = json_objective

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    json_ranking: str | Unset = UNSET
    if not isinstance(ranking, Unset):
        json_ranking = ranking.value

    params["ranking"] = json_ranking

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/backtest/{exchange_id}/{type_}/executeSweep/{request_id}/{sweep_id}".format(
            exchange_id=quote(str(exchange_id), safe=""),
            type_=quote(str(type_), safe=""),
            request_id=quote(str(request_id), safe=""),
            sweep_id=quote(str(sweep_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExecuteSweepResult | ResponseError | None:
    if response.status_code == 200:
        response_200 = ExecuteSweepResult.from_dict(response.json())

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
) -> Response[ExecuteSweepResult | ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    exchange_id: str,
    type_: DataSourceType,
    request_id: str,
    sweep_id: str,
    *,
    client: AuthenticatedClient,
    objective: GetSweepResultObjective | Unset = UNSET,
    order: GetSweepResultOrder | Unset = GetSweepResultOrder.RANKED,
    ranking: GetSweepResultRanking | Unset = GetSweepResultRanking.PLATEAU,
) -> Response[ExecuteSweepResult | ResponseError]:
    """Get sweep progress and results

     Returns incremental sweep progress. The default `ranked` view sorts and may truncate the
    display leaderboard. `order=natural` returns every available row, untruncated, ordered by
    deterministic `runIx`; use that view when materialising durable trial rows.

    The `ranked` view is ordered by **plateau score** by default, not by the raw objective. A
    plateau score is the objective of the worst run in a parameter point's immediate
    neighbourhood, so a point scores well only if the region around it also does — the highest
    raw score is frequently a spike that does not survive the parameters moving slightly. Pass
    `ranking=raw` for the unadjusted objective order.

    Rows in the `ranked` view carry `plateauScore` and `neighbourCount` when plateau ranking
    applied. Read them together: `neighbourCount: 0` means the point had no neighbours to
    compare against, so its plateau score is unevidenced rather than confirmed. Sweeps
    submitted before plateau ranking existed have no stored parameter grid to rebuild a
    neighbourhood from and are always ranked raw; the response's `ranking` field says which
    ordering was actually used.

    A sweep submitted with `walkForward` answers in a different shape, and the `walkForward`
    field on the response is what tells the two apart — it appears as soon as the sweep is
    accepted, before any fold has finished, so it is safe to branch on while polling. There
    the leaderboard is one row per completed fold: that fold's winner as it scored
    **out-of-sample**, with `runIx` carrying the fold index rather than a grid position. The
    in-sample runs behind those winners are not retained — they are an optimization's working
    set, and only the winner survives its fold. `ranking` is always `raw` and no plateau, DSR
    or PBO figure is reported: the out-of-sample scores are already the honest number, and
    layering a certification computed over F observations on top of them would overstate what
    was measured.

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
        request_id (str):
        sweep_id (str):
        objective (GetSweepResultObjective | Unset):
        order (GetSweepResultOrder | Unset):  Default: GetSweepResultOrder.RANKED.
        ranking (GetSweepResultRanking | Unset):  Default: GetSweepResultRanking.PLATEAU.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecuteSweepResult | ResponseError]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        type_=type_,
        request_id=request_id,
        sweep_id=sweep_id,
        objective=objective,
        order=order,
        ranking=ranking,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    exchange_id: str,
    type_: DataSourceType,
    request_id: str,
    sweep_id: str,
    *,
    client: AuthenticatedClient,
    objective: GetSweepResultObjective | Unset = UNSET,
    order: GetSweepResultOrder | Unset = GetSweepResultOrder.RANKED,
    ranking: GetSweepResultRanking | Unset = GetSweepResultRanking.PLATEAU,
) -> ExecuteSweepResult | ResponseError | None:
    """Get sweep progress and results

     Returns incremental sweep progress. The default `ranked` view sorts and may truncate the
    display leaderboard. `order=natural` returns every available row, untruncated, ordered by
    deterministic `runIx`; use that view when materialising durable trial rows.

    The `ranked` view is ordered by **plateau score** by default, not by the raw objective. A
    plateau score is the objective of the worst run in a parameter point's immediate
    neighbourhood, so a point scores well only if the region around it also does — the highest
    raw score is frequently a spike that does not survive the parameters moving slightly. Pass
    `ranking=raw` for the unadjusted objective order.

    Rows in the `ranked` view carry `plateauScore` and `neighbourCount` when plateau ranking
    applied. Read them together: `neighbourCount: 0` means the point had no neighbours to
    compare against, so its plateau score is unevidenced rather than confirmed. Sweeps
    submitted before plateau ranking existed have no stored parameter grid to rebuild a
    neighbourhood from and are always ranked raw; the response's `ranking` field says which
    ordering was actually used.

    A sweep submitted with `walkForward` answers in a different shape, and the `walkForward`
    field on the response is what tells the two apart — it appears as soon as the sweep is
    accepted, before any fold has finished, so it is safe to branch on while polling. There
    the leaderboard is one row per completed fold: that fold's winner as it scored
    **out-of-sample**, with `runIx` carrying the fold index rather than a grid position. The
    in-sample runs behind those winners are not retained — they are an optimization's working
    set, and only the winner survives its fold. `ranking` is always `raw` and no plateau, DSR
    or PBO figure is reported: the out-of-sample scores are already the honest number, and
    layering a certification computed over F observations on top of them would overstate what
    was measured.

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
        request_id (str):
        sweep_id (str):
        objective (GetSweepResultObjective | Unset):
        order (GetSweepResultOrder | Unset):  Default: GetSweepResultOrder.RANKED.
        ranking (GetSweepResultRanking | Unset):  Default: GetSweepResultRanking.PLATEAU.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecuteSweepResult | ResponseError
    """

    return sync_detailed(
        exchange_id=exchange_id,
        type_=type_,
        request_id=request_id,
        sweep_id=sweep_id,
        client=client,
        objective=objective,
        order=order,
        ranking=ranking,
    ).parsed


async def asyncio_detailed(
    exchange_id: str,
    type_: DataSourceType,
    request_id: str,
    sweep_id: str,
    *,
    client: AuthenticatedClient,
    objective: GetSweepResultObjective | Unset = UNSET,
    order: GetSweepResultOrder | Unset = GetSweepResultOrder.RANKED,
    ranking: GetSweepResultRanking | Unset = GetSweepResultRanking.PLATEAU,
) -> Response[ExecuteSweepResult | ResponseError]:
    """Get sweep progress and results

     Returns incremental sweep progress. The default `ranked` view sorts and may truncate the
    display leaderboard. `order=natural` returns every available row, untruncated, ordered by
    deterministic `runIx`; use that view when materialising durable trial rows.

    The `ranked` view is ordered by **plateau score** by default, not by the raw objective. A
    plateau score is the objective of the worst run in a parameter point's immediate
    neighbourhood, so a point scores well only if the region around it also does — the highest
    raw score is frequently a spike that does not survive the parameters moving slightly. Pass
    `ranking=raw` for the unadjusted objective order.

    Rows in the `ranked` view carry `plateauScore` and `neighbourCount` when plateau ranking
    applied. Read them together: `neighbourCount: 0` means the point had no neighbours to
    compare against, so its plateau score is unevidenced rather than confirmed. Sweeps
    submitted before plateau ranking existed have no stored parameter grid to rebuild a
    neighbourhood from and are always ranked raw; the response's `ranking` field says which
    ordering was actually used.

    A sweep submitted with `walkForward` answers in a different shape, and the `walkForward`
    field on the response is what tells the two apart — it appears as soon as the sweep is
    accepted, before any fold has finished, so it is safe to branch on while polling. There
    the leaderboard is one row per completed fold: that fold's winner as it scored
    **out-of-sample**, with `runIx` carrying the fold index rather than a grid position. The
    in-sample runs behind those winners are not retained — they are an optimization's working
    set, and only the winner survives its fold. `ranking` is always `raw` and no plateau, DSR
    or PBO figure is reported: the out-of-sample scores are already the honest number, and
    layering a certification computed over F observations on top of them would overstate what
    was measured.

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
        request_id (str):
        sweep_id (str):
        objective (GetSweepResultObjective | Unset):
        order (GetSweepResultOrder | Unset):  Default: GetSweepResultOrder.RANKED.
        ranking (GetSweepResultRanking | Unset):  Default: GetSweepResultRanking.PLATEAU.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecuteSweepResult | ResponseError]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        type_=type_,
        request_id=request_id,
        sweep_id=sweep_id,
        objective=objective,
        order=order,
        ranking=ranking,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    exchange_id: str,
    type_: DataSourceType,
    request_id: str,
    sweep_id: str,
    *,
    client: AuthenticatedClient,
    objective: GetSweepResultObjective | Unset = UNSET,
    order: GetSweepResultOrder | Unset = GetSweepResultOrder.RANKED,
    ranking: GetSweepResultRanking | Unset = GetSweepResultRanking.PLATEAU,
) -> ExecuteSweepResult | ResponseError | None:
    """Get sweep progress and results

     Returns incremental sweep progress. The default `ranked` view sorts and may truncate the
    display leaderboard. `order=natural` returns every available row, untruncated, ordered by
    deterministic `runIx`; use that view when materialising durable trial rows.

    The `ranked` view is ordered by **plateau score** by default, not by the raw objective. A
    plateau score is the objective of the worst run in a parameter point's immediate
    neighbourhood, so a point scores well only if the region around it also does — the highest
    raw score is frequently a spike that does not survive the parameters moving slightly. Pass
    `ranking=raw` for the unadjusted objective order.

    Rows in the `ranked` view carry `plateauScore` and `neighbourCount` when plateau ranking
    applied. Read them together: `neighbourCount: 0` means the point had no neighbours to
    compare against, so its plateau score is unevidenced rather than confirmed. Sweeps
    submitted before plateau ranking existed have no stored parameter grid to rebuild a
    neighbourhood from and are always ranked raw; the response's `ranking` field says which
    ordering was actually used.

    A sweep submitted with `walkForward` answers in a different shape, and the `walkForward`
    field on the response is what tells the two apart — it appears as soon as the sweep is
    accepted, before any fold has finished, so it is safe to branch on while polling. There
    the leaderboard is one row per completed fold: that fold's winner as it scored
    **out-of-sample**, with `runIx` carrying the fold index rather than a grid position. The
    in-sample runs behind those winners are not retained — they are an optimization's working
    set, and only the winner survives its fold. `ranking` is always `raw` and no plateau, DSR
    or PBO figure is reported: the out-of-sample scores are already the honest number, and
    layering a certification computed over F observations on top of them would overstate what
    was measured.

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
        request_id (str):
        sweep_id (str):
        objective (GetSweepResultObjective | Unset):
        order (GetSweepResultOrder | Unset):  Default: GetSweepResultOrder.RANKED.
        ranking (GetSweepResultRanking | Unset):  Default: GetSweepResultRanking.PLATEAU.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecuteSweepResult | ResponseError
    """

    return (
        await asyncio_detailed(
            exchange_id=exchange_id,
            type_=type_,
            request_id=request_id,
            sweep_id=sweep_id,
            client=client,
            objective=objective,
            order=order,
            ranking=ranking,
        )
    ).parsed
