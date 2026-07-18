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
) -> Response[ExecuteSweepResult | ResponseError]:
    """Get sweep progress and results

     Returns incremental sweep progress. The default `ranked` view sorts and may truncate the
    display leaderboard. `order=natural` returns every available row, untruncated, ordered by
    deterministic `runIx`; use that view when materialising durable trial rows.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        request_id (str):
        sweep_id (str):
        objective (GetSweepResultObjective | Unset):
        order (GetSweepResultOrder | Unset):  Default: GetSweepResultOrder.RANKED.

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
) -> ExecuteSweepResult | ResponseError | None:
    """Get sweep progress and results

     Returns incremental sweep progress. The default `ranked` view sorts and may truncate the
    display leaderboard. `order=natural` returns every available row, untruncated, ordered by
    deterministic `runIx`; use that view when materialising durable trial rows.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        request_id (str):
        sweep_id (str):
        objective (GetSweepResultObjective | Unset):
        order (GetSweepResultOrder | Unset):  Default: GetSweepResultOrder.RANKED.

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
) -> Response[ExecuteSweepResult | ResponseError]:
    """Get sweep progress and results

     Returns incremental sweep progress. The default `ranked` view sorts and may truncate the
    display leaderboard. `order=natural` returns every available row, untruncated, ordered by
    deterministic `runIx`; use that view when materialising durable trial rows.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        request_id (str):
        sweep_id (str):
        objective (GetSweepResultObjective | Unset):
        order (GetSweepResultOrder | Unset):  Default: GetSweepResultOrder.RANKED.

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
) -> ExecuteSweepResult | ResponseError | None:
    """Get sweep progress and results

     Returns incremental sweep progress. The default `ranked` view sorts and may truncate the
    display leaderboard. `order=natural` returns every available row, untruncated, ordered by
    deterministic `runIx`; use that view when materialising durable trial rows.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        request_id (str):
        sweep_id (str):
        objective (GetSweepResultObjective | Unset):
        order (GetSweepResultOrder | Unset):  Default: GetSweepResultOrder.RANKED.

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
        )
    ).parsed
