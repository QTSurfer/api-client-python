from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.response_error import ResponseError
from ...models.strategy_state import StrategyState
from ...models.validate_strategy_response_202 import ValidateStrategyResponse202
from ...types import Response


def _get_kwargs(
    strategy_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/strategy/{strategy_id}/validate".format(
            strategy_id=quote(str(strategy_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ResponseError | StrategyState | ValidateStrategyResponse202 | None:
    if response.status_code == 200:
        response_200 = StrategyState.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = ValidateStrategyResponse202.from_dict(response.json())

        return response_202

    if response.status_code == 404:
        response_404 = ResponseError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ResponseError | StrategyState | ValidateStrategyResponse202]:
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
) -> Response[ResponseError | StrategyState | ValidateStrategyResponse202]:
    """Check that a registered strategy can actually run

     Instantiates the compiled class and drives it through a bounded synthetic series, so a wiring
    fault surfaces here instead of at your first backtest. The verdict — pass or fail, plus any
    engine notices — is recorded and served from `GET /strategy/{strategyId}`.

    **Idempotent.** If a verdict already exists for the current compilation it comes straight
    back with `200` and nothing is queued. Otherwise the check is queued and this returns `202`;
    poll `GET /strategy/{strategyId}` until `validation` is `passed` or `failed`.

    Recompiling supersedes a verdict, which makes this callable again — the old answer described
    bytecode that is no longer what would run.

    Args:
        strategy_id (str): Unique identifier for a compiled strategy, derived from the source
            itself: the same code
            always yields the same id, for every caller, whatever its formatting. See
            `POST /strategy` for exactly which rewrites preserve it and which do not.
             Example: 6bsh31ikwkuivhtgcoa6s4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError | StrategyState | ValidateStrategyResponse202]
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
) -> ResponseError | StrategyState | ValidateStrategyResponse202 | None:
    """Check that a registered strategy can actually run

     Instantiates the compiled class and drives it through a bounded synthetic series, so a wiring
    fault surfaces here instead of at your first backtest. The verdict — pass or fail, plus any
    engine notices — is recorded and served from `GET /strategy/{strategyId}`.

    **Idempotent.** If a verdict already exists for the current compilation it comes straight
    back with `200` and nothing is queued. Otherwise the check is queued and this returns `202`;
    poll `GET /strategy/{strategyId}` until `validation` is `passed` or `failed`.

    Recompiling supersedes a verdict, which makes this callable again — the old answer described
    bytecode that is no longer what would run.

    Args:
        strategy_id (str): Unique identifier for a compiled strategy, derived from the source
            itself: the same code
            always yields the same id, for every caller, whatever its formatting. See
            `POST /strategy` for exactly which rewrites preserve it and which do not.
             Example: 6bsh31ikwkuivhtgcoa6s4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError | StrategyState | ValidateStrategyResponse202
    """

    return sync_detailed(
        strategy_id=strategy_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    strategy_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ResponseError | StrategyState | ValidateStrategyResponse202]:
    """Check that a registered strategy can actually run

     Instantiates the compiled class and drives it through a bounded synthetic series, so a wiring
    fault surfaces here instead of at your first backtest. The verdict — pass or fail, plus any
    engine notices — is recorded and served from `GET /strategy/{strategyId}`.

    **Idempotent.** If a verdict already exists for the current compilation it comes straight
    back with `200` and nothing is queued. Otherwise the check is queued and this returns `202`;
    poll `GET /strategy/{strategyId}` until `validation` is `passed` or `failed`.

    Recompiling supersedes a verdict, which makes this callable again — the old answer described
    bytecode that is no longer what would run.

    Args:
        strategy_id (str): Unique identifier for a compiled strategy, derived from the source
            itself: the same code
            always yields the same id, for every caller, whatever its formatting. See
            `POST /strategy` for exactly which rewrites preserve it and which do not.
             Example: 6bsh31ikwkuivhtgcoa6s4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError | StrategyState | ValidateStrategyResponse202]
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
) -> ResponseError | StrategyState | ValidateStrategyResponse202 | None:
    """Check that a registered strategy can actually run

     Instantiates the compiled class and drives it through a bounded synthetic series, so a wiring
    fault surfaces here instead of at your first backtest. The verdict — pass or fail, plus any
    engine notices — is recorded and served from `GET /strategy/{strategyId}`.

    **Idempotent.** If a verdict already exists for the current compilation it comes straight
    back with `200` and nothing is queued. Otherwise the check is queued and this returns `202`;
    poll `GET /strategy/{strategyId}` until `validation` is `passed` or `failed`.

    Recompiling supersedes a verdict, which makes this callable again — the old answer described
    bytecode that is no longer what would run.

    Args:
        strategy_id (str): Unique identifier for a compiled strategy, derived from the source
            itself: the same code
            always yields the same id, for every caller, whatever its formatting. See
            `POST /strategy` for exactly which rewrites preserve it and which do not.
             Example: 6bsh31ikwkuivhtgcoa6s4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError | StrategyState | ValidateStrategyResponse202
    """

    return (
        await asyncio_detailed(
            strategy_id=strategy_id,
            client=client,
        )
    ).parsed
