from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.live_paper import LivePaper
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    run_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/live/{run_id}/paper".format(
            run_id=quote(str(run_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InsufficientScopeError | LivePaper | ResponseError | None:
    if response.status_code == 200:
        response_200 = LivePaper.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = InsufficientScopeError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ResponseError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[InsufficientScopeError | LivePaper | ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[InsufficientScopeError | LivePaper | ResponseError]:
    """Read a run's paper trading

     The run's paper trading as last recorded: one entry per simulated account (one per quote
    currency the run trades — never added together), with its starting capital, current
    equity, realised PnL, open positions and KPIs. The KPIs are the same a backtest reports,
    computed over the trades closed so far.

    `equity` is the account's latest recorded value: at the last closed trade (`equityKind:
    equity`), or the last periodic mark-to-market while positions are open (`equityKind:
    mark`, taken every minute of market time). Until either exists the account holds its
    starting capital.

    A run started with `accounts: instrument` has one account per instrument instead: each
    carries the `instrument` it is, with its own `initialFunding`, and none carries
    `instruments`. The accounts of such a run are never added together either.

    A position also says what it is worth. When the last mark valued it as it stands now, its
    entry in `openPositions` carries `markPrice` (the price it was valued at), `markedAtMs`
    (when) and `unrealisedPnl` (`base` times `markPrice`, minus `cost`). A position opened or
    changed since the last mark, which is at most about a minute old, has none of the three yet.
    The account says it for all its positions together: `unrealisedPnl` (their sum, `0` when it
    holds nothing) and `totalPnl` (with its `realisedPnl`); both are absent while any of its
    positions has no current mark.

    An account is shared by every instrument of its quote currency, so each account also says
    what it realised per instrument, in `instruments`: the trades, the realised PnL, its
    contribution as a percent of the account's starting capital, the position it holds, what
    that position is worth (`unrealisedPnl`, and `totalPnl` with the realised part) and its
    KPIs. It is exact for what was realised, and it is not how the instrument would have done
    on its own: its entries depended on what the others had locked from the same account.

    Readable by the run's owner, and by anyone if the run is `public` and has reached the `live`
    stage. A run started without a `paper` block answers `404`.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | LivePaper | ResponseError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> InsufficientScopeError | LivePaper | ResponseError | None:
    """Read a run's paper trading

     The run's paper trading as last recorded: one entry per simulated account (one per quote
    currency the run trades — never added together), with its starting capital, current
    equity, realised PnL, open positions and KPIs. The KPIs are the same a backtest reports,
    computed over the trades closed so far.

    `equity` is the account's latest recorded value: at the last closed trade (`equityKind:
    equity`), or the last periodic mark-to-market while positions are open (`equityKind:
    mark`, taken every minute of market time). Until either exists the account holds its
    starting capital.

    A run started with `accounts: instrument` has one account per instrument instead: each
    carries the `instrument` it is, with its own `initialFunding`, and none carries
    `instruments`. The accounts of such a run are never added together either.

    A position also says what it is worth. When the last mark valued it as it stands now, its
    entry in `openPositions` carries `markPrice` (the price it was valued at), `markedAtMs`
    (when) and `unrealisedPnl` (`base` times `markPrice`, minus `cost`). A position opened or
    changed since the last mark, which is at most about a minute old, has none of the three yet.
    The account says it for all its positions together: `unrealisedPnl` (their sum, `0` when it
    holds nothing) and `totalPnl` (with its `realisedPnl`); both are absent while any of its
    positions has no current mark.

    An account is shared by every instrument of its quote currency, so each account also says
    what it realised per instrument, in `instruments`: the trades, the realised PnL, its
    contribution as a percent of the account's starting capital, the position it holds, what
    that position is worth (`unrealisedPnl`, and `totalPnl` with the realised part) and its
    KPIs. It is exact for what was realised, and it is not how the instrument would have done
    on its own: its entries depended on what the others had locked from the same account.

    Readable by the run's owner, and by anyone if the run is `public` and has reached the `live`
    stage. A run started without a `paper` block answers `404`.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | LivePaper | ResponseError
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[InsufficientScopeError | LivePaper | ResponseError]:
    """Read a run's paper trading

     The run's paper trading as last recorded: one entry per simulated account (one per quote
    currency the run trades — never added together), with its starting capital, current
    equity, realised PnL, open positions and KPIs. The KPIs are the same a backtest reports,
    computed over the trades closed so far.

    `equity` is the account's latest recorded value: at the last closed trade (`equityKind:
    equity`), or the last periodic mark-to-market while positions are open (`equityKind:
    mark`, taken every minute of market time). Until either exists the account holds its
    starting capital.

    A run started with `accounts: instrument` has one account per instrument instead: each
    carries the `instrument` it is, with its own `initialFunding`, and none carries
    `instruments`. The accounts of such a run are never added together either.

    A position also says what it is worth. When the last mark valued it as it stands now, its
    entry in `openPositions` carries `markPrice` (the price it was valued at), `markedAtMs`
    (when) and `unrealisedPnl` (`base` times `markPrice`, minus `cost`). A position opened or
    changed since the last mark, which is at most about a minute old, has none of the three yet.
    The account says it for all its positions together: `unrealisedPnl` (their sum, `0` when it
    holds nothing) and `totalPnl` (with its `realisedPnl`); both are absent while any of its
    positions has no current mark.

    An account is shared by every instrument of its quote currency, so each account also says
    what it realised per instrument, in `instruments`: the trades, the realised PnL, its
    contribution as a percent of the account's starting capital, the position it holds, what
    that position is worth (`unrealisedPnl`, and `totalPnl` with the realised part) and its
    KPIs. It is exact for what was realised, and it is not how the instrument would have done
    on its own: its entries depended on what the others had locked from the same account.

    Readable by the run's owner, and by anyone if the run is `public` and has reached the `live`
    stage. A run started without a `paper` block answers `404`.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | LivePaper | ResponseError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> InsufficientScopeError | LivePaper | ResponseError | None:
    """Read a run's paper trading

     The run's paper trading as last recorded: one entry per simulated account (one per quote
    currency the run trades — never added together), with its starting capital, current
    equity, realised PnL, open positions and KPIs. The KPIs are the same a backtest reports,
    computed over the trades closed so far.

    `equity` is the account's latest recorded value: at the last closed trade (`equityKind:
    equity`), or the last periodic mark-to-market while positions are open (`equityKind:
    mark`, taken every minute of market time). Until either exists the account holds its
    starting capital.

    A run started with `accounts: instrument` has one account per instrument instead: each
    carries the `instrument` it is, with its own `initialFunding`, and none carries
    `instruments`. The accounts of such a run are never added together either.

    A position also says what it is worth. When the last mark valued it as it stands now, its
    entry in `openPositions` carries `markPrice` (the price it was valued at), `markedAtMs`
    (when) and `unrealisedPnl` (`base` times `markPrice`, minus `cost`). A position opened or
    changed since the last mark, which is at most about a minute old, has none of the three yet.
    The account says it for all its positions together: `unrealisedPnl` (their sum, `0` when it
    holds nothing) and `totalPnl` (with its `realisedPnl`); both are absent while any of its
    positions has no current mark.

    An account is shared by every instrument of its quote currency, so each account also says
    what it realised per instrument, in `instruments`: the trades, the realised PnL, its
    contribution as a percent of the account's starting capital, the position it holds, what
    that position is worth (`unrealisedPnl`, and `totalPnl` with the realised part) and its
    KPIs. It is exact for what was realised, and it is not how the instrument would have done
    on its own: its entries depended on what the others had locked from the same account.

    Readable by the run's owner, and by anyone if the run is `public` and has reached the `live`
    stage. A run started without a `paper` block answers `404`.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | LivePaper | ResponseError
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
        )
    ).parsed
