from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_strategy_response_200 import GetStrategyResponse200
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    strategy_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/strategy/{strategy_id}".format(
            strategy_id=quote(str(strategy_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetStrategyResponse200 | ResponseError | None:
    if response.status_code == 200:
        response_200 = GetStrategyResponse200.from_dict(response.json())

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
) -> Response[GetStrategyResponse200 | ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    strategy_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[GetStrategyResponse200 | ResponseError]:
    """Get a strategy by id, including its compile status

     Polls the status of a strategy compilation. Useful when the strategy was submitted with
    `X-Compile-Async: true`. Returns the resolved `strategyId` once compilation completes.

    Args:
        strategy_id (str):  Example: 6bsh31ikwkuivhtgcoa6s4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetStrategyResponse200 | ResponseError]
    """

    kwargs = _get_kwargs(
        strategy_id=strategy_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    strategy_id: str,
    *,
    client: AuthenticatedClient,
) -> GetStrategyResponse200 | ResponseError | None:
    """Get a strategy by id, including its compile status

     Polls the status of a strategy compilation. Useful when the strategy was submitted with
    `X-Compile-Async: true`. Returns the resolved `strategyId` once compilation completes.

    Args:
        strategy_id (str):  Example: 6bsh31ikwkuivhtgcoa6s4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStrategyResponse200 | ResponseError
    """

    return sync_detailed(
        strategy_id=strategy_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    strategy_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[GetStrategyResponse200 | ResponseError]:
    """Get a strategy by id, including its compile status

     Polls the status of a strategy compilation. Useful when the strategy was submitted with
    `X-Compile-Async: true`. Returns the resolved `strategyId` once compilation completes.

    Args:
        strategy_id (str):  Example: 6bsh31ikwkuivhtgcoa6s4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetStrategyResponse200 | ResponseError]
    """

    kwargs = _get_kwargs(
        strategy_id=strategy_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    strategy_id: str,
    *,
    client: AuthenticatedClient,
) -> GetStrategyResponse200 | ResponseError | None:
    """Get a strategy by id, including its compile status

     Polls the status of a strategy compilation. Useful when the strategy was submitted with
    `X-Compile-Async: true`. Returns the resolved `strategyId` once compilation completes.

    Args:
        strategy_id (str):  Example: 6bsh31ikwkuivhtgcoa6s4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStrategyResponse200 | ResponseError
    """

    return (
        await asyncio_detailed(
            strategy_id=strategy_id,
            client=client,
        )
    ).parsed
