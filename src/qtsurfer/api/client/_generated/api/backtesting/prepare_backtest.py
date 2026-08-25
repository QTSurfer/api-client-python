from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.accepted_job import AcceptedJob
from ...models.data_source_type import DataSourceType
from ...models.prepare_request import PrepareRequest
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    exchange_id: str,
    type_: DataSourceType,
    *,
    body: PrepareRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/backtest/{exchange_id}/{type_}/prepare".format(
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
    body: PrepareRequest,
) -> Response[AcceptedJob | ResponseError]:
    """Prepare backtest data

     Enqueues a prepare task over the requested date range. Returns immediately with a `jobId`;
    poll `GET /backtest/{exchangeId}/{type}/prepare/{jobId}` for completion.

    The same params always return the same `jobId` (idempotent). Repeated calls with identical
    params do not enqueue duplicate work — they reuse the existing job.

    **`exchangeId: user` is reserved for your own uploaded data.** Instead of a managed
    exchange, it prepares from a dataset you created via `POST /datasets` (see the **Dataset**
    endpoints) — send `datasetId` in place of `instrument`. See `PrepareRequest` below for the
    two request shapes.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        body (PrepareRequest): Two shapes, chosen by the `exchangeId` path segment. Against a
            managed exchange,
            `instrument` is required and `datasetId`/`datasetVersionId` are ignored. Against the
            reserved `exchangeId: user`, send `datasetId` instead of `instrument` — `instrument` is
            ignored there, since it comes from the dataset itself.
             Example: {'instrument': 'BTC/USDT', 'from': '2024-12-13T00:00:00Z', 'to':
            '2024-12-14T00:00:00Z', 'cadence': '1m'}.

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
    body: PrepareRequest,
) -> AcceptedJob | ResponseError | None:
    """Prepare backtest data

     Enqueues a prepare task over the requested date range. Returns immediately with a `jobId`;
    poll `GET /backtest/{exchangeId}/{type}/prepare/{jobId}` for completion.

    The same params always return the same `jobId` (idempotent). Repeated calls with identical
    params do not enqueue duplicate work — they reuse the existing job.

    **`exchangeId: user` is reserved for your own uploaded data.** Instead of a managed
    exchange, it prepares from a dataset you created via `POST /datasets` (see the **Dataset**
    endpoints) — send `datasetId` in place of `instrument`. See `PrepareRequest` below for the
    two request shapes.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        body (PrepareRequest): Two shapes, chosen by the `exchangeId` path segment. Against a
            managed exchange,
            `instrument` is required and `datasetId`/`datasetVersionId` are ignored. Against the
            reserved `exchangeId: user`, send `datasetId` instead of `instrument` — `instrument` is
            ignored there, since it comes from the dataset itself.
             Example: {'instrument': 'BTC/USDT', 'from': '2024-12-13T00:00:00Z', 'to':
            '2024-12-14T00:00:00Z', 'cadence': '1m'}.

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
    body: PrepareRequest,
) -> Response[AcceptedJob | ResponseError]:
    """Prepare backtest data

     Enqueues a prepare task over the requested date range. Returns immediately with a `jobId`;
    poll `GET /backtest/{exchangeId}/{type}/prepare/{jobId}` for completion.

    The same params always return the same `jobId` (idempotent). Repeated calls with identical
    params do not enqueue duplicate work — they reuse the existing job.

    **`exchangeId: user` is reserved for your own uploaded data.** Instead of a managed
    exchange, it prepares from a dataset you created via `POST /datasets` (see the **Dataset**
    endpoints) — send `datasetId` in place of `instrument`. See `PrepareRequest` below for the
    two request shapes.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        body (PrepareRequest): Two shapes, chosen by the `exchangeId` path segment. Against a
            managed exchange,
            `instrument` is required and `datasetId`/`datasetVersionId` are ignored. Against the
            reserved `exchangeId: user`, send `datasetId` instead of `instrument` — `instrument` is
            ignored there, since it comes from the dataset itself.
             Example: {'instrument': 'BTC/USDT', 'from': '2024-12-13T00:00:00Z', 'to':
            '2024-12-14T00:00:00Z', 'cadence': '1m'}.

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
    body: PrepareRequest,
) -> AcceptedJob | ResponseError | None:
    """Prepare backtest data

     Enqueues a prepare task over the requested date range. Returns immediately with a `jobId`;
    poll `GET /backtest/{exchangeId}/{type}/prepare/{jobId}` for completion.

    The same params always return the same `jobId` (idempotent). Repeated calls with identical
    params do not enqueue duplicate work — they reuse the existing job.

    **`exchangeId: user` is reserved for your own uploaded data.** Instead of a managed
    exchange, it prepares from a dataset you created via `POST /datasets` (see the **Dataset**
    endpoints) — send `datasetId` in place of `instrument`. See `PrepareRequest` below for the
    two request shapes.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        body (PrepareRequest): Two shapes, chosen by the `exchangeId` path segment. Against a
            managed exchange,
            `instrument` is required and `datasetId`/`datasetVersionId` are ignored. Against the
            reserved `exchangeId: user`, send `datasetId` instead of `instrument` — `instrument` is
            ignored there, since it comes from the dataset itself.
             Example: {'instrument': 'BTC/USDT', 'from': '2024-12-13T00:00:00Z', 'to':
            '2024-12-14T00:00:00Z', 'cadence': '1m'}.

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
