from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
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
) -> LivePaper | ResponseError | None:
    if response.status_code == 200:
        response_200 = LivePaper.from_dict(response.json())

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
) -> Response[LivePaper | ResponseError]:
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
) -> Response[LivePaper | ResponseError]:
    """Read a run's paper trading

     The run's paper trading as last recorded: one entry per simulated account (one per quote
    currency the run trades — never added together), with its starting capital, current
    equity, realised PnL, open positions and KPIs. The KPIs are the same a backtest reports,
    computed over the trades closed so far.

    `equity` is the account's latest recorded value: at the last closed trade (`equityKind:
    equity`), or the last periodic mark-to-market while positions are open (`equityKind:
    mark`, taken every minute of market time). Until either exists the account holds its
    starting capital.

    Readable by the run's owner, and by anyone if the run is `public` and has reached the `live`
    stage. A run started without a `paper` block answers `404`.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LivePaper | ResponseError]
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
) -> LivePaper | ResponseError | None:
    """Read a run's paper trading

     The run's paper trading as last recorded: one entry per simulated account (one per quote
    currency the run trades — never added together), with its starting capital, current
    equity, realised PnL, open positions and KPIs. The KPIs are the same a backtest reports,
    computed over the trades closed so far.

    `equity` is the account's latest recorded value: at the last closed trade (`equityKind:
    equity`), or the last periodic mark-to-market while positions are open (`equityKind:
    mark`, taken every minute of market time). Until either exists the account holds its
    starting capital.

    Readable by the run's owner, and by anyone if the run is `public` and has reached the `live`
    stage. A run started without a `paper` block answers `404`.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LivePaper | ResponseError
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[LivePaper | ResponseError]:
    """Read a run's paper trading

     The run's paper trading as last recorded: one entry per simulated account (one per quote
    currency the run trades — never added together), with its starting capital, current
    equity, realised PnL, open positions and KPIs. The KPIs are the same a backtest reports,
    computed over the trades closed so far.

    `equity` is the account's latest recorded value: at the last closed trade (`equityKind:
    equity`), or the last periodic mark-to-market while positions are open (`equityKind:
    mark`, taken every minute of market time). Until either exists the account holds its
    starting capital.

    Readable by the run's owner, and by anyone if the run is `public` and has reached the `live`
    stage. A run started without a `paper` block answers `404`.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LivePaper | ResponseError]
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
) -> LivePaper | ResponseError | None:
    """Read a run's paper trading

     The run's paper trading as last recorded: one entry per simulated account (one per quote
    currency the run trades — never added together), with its starting capital, current
    equity, realised PnL, open positions and KPIs. The KPIs are the same a backtest reports,
    computed over the trades closed so far.

    `equity` is the account's latest recorded value: at the last closed trade (`equityKind:
    equity`), or the last periodic mark-to-market while positions are open (`equityKind:
    mark`, taken every minute of market time). Until either exists the account holds its
    starting capital.

    Readable by the run's owner, and by anyone if the run is `public` and has reached the `live`
    stage. A run started without a `paper` block answers `404`.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LivePaper | ResponseError
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
        )
    ).parsed
