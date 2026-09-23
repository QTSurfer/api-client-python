from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.live_run import LiveRun
from ...models.response_error import ResponseError
from ...models.start_live_request import StartLiveRequest
from ...types import Response


def _get_kwargs(
    strategy_id: str,
    *,
    body: StartLiveRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/strategy/{strategy_id}/live".format(
            strategy_id=quote(str(strategy_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LiveRun | ResponseError | None:
    if response.status_code == 201:
        response_201 = LiveRun.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ResponseError.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ResponseError.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ResponseError.from_dict(response.json())

        return response_409

    if response.status_code == 429:
        response_429 = ResponseError.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LiveRun | ResponseError]:
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
    body: StartLiveRequest,
) -> Response[LiveRun | ResponseError]:
    r"""Start a strategy on a live market feed

     Starts your strategy against a live market feed. A new run always begins in the **sandbox**
    stage — a short trial that compares an independent second execution against the first for
    agreement — before it is eligible for promotion to the live stage where it actually
    publishes signals other systems can act on. Poll `GET /strategy/{strategyId}/live` (or
    `PATCH`/`DELETE` `/live/{runId}` once you have the `runId`) to watch `stage` move from
    `SANDBOX` to `LIVE`.

    Only one run per strategy at a time — starting again while one is already running is `409`;
    stop the current one first.

    `sources` takes exactly one entry today (multi-source strategies are not supported yet).
    `type` is `ticker` or `kline`; anything else is rejected. Both connect to the lightest
    (fastest) cadence available for the exchange — today that is 1 tick/second on every
    supported exchange; choosing among several cadences is not offered yet.

    `params` is passed straight through to the strategy at start — the same free-form object
    `POST /strategy/{strategyId}/validate` and the backtest endpoints already accept. To change
    a parameter **while the run is live**, use `PUT /live/{runId}/params` instead; this endpoint
    only sets the values a run starts with.

    Consuming a run's own output — its signals, and updating its parameters over a live
    connection instead of polling — is a WebSocket protocol on top of these REST endpoints; see
    the \"Live execution\" guide linked from this tag's description for the full flow (minting a
    connection token, the channel and RPC method).

    Args:
        strategy_id (str): Unique identifier for a compiled strategy, derived from the source
            itself: the same code
            always yields the same id, for every caller. How much formatting the id ignores depends on
            the language — see `POST /strategy` for exactly which rewrites preserve it and which do
            not.
             Example: 6bsh31ikwkuivhtgcoa6s4.
        body (StartLiveRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiveRun | ResponseError]
    """

    kwargs = _get_kwargs(
        strategy_id=strategy_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    strategy_id: str,
    *,
    client: AuthenticatedClient,
    body: StartLiveRequest,
) -> LiveRun | ResponseError | None:
    r"""Start a strategy on a live market feed

     Starts your strategy against a live market feed. A new run always begins in the **sandbox**
    stage — a short trial that compares an independent second execution against the first for
    agreement — before it is eligible for promotion to the live stage where it actually
    publishes signals other systems can act on. Poll `GET /strategy/{strategyId}/live` (or
    `PATCH`/`DELETE` `/live/{runId}` once you have the `runId`) to watch `stage` move from
    `SANDBOX` to `LIVE`.

    Only one run per strategy at a time — starting again while one is already running is `409`;
    stop the current one first.

    `sources` takes exactly one entry today (multi-source strategies are not supported yet).
    `type` is `ticker` or `kline`; anything else is rejected. Both connect to the lightest
    (fastest) cadence available for the exchange — today that is 1 tick/second on every
    supported exchange; choosing among several cadences is not offered yet.

    `params` is passed straight through to the strategy at start — the same free-form object
    `POST /strategy/{strategyId}/validate` and the backtest endpoints already accept. To change
    a parameter **while the run is live**, use `PUT /live/{runId}/params` instead; this endpoint
    only sets the values a run starts with.

    Consuming a run's own output — its signals, and updating its parameters over a live
    connection instead of polling — is a WebSocket protocol on top of these REST endpoints; see
    the \"Live execution\" guide linked from this tag's description for the full flow (minting a
    connection token, the channel and RPC method).

    Args:
        strategy_id (str): Unique identifier for a compiled strategy, derived from the source
            itself: the same code
            always yields the same id, for every caller. How much formatting the id ignores depends on
            the language — see `POST /strategy` for exactly which rewrites preserve it and which do
            not.
             Example: 6bsh31ikwkuivhtgcoa6s4.
        body (StartLiveRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiveRun | ResponseError
    """

    return sync_detailed(
        strategy_id=strategy_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    strategy_id: str,
    *,
    client: AuthenticatedClient,
    body: StartLiveRequest,
) -> Response[LiveRun | ResponseError]:
    r"""Start a strategy on a live market feed

     Starts your strategy against a live market feed. A new run always begins in the **sandbox**
    stage — a short trial that compares an independent second execution against the first for
    agreement — before it is eligible for promotion to the live stage where it actually
    publishes signals other systems can act on. Poll `GET /strategy/{strategyId}/live` (or
    `PATCH`/`DELETE` `/live/{runId}` once you have the `runId`) to watch `stage` move from
    `SANDBOX` to `LIVE`.

    Only one run per strategy at a time — starting again while one is already running is `409`;
    stop the current one first.

    `sources` takes exactly one entry today (multi-source strategies are not supported yet).
    `type` is `ticker` or `kline`; anything else is rejected. Both connect to the lightest
    (fastest) cadence available for the exchange — today that is 1 tick/second on every
    supported exchange; choosing among several cadences is not offered yet.

    `params` is passed straight through to the strategy at start — the same free-form object
    `POST /strategy/{strategyId}/validate` and the backtest endpoints already accept. To change
    a parameter **while the run is live**, use `PUT /live/{runId}/params` instead; this endpoint
    only sets the values a run starts with.

    Consuming a run's own output — its signals, and updating its parameters over a live
    connection instead of polling — is a WebSocket protocol on top of these REST endpoints; see
    the \"Live execution\" guide linked from this tag's description for the full flow (minting a
    connection token, the channel and RPC method).

    Args:
        strategy_id (str): Unique identifier for a compiled strategy, derived from the source
            itself: the same code
            always yields the same id, for every caller. How much formatting the id ignores depends on
            the language — see `POST /strategy` for exactly which rewrites preserve it and which do
            not.
             Example: 6bsh31ikwkuivhtgcoa6s4.
        body (StartLiveRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiveRun | ResponseError]
    """

    kwargs = _get_kwargs(
        strategy_id=strategy_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    strategy_id: str,
    *,
    client: AuthenticatedClient,
    body: StartLiveRequest,
) -> LiveRun | ResponseError | None:
    r"""Start a strategy on a live market feed

     Starts your strategy against a live market feed. A new run always begins in the **sandbox**
    stage — a short trial that compares an independent second execution against the first for
    agreement — before it is eligible for promotion to the live stage where it actually
    publishes signals other systems can act on. Poll `GET /strategy/{strategyId}/live` (or
    `PATCH`/`DELETE` `/live/{runId}` once you have the `runId`) to watch `stage` move from
    `SANDBOX` to `LIVE`.

    Only one run per strategy at a time — starting again while one is already running is `409`;
    stop the current one first.

    `sources` takes exactly one entry today (multi-source strategies are not supported yet).
    `type` is `ticker` or `kline`; anything else is rejected. Both connect to the lightest
    (fastest) cadence available for the exchange — today that is 1 tick/second on every
    supported exchange; choosing among several cadences is not offered yet.

    `params` is passed straight through to the strategy at start — the same free-form object
    `POST /strategy/{strategyId}/validate` and the backtest endpoints already accept. To change
    a parameter **while the run is live**, use `PUT /live/{runId}/params` instead; this endpoint
    only sets the values a run starts with.

    Consuming a run's own output — its signals, and updating its parameters over a live
    connection instead of polling — is a WebSocket protocol on top of these REST endpoints; see
    the \"Live execution\" guide linked from this tag's description for the full flow (minting a
    connection token, the channel and RPC method).

    Args:
        strategy_id (str): Unique identifier for a compiled strategy, derived from the source
            itself: the same code
            always yields the same id, for every caller. How much formatting the id ignores depends on
            the language — see `POST /strategy` for exactly which rewrites preserve it and which do
            not.
             Example: 6bsh31ikwkuivhtgcoa6s4.
        body (StartLiveRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiveRun | ResponseError
    """

    return (
        await asyncio_detailed(
            strategy_id=strategy_id,
            client=client,
            body=body,
        )
    ).parsed
