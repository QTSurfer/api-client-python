from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cancel_execution_response_200 import CancelExecutionResponse200
from ...models.data_source_type import DataSourceType
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    exchange_id: str,
    type_: DataSourceType,
    job_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/backtest/{exchange_id}/{type_}/execute/{job_id}".format(
            exchange_id=quote(str(exchange_id), safe=""),
            type_=quote(str(type_), safe=""),
            job_id=quote(str(job_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CancelExecutionResponse200 | ResponseError | None:
    if response.status_code == 200:
        response_200 = CancelExecutionResponse200.from_dict(response.json())

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
) -> Response[CancelExecutionResponse200 | ResponseError]:
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
) -> Response[CancelExecutionResponse200 | ResponseError]:
    """Cancel a running backtest execution

     Requests cancellation of the specified execution. The execution
    status will transition to `Aborted` once the cancellation is
    processed. Cancellation is asynchronous — poll the GET endpoint
    to confirm the final status.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        job_id (str):  Example: 13RBLGQlPnfDjO6wyKSX8i.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelExecutionResponse200 | ResponseError]
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
) -> CancelExecutionResponse200 | ResponseError | None:
    """Cancel a running backtest execution

     Requests cancellation of the specified execution. The execution
    status will transition to `Aborted` once the cancellation is
    processed. Cancellation is asynchronous — poll the GET endpoint
    to confirm the final status.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        job_id (str):  Example: 13RBLGQlPnfDjO6wyKSX8i.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelExecutionResponse200 | ResponseError
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
) -> Response[CancelExecutionResponse200 | ResponseError]:
    """Cancel a running backtest execution

     Requests cancellation of the specified execution. The execution
    status will transition to `Aborted` once the cancellation is
    processed. Cancellation is asynchronous — poll the GET endpoint
    to confirm the final status.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        job_id (str):  Example: 13RBLGQlPnfDjO6wyKSX8i.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelExecutionResponse200 | ResponseError]
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
) -> CancelExecutionResponse200 | ResponseError | None:
    """Cancel a running backtest execution

     Requests cancellation of the specified execution. The execution
    status will transition to `Aborted` once the cancellation is
    processed. Cancellation is asynchronous — poll the GET endpoint
    to confirm the final status.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        job_id (str):  Example: 13RBLGQlPnfDjO6wyKSX8i.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelExecutionResponse200 | ResponseError
    """

    return (
        await asyncio_detailed(
            exchange_id=exchange_id,
            type_=type_,
            job_id=job_id,
            client=client,
        )
    ).parsed
