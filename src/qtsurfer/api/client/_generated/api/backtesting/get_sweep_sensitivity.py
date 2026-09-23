from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_source_type import DataSourceType
from ...models.get_sweep_sensitivity_objective import GetSweepSensitivityObjective
from ...models.response_error import ResponseError
from ...models.sweep_sensitivity import SweepSensitivity
from ...types import UNSET, Response, Unset


def _get_kwargs(
    exchange_id: str,
    type_: DataSourceType,
    request_id: str,
    sweep_id: str,
    *,
    objective: GetSweepSensitivityObjective | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_objective: str | Unset = UNSET
    if not isinstance(objective, Unset):
        json_objective = objective.value

    params["objective"] = json_objective

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/backtest/{exchange_id}/{type_}/executeSweep/{request_id}/{sweep_id}/sensitivity".format(
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
) -> ResponseError | SweepSensitivity | None:
    if response.status_code == 200:
        response_200 = SweepSensitivity.from_dict(response.json())

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
) -> Response[ResponseError | SweepSensitivity]:
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
    objective: GetSweepSensitivityObjective | Unset = UNSET,
) -> Response[ResponseError | SweepSensitivity]:
    """Get sweep sensitivity surfaces

     How the objective moves as each parameter moves — the question a leaderboard cannot answer.
    A leaderboard says which point won; a sweep can spend its entire budget on an axis that
    never moved the objective at all, and showing only the top rows hides that completely.

    A **marginal** takes one axis and collapses every other one: for each value of that axis,
    it aggregates every run that used it, whatever the rest of the parameters were. A flat
    marginal means the axis is irrelevant over the range swept. `best`, `mean` and `worst` are
    all reported because them disagreeing is itself the signal — a value with a high `best` and
    a poor `mean` works only in specific company, which is an interaction between parameters
    and would be invisible behind a single number.

    A **heatmap** does the same over a pair of axes, where that interaction becomes visible
    directly.

    Served from the sweep's stored rows: no re-run, no engine call, and it works on a sweep
    still in flight — the aggregates then describe the runs finished so far. Aborted runs are
    excluded throughout, since a run that threw measured nothing and counting it as a bad
    outcome would invent evidence against a parameter value that was never really tested.

    This is a separate endpoint rather than extra fields on the result view because the
    two-dimensional half is quadratic in the axis count (N axes give N(N-1)/2 surfaces, each
    the product of two axes' value counts) and is not wanted on the poll that drives progress.

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
        objective (GetSweepSensitivityObjective | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError | SweepSensitivity]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        type_=type_,
        request_id=request_id,
        sweep_id=sweep_id,
        objective=objective,
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
    objective: GetSweepSensitivityObjective | Unset = UNSET,
) -> ResponseError | SweepSensitivity | None:
    """Get sweep sensitivity surfaces

     How the objective moves as each parameter moves — the question a leaderboard cannot answer.
    A leaderboard says which point won; a sweep can spend its entire budget on an axis that
    never moved the objective at all, and showing only the top rows hides that completely.

    A **marginal** takes one axis and collapses every other one: for each value of that axis,
    it aggregates every run that used it, whatever the rest of the parameters were. A flat
    marginal means the axis is irrelevant over the range swept. `best`, `mean` and `worst` are
    all reported because them disagreeing is itself the signal — a value with a high `best` and
    a poor `mean` works only in specific company, which is an interaction between parameters
    and would be invisible behind a single number.

    A **heatmap** does the same over a pair of axes, where that interaction becomes visible
    directly.

    Served from the sweep's stored rows: no re-run, no engine call, and it works on a sweep
    still in flight — the aggregates then describe the runs finished so far. Aborted runs are
    excluded throughout, since a run that threw measured nothing and counting it as a bad
    outcome would invent evidence against a parameter value that was never really tested.

    This is a separate endpoint rather than extra fields on the result view because the
    two-dimensional half is quadratic in the axis count (N axes give N(N-1)/2 surfaces, each
    the product of two axes' value counts) and is not wanted on the poll that drives progress.

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
        objective (GetSweepSensitivityObjective | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError | SweepSensitivity
    """

    return sync_detailed(
        exchange_id=exchange_id,
        type_=type_,
        request_id=request_id,
        sweep_id=sweep_id,
        client=client,
        objective=objective,
    ).parsed


async def asyncio_detailed(
    exchange_id: str,
    type_: DataSourceType,
    request_id: str,
    sweep_id: str,
    *,
    client: AuthenticatedClient,
    objective: GetSweepSensitivityObjective | Unset = UNSET,
) -> Response[ResponseError | SweepSensitivity]:
    """Get sweep sensitivity surfaces

     How the objective moves as each parameter moves — the question a leaderboard cannot answer.
    A leaderboard says which point won; a sweep can spend its entire budget on an axis that
    never moved the objective at all, and showing only the top rows hides that completely.

    A **marginal** takes one axis and collapses every other one: for each value of that axis,
    it aggregates every run that used it, whatever the rest of the parameters were. A flat
    marginal means the axis is irrelevant over the range swept. `best`, `mean` and `worst` are
    all reported because them disagreeing is itself the signal — a value with a high `best` and
    a poor `mean` works only in specific company, which is an interaction between parameters
    and would be invisible behind a single number.

    A **heatmap** does the same over a pair of axes, where that interaction becomes visible
    directly.

    Served from the sweep's stored rows: no re-run, no engine call, and it works on a sweep
    still in flight — the aggregates then describe the runs finished so far. Aborted runs are
    excluded throughout, since a run that threw measured nothing and counting it as a bad
    outcome would invent evidence against a parameter value that was never really tested.

    This is a separate endpoint rather than extra fields on the result view because the
    two-dimensional half is quadratic in the axis count (N axes give N(N-1)/2 surfaces, each
    the product of two axes' value counts) and is not wanted on the poll that drives progress.

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
        objective (GetSweepSensitivityObjective | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError | SweepSensitivity]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        type_=type_,
        request_id=request_id,
        sweep_id=sweep_id,
        objective=objective,
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
    objective: GetSweepSensitivityObjective | Unset = UNSET,
) -> ResponseError | SweepSensitivity | None:
    """Get sweep sensitivity surfaces

     How the objective moves as each parameter moves — the question a leaderboard cannot answer.
    A leaderboard says which point won; a sweep can spend its entire budget on an axis that
    never moved the objective at all, and showing only the top rows hides that completely.

    A **marginal** takes one axis and collapses every other one: for each value of that axis,
    it aggregates every run that used it, whatever the rest of the parameters were. A flat
    marginal means the axis is irrelevant over the range swept. `best`, `mean` and `worst` are
    all reported because them disagreeing is itself the signal — a value with a high `best` and
    a poor `mean` works only in specific company, which is an interaction between parameters
    and would be invisible behind a single number.

    A **heatmap** does the same over a pair of axes, where that interaction becomes visible
    directly.

    Served from the sweep's stored rows: no re-run, no engine call, and it works on a sweep
    still in flight — the aggregates then describe the runs finished so far. Aborted runs are
    excluded throughout, since a run that threw measured nothing and counting it as a bad
    outcome would invent evidence against a parameter value that was never really tested.

    This is a separate endpoint rather than extra fields on the result view because the
    two-dimensional half is quadratic in the axis count (N axes give N(N-1)/2 surfaces, each
    the product of two axes' value counts) and is not wanted on the poll that drives progress.

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
        objective (GetSweepSensitivityObjective | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError | SweepSensitivity
    """

    return (
        await asyncio_detailed(
            exchange_id=exchange_id,
            type_=type_,
            request_id=request_id,
            sweep_id=sweep_id,
            client=client,
            objective=objective,
        )
    ).parsed
