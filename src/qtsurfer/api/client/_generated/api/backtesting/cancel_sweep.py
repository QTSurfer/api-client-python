from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cancel_sweep_response_200 import CancelSweepResponse200
from ...models.data_source_type import DataSourceType
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    exchange_id: str,
    type_: DataSourceType,
    request_id: str,
    sweep_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/backtest/{exchange_id}/{type_}/executeSweep/{request_id}/{sweep_id}".format(
            exchange_id=quote(str(exchange_id), safe=""),
            type_=quote(str(type_), safe=""),
            request_id=quote(str(request_id), safe=""),
            sweep_id=quote(str(sweep_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CancelSweepResponse200 | ResponseError | None:
    if response.status_code == 200:
        response_200 = CancelSweepResponse200.from_dict(response.json())

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
) -> Response[CancelSweepResponse200 | ResponseError]:
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
) -> Response[CancelSweepResponse200 | ResponseError]:
    """Cancel a running parameter sweep

     Requests cancellation between parameter vectors. Completed rows remain readable.

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelSweepResponse200 | ResponseError]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        type_=type_,
        request_id=request_id,
        sweep_id=sweep_id,
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
) -> CancelSweepResponse200 | ResponseError | None:
    """Cancel a running parameter sweep

     Requests cancellation between parameter vectors. Completed rows remain readable.

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelSweepResponse200 | ResponseError
    """

    return sync_detailed(
        exchange_id=exchange_id,
        type_=type_,
        request_id=request_id,
        sweep_id=sweep_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    exchange_id: str,
    type_: DataSourceType,
    request_id: str,
    sweep_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CancelSweepResponse200 | ResponseError]:
    """Cancel a running parameter sweep

     Requests cancellation between parameter vectors. Completed rows remain readable.

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelSweepResponse200 | ResponseError]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        type_=type_,
        request_id=request_id,
        sweep_id=sweep_id,
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
) -> CancelSweepResponse200 | ResponseError | None:
    """Cancel a running parameter sweep

     Requests cancellation between parameter vectors. Completed rows remain readable.

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelSweepResponse200 | ResponseError
    """

    return (
        await asyncio_detailed(
            exchange_id=exchange_id,
            type_=type_,
            request_id=request_id,
            sweep_id=sweep_id,
            client=client,
        )
    ).parsed
