from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_source_type import DataSourceType
from ...models.execute_sweep_accepted import ExecuteSweepAccepted
from ...models.execute_sweep_request import ExecuteSweepRequest
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    exchange_id: str,
    type_: DataSourceType,
    request_id: str,
    *,
    body: ExecuteSweepRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/backtest/{exchange_id}/{type_}/executeSweep/{request_id}".format(
            exchange_id=quote(str(exchange_id), safe=""),
            type_=quote(str(type_), safe=""),
            request_id=quote(str(request_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExecuteSweepAccepted | ResponseError | None:
    if response.status_code == 202:
        response_202 = ExecuteSweepAccepted.from_dict(response.json())

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
) -> Response[ExecuteSweepAccepted | ResponseError]:
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
    *,
    client: AuthenticatedClient,
    body: ExecuteSweepRequest,
) -> Response[ExecuteSweepAccepted | ResponseError]:
    r"""Execute a parameter sweep over prepared data

     Runs a parameter matrix over the single immutable dataset identified by `requestId`.
    The backend expands and executes the matrix internally; clients poll the returned
    `sweepId` for incremental results.

    Supplying `walkForward` runs the sweep in a different mode entirely. Instead of scoring
    every parameter vector once over the whole range, the data is split into F sequential
    folds; each fold optimizes the full grid on its own window and then scores only its winner
    on the window immediately after — data that winner was not chosen on. It answers a harder
    question than a leaderboard: not \"which parameters won\", but \"does re-optimizing this
    periodically actually work\". Omit the block and nothing changes, including the response.

    The cost is the reason it is opt-in rather than always on: F folds × N vectors, so a
    4-fold run over a 500-point grid is 2004 backtests where the plain sweep is 500. The
    request is rejected when `folds × totalRuns` exceeds the server's sweep budget.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        request_id (str):
        body (ExecuteSweepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecuteSweepAccepted | ResponseError]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        type_=type_,
        request_id=request_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    exchange_id: str,
    type_: DataSourceType,
    request_id: str,
    *,
    client: AuthenticatedClient,
    body: ExecuteSweepRequest,
) -> ExecuteSweepAccepted | ResponseError | None:
    r"""Execute a parameter sweep over prepared data

     Runs a parameter matrix over the single immutable dataset identified by `requestId`.
    The backend expands and executes the matrix internally; clients poll the returned
    `sweepId` for incremental results.

    Supplying `walkForward` runs the sweep in a different mode entirely. Instead of scoring
    every parameter vector once over the whole range, the data is split into F sequential
    folds; each fold optimizes the full grid on its own window and then scores only its winner
    on the window immediately after — data that winner was not chosen on. It answers a harder
    question than a leaderboard: not \"which parameters won\", but \"does re-optimizing this
    periodically actually work\". Omit the block and nothing changes, including the response.

    The cost is the reason it is opt-in rather than always on: F folds × N vectors, so a
    4-fold run over a 500-point grid is 2004 backtests where the plain sweep is 500. The
    request is rejected when `folds × totalRuns` exceeds the server's sweep budget.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        request_id (str):
        body (ExecuteSweepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecuteSweepAccepted | ResponseError
    """

    return sync_detailed(
        exchange_id=exchange_id,
        type_=type_,
        request_id=request_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    exchange_id: str,
    type_: DataSourceType,
    request_id: str,
    *,
    client: AuthenticatedClient,
    body: ExecuteSweepRequest,
) -> Response[ExecuteSweepAccepted | ResponseError]:
    r"""Execute a parameter sweep over prepared data

     Runs a parameter matrix over the single immutable dataset identified by `requestId`.
    The backend expands and executes the matrix internally; clients poll the returned
    `sweepId` for incremental results.

    Supplying `walkForward` runs the sweep in a different mode entirely. Instead of scoring
    every parameter vector once over the whole range, the data is split into F sequential
    folds; each fold optimizes the full grid on its own window and then scores only its winner
    on the window immediately after — data that winner was not chosen on. It answers a harder
    question than a leaderboard: not \"which parameters won\", but \"does re-optimizing this
    periodically actually work\". Omit the block and nothing changes, including the response.

    The cost is the reason it is opt-in rather than always on: F folds × N vectors, so a
    4-fold run over a 500-point grid is 2004 backtests where the plain sweep is 500. The
    request is rejected when `folds × totalRuns` exceeds the server's sweep budget.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        request_id (str):
        body (ExecuteSweepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecuteSweepAccepted | ResponseError]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        type_=type_,
        request_id=request_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    exchange_id: str,
    type_: DataSourceType,
    request_id: str,
    *,
    client: AuthenticatedClient,
    body: ExecuteSweepRequest,
) -> ExecuteSweepAccepted | ResponseError | None:
    r"""Execute a parameter sweep over prepared data

     Runs a parameter matrix over the single immutable dataset identified by `requestId`.
    The backend expands and executes the matrix internally; clients poll the returned
    `sweepId` for incremental results.

    Supplying `walkForward` runs the sweep in a different mode entirely. Instead of scoring
    every parameter vector once over the whole range, the data is split into F sequential
    folds; each fold optimizes the full grid on its own window and then scores only its winner
    on the window immediately after — data that winner was not chosen on. It answers a harder
    question than a leaderboard: not \"which parameters won\", but \"does re-optimizing this
    periodically actually work\". Omit the block and nothing changes, including the response.

    The cost is the reason it is opt-in rather than always on: F folds × N vectors, so a
    4-fold run over a 500-point grid is 2004 backtests where the plain sweep is 500. The
    request is rejected when `folds × totalRuns` exceeds the server's sweep budget.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        request_id (str):
        body (ExecuteSweepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecuteSweepAccepted | ResponseError
    """

    return (
        await asyncio_detailed(
            exchange_id=exchange_id,
            type_=type_,
            request_id=request_id,
            client=client,
            body=body,
        )
    ).parsed
