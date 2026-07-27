from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.backtest_job_result import BacktestJobResult
from ...models.data_source_type import DataSourceType
from ...models.get_backtest_result_response_202 import GetBacktestResultResponse202
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    exchange_id: str,
    type_: DataSourceType,
    job_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/backtest/{exchange_id}/{type_}/execute/{job_id}".format(
            exchange_id=quote(str(exchange_id), safe=""),
            type_=quote(str(type_), safe=""),
            job_id=quote(str(job_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BacktestJobResult | GetBacktestResultResponse202 | ResponseError | None:
    if response.status_code == 200:
        response_200 = BacktestJobResult.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = GetBacktestResultResponse202.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ResponseError.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ResponseError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BacktestJobResult | GetBacktestResultResponse202 | ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    exchange_id: str,
    type_: DataSourceType,
    job_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[BacktestJobResult | GetBacktestResultResponse202 | ResponseError]:
    """Get the result of a backtest execution job

     Retrieves the current state and results of the execute job identified by `jobId`.
    Poll until `state.status` is `Completed`, `Failed`, or `Aborted`.

    A `202` means the result is not readable yet — keep polling. It is never a terminal
    outcome, and it carries no `state`, so a poll loop that stops on a terminal status will
    not stop on it.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        job_id (str):  Example: 13RBLGQlPnfDjO6wyKSX8i.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BacktestJobResult | GetBacktestResultResponse202 | ResponseError]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        type_=type_,
        job_id=job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    exchange_id: str,
    type_: DataSourceType,
    job_id: str,
    *,
    client: AuthenticatedClient,
) -> BacktestJobResult | GetBacktestResultResponse202 | ResponseError | None:
    """Get the result of a backtest execution job

     Retrieves the current state and results of the execute job identified by `jobId`.
    Poll until `state.status` is `Completed`, `Failed`, or `Aborted`.

    A `202` means the result is not readable yet — keep polling. It is never a terminal
    outcome, and it carries no `state`, so a poll loop that stops on a terminal status will
    not stop on it.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        job_id (str):  Example: 13RBLGQlPnfDjO6wyKSX8i.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BacktestJobResult | GetBacktestResultResponse202 | ResponseError
    """

    return sync_detailed(
        exchange_id=exchange_id,
        type_=type_,
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    exchange_id: str,
    type_: DataSourceType,
    job_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[BacktestJobResult | GetBacktestResultResponse202 | ResponseError]:
    """Get the result of a backtest execution job

     Retrieves the current state and results of the execute job identified by `jobId`.
    Poll until `state.status` is `Completed`, `Failed`, or `Aborted`.

    A `202` means the result is not readable yet — keep polling. It is never a terminal
    outcome, and it carries no `state`, so a poll loop that stops on a terminal status will
    not stop on it.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        job_id (str):  Example: 13RBLGQlPnfDjO6wyKSX8i.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BacktestJobResult | GetBacktestResultResponse202 | ResponseError]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        type_=type_,
        job_id=job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    exchange_id: str,
    type_: DataSourceType,
    job_id: str,
    *,
    client: AuthenticatedClient,
) -> BacktestJobResult | GetBacktestResultResponse202 | ResponseError | None:
    """Get the result of a backtest execution job

     Retrieves the current state and results of the execute job identified by `jobId`.
    Poll until `state.status` is `Completed`, `Failed`, or `Aborted`.

    A `202` means the result is not readable yet — keep polling. It is never a terminal
    outcome, and it carries no `state`, so a poll loop that stops on a terminal status will
    not stop on it.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        job_id (str):  Example: 13RBLGQlPnfDjO6wyKSX8i.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BacktestJobResult | GetBacktestResultResponse202 | ResponseError
    """

    return (
        await asyncio_detailed(
            exchange_id=exchange_id,
            type_=type_,
            job_id=job_id,
            client=client,
        )
    ).parsed
