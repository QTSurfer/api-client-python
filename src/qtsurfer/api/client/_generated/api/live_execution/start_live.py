from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.live_run_with_stream import LiveRunWithStream
from ...models.plan_required_error import PlanRequiredError
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
) -> InsufficientScopeError | LiveRunWithStream | PlanRequiredError | ResponseError | None:
    if response.status_code == 201:
        response_201 = LiveRunWithStream.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ResponseError.from_dict(response.json())

        return response_400

    if response.status_code == 402:
        response_402 = PlanRequiredError.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = InsufficientScopeError.from_dict(response.json())

        return response_403

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
) -> Response[InsufficientScopeError | LiveRunWithStream | PlanRequiredError | ResponseError]:
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
) -> Response[InsufficientScopeError | LiveRunWithStream | PlanRequiredError | ResponseError]:
    r"""Start a strategy on a live market feed

     Starts your strategy against a live market feed. A new run begins in the **sandbox**
    stage — a short trial that compares an independent second execution against the first for
    agreement — before it is eligible for promotion to the live stage where it actually
    publishes signals other systems can act on. Poll `GET /strategy/{strategyId}/live` (or
    `PATCH`/`DELETE` `/live/{runId}` once you have the `runId`) to watch `stage` move from
    `SANDBOX` to `LIVE`.

    A strategy that has already been through that trial does not go through it again. When an
    earlier run of yours of the same compiled strategy was promoted to `LIVE`, and none of that
    compilation's runs was stopped for using more resources than allowed, the new run starts in
    `LIVE` at once: the response says `stage: LIVE` and carries the earlier verdict in `gate`.
    The parameters, sources and instruments may differ from the earlier run. Submitting the
    strategy again (`POST /strategy`) compiles it anew, and a new compilation goes through the
    sandbox like a first run. Send `sandbox: true` to start in the sandbox anyway — for
    example to read the run's signals back over the connection while you debug it, which the
    live stage does not keep.

    Only one run per strategy at a time — starting again while one is already running is `409`;
    stop the current one first.

    `sources` takes exactly one entry today (multi-source strategies are not supported yet).
    `type` is `ticker` or `kline`; anything else is rejected. Both connect to the lightest
    (fastest) cadence available for the exchange — today that is 1 tick/second on every
    supported exchange; choosing among several cadences is not offered yet.

    `venueType` is `cex` (a centralized exchange) or `dex` (one pool on a decentralized exchange). A
    `dex` source reads one
    pool, takes only `kline`, and needs the pool's address as its single instrument. See the \"Live
    execution\" guide,
    \"Sources\".

    `venueType`, `exchange` and `segment` have to be ones `GET /exchanges` lists together: the exchange
    under that
    venue type, and the segment among its `liveSegments`. Case and the spaces around a value do not
    matter, and the
    run reports them back in lower case (`cx`, the older spelling of `cex`, is still read). Anything
    else is refused
    with `400`, naming what the list has.

    `instruments` can be left out, except for a `dex` source. A QTScript strategy can declare which
    instruments it accepts with an `instruments`
    line in its source; when the compilation of the strategy records that selection as a list of pairs,
    a
    start that leaves `instruments` out, or sends `[\"*\"]`, takes that list, and otherwise the run
    reads every
    instrument the exchange/segment offers. A list you send is taken as sent. Either side of an entry
    can be `*`
    (any base paired with USDT). The instruments the run reads come back in `sources`. See the \"Live
    execution\" guide, \"Sources\".

    `params` is passed straight through to the strategy at start — the same free-form object
    `POST /strategy/{strategyId}/validate` and the backtest endpoints already accept. To change
    a parameter **while the run is live**, use `PUT /live/{runId}/params` instead; this endpoint
    only sets the values a run starts with.

    Consuming a run's own output — its signals, and updating its parameters over a live
    connection instead of polling — is a WebSocket protocol on top of these REST endpoints; see
    the \"Live execution\" guide linked from this tag's description for the full flow (minting a
    connection token, the channel and RPC method).

    **Paper trading.** Pass a `paper` block to have the run's hints executed in simulation from
    its first tick, as a backtest would execute them: fills, closed trades, equity and KPIs,
    with one simulated account per quote currency. Omitted, the run has no paper trading. It
    takes the same economics as a backtest's `baseConfig` plus where its output goes; read it
    back with `GET /live/{runId}/paper`. A strategy that listens to its own execution events
    (it overrides `getExecutionCallback()`) has no other execution venue, so it cannot start
    without a `paper` block.

    **Warming up.** Pass `warmFrom` to choose how many seconds before its start the run replays the
    market
    feed from, so that its indicators and windows have history when the first live tick arrives. `0`
    replays
    nothing: the run delivers its first signal as soon as it is running, but its indicators start empty
    and the
    first bar of a window can be partial. Omitted, the platform replays from the start of the current
    15-minute
    block, which is between 0 and 900 seconds before the run's start, so the first bar of a 15-minute
    window is
    complete. The value in effect, yours or the platform's, comes back as `warmFrom`. It can be set only
    here,
    when the run is started. See the \"Live execution\" guide, \"Warming up\".

    **How long the sandbox lasts.** A new run is tried in the sandbox for at least as long as the
    shortest trial your plan
    gives, and for no more than 24 hours. Pass `sandboxMinutes` (an integer from 5 to 1440) to ask for a
    longer one; asking
    for less than your plan gives is `429`. Omitted, the run gets your plan's shortest trial. The value
    in effect comes back
    as `sandboxMinutes`. It can be set only here, when the run is started. See the \"Live execution\"
    guide, \"How long the
    sandbox lasts\".

    **A plain WebSocket stream.** Pass `stream: true` to get a secret URL for this run's signals that a
    simple
    client, or a service that passes them on to others, can open as an ordinary WebSocket, from the
    sandbox stage
    on. The URL is in the response (`streamUrl`) and in `GET /strategy/{strategyId}/live`; treat it like
    a
    password. See the \"Live execution\" guide.

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
        Response[InsufficientScopeError | LiveRunWithStream | PlanRequiredError | ResponseError]
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
) -> InsufficientScopeError | LiveRunWithStream | PlanRequiredError | ResponseError | None:
    r"""Start a strategy on a live market feed

     Starts your strategy against a live market feed. A new run begins in the **sandbox**
    stage — a short trial that compares an independent second execution against the first for
    agreement — before it is eligible for promotion to the live stage where it actually
    publishes signals other systems can act on. Poll `GET /strategy/{strategyId}/live` (or
    `PATCH`/`DELETE` `/live/{runId}` once you have the `runId`) to watch `stage` move from
    `SANDBOX` to `LIVE`.

    A strategy that has already been through that trial does not go through it again. When an
    earlier run of yours of the same compiled strategy was promoted to `LIVE`, and none of that
    compilation's runs was stopped for using more resources than allowed, the new run starts in
    `LIVE` at once: the response says `stage: LIVE` and carries the earlier verdict in `gate`.
    The parameters, sources and instruments may differ from the earlier run. Submitting the
    strategy again (`POST /strategy`) compiles it anew, and a new compilation goes through the
    sandbox like a first run. Send `sandbox: true` to start in the sandbox anyway — for
    example to read the run's signals back over the connection while you debug it, which the
    live stage does not keep.

    Only one run per strategy at a time — starting again while one is already running is `409`;
    stop the current one first.

    `sources` takes exactly one entry today (multi-source strategies are not supported yet).
    `type` is `ticker` or `kline`; anything else is rejected. Both connect to the lightest
    (fastest) cadence available for the exchange — today that is 1 tick/second on every
    supported exchange; choosing among several cadences is not offered yet.

    `venueType` is `cex` (a centralized exchange) or `dex` (one pool on a decentralized exchange). A
    `dex` source reads one
    pool, takes only `kline`, and needs the pool's address as its single instrument. See the \"Live
    execution\" guide,
    \"Sources\".

    `venueType`, `exchange` and `segment` have to be ones `GET /exchanges` lists together: the exchange
    under that
    venue type, and the segment among its `liveSegments`. Case and the spaces around a value do not
    matter, and the
    run reports them back in lower case (`cx`, the older spelling of `cex`, is still read). Anything
    else is refused
    with `400`, naming what the list has.

    `instruments` can be left out, except for a `dex` source. A QTScript strategy can declare which
    instruments it accepts with an `instruments`
    line in its source; when the compilation of the strategy records that selection as a list of pairs,
    a
    start that leaves `instruments` out, or sends `[\"*\"]`, takes that list, and otherwise the run
    reads every
    instrument the exchange/segment offers. A list you send is taken as sent. Either side of an entry
    can be `*`
    (any base paired with USDT). The instruments the run reads come back in `sources`. See the \"Live
    execution\" guide, \"Sources\".

    `params` is passed straight through to the strategy at start — the same free-form object
    `POST /strategy/{strategyId}/validate` and the backtest endpoints already accept. To change
    a parameter **while the run is live**, use `PUT /live/{runId}/params` instead; this endpoint
    only sets the values a run starts with.

    Consuming a run's own output — its signals, and updating its parameters over a live
    connection instead of polling — is a WebSocket protocol on top of these REST endpoints; see
    the \"Live execution\" guide linked from this tag's description for the full flow (minting a
    connection token, the channel and RPC method).

    **Paper trading.** Pass a `paper` block to have the run's hints executed in simulation from
    its first tick, as a backtest would execute them: fills, closed trades, equity and KPIs,
    with one simulated account per quote currency. Omitted, the run has no paper trading. It
    takes the same economics as a backtest's `baseConfig` plus where its output goes; read it
    back with `GET /live/{runId}/paper`. A strategy that listens to its own execution events
    (it overrides `getExecutionCallback()`) has no other execution venue, so it cannot start
    without a `paper` block.

    **Warming up.** Pass `warmFrom` to choose how many seconds before its start the run replays the
    market
    feed from, so that its indicators and windows have history when the first live tick arrives. `0`
    replays
    nothing: the run delivers its first signal as soon as it is running, but its indicators start empty
    and the
    first bar of a window can be partial. Omitted, the platform replays from the start of the current
    15-minute
    block, which is between 0 and 900 seconds before the run's start, so the first bar of a 15-minute
    window is
    complete. The value in effect, yours or the platform's, comes back as `warmFrom`. It can be set only
    here,
    when the run is started. See the \"Live execution\" guide, \"Warming up\".

    **How long the sandbox lasts.** A new run is tried in the sandbox for at least as long as the
    shortest trial your plan
    gives, and for no more than 24 hours. Pass `sandboxMinutes` (an integer from 5 to 1440) to ask for a
    longer one; asking
    for less than your plan gives is `429`. Omitted, the run gets your plan's shortest trial. The value
    in effect comes back
    as `sandboxMinutes`. It can be set only here, when the run is started. See the \"Live execution\"
    guide, \"How long the
    sandbox lasts\".

    **A plain WebSocket stream.** Pass `stream: true` to get a secret URL for this run's signals that a
    simple
    client, or a service that passes them on to others, can open as an ordinary WebSocket, from the
    sandbox stage
    on. The URL is in the response (`streamUrl`) and in `GET /strategy/{strategyId}/live`; treat it like
    a
    password. See the \"Live execution\" guide.

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
        InsufficientScopeError | LiveRunWithStream | PlanRequiredError | ResponseError
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
) -> Response[InsufficientScopeError | LiveRunWithStream | PlanRequiredError | ResponseError]:
    r"""Start a strategy on a live market feed

     Starts your strategy against a live market feed. A new run begins in the **sandbox**
    stage — a short trial that compares an independent second execution against the first for
    agreement — before it is eligible for promotion to the live stage where it actually
    publishes signals other systems can act on. Poll `GET /strategy/{strategyId}/live` (or
    `PATCH`/`DELETE` `/live/{runId}` once you have the `runId`) to watch `stage` move from
    `SANDBOX` to `LIVE`.

    A strategy that has already been through that trial does not go through it again. When an
    earlier run of yours of the same compiled strategy was promoted to `LIVE`, and none of that
    compilation's runs was stopped for using more resources than allowed, the new run starts in
    `LIVE` at once: the response says `stage: LIVE` and carries the earlier verdict in `gate`.
    The parameters, sources and instruments may differ from the earlier run. Submitting the
    strategy again (`POST /strategy`) compiles it anew, and a new compilation goes through the
    sandbox like a first run. Send `sandbox: true` to start in the sandbox anyway — for
    example to read the run's signals back over the connection while you debug it, which the
    live stage does not keep.

    Only one run per strategy at a time — starting again while one is already running is `409`;
    stop the current one first.

    `sources` takes exactly one entry today (multi-source strategies are not supported yet).
    `type` is `ticker` or `kline`; anything else is rejected. Both connect to the lightest
    (fastest) cadence available for the exchange — today that is 1 tick/second on every
    supported exchange; choosing among several cadences is not offered yet.

    `venueType` is `cex` (a centralized exchange) or `dex` (one pool on a decentralized exchange). A
    `dex` source reads one
    pool, takes only `kline`, and needs the pool's address as its single instrument. See the \"Live
    execution\" guide,
    \"Sources\".

    `venueType`, `exchange` and `segment` have to be ones `GET /exchanges` lists together: the exchange
    under that
    venue type, and the segment among its `liveSegments`. Case and the spaces around a value do not
    matter, and the
    run reports them back in lower case (`cx`, the older spelling of `cex`, is still read). Anything
    else is refused
    with `400`, naming what the list has.

    `instruments` can be left out, except for a `dex` source. A QTScript strategy can declare which
    instruments it accepts with an `instruments`
    line in its source; when the compilation of the strategy records that selection as a list of pairs,
    a
    start that leaves `instruments` out, or sends `[\"*\"]`, takes that list, and otherwise the run
    reads every
    instrument the exchange/segment offers. A list you send is taken as sent. Either side of an entry
    can be `*`
    (any base paired with USDT). The instruments the run reads come back in `sources`. See the \"Live
    execution\" guide, \"Sources\".

    `params` is passed straight through to the strategy at start — the same free-form object
    `POST /strategy/{strategyId}/validate` and the backtest endpoints already accept. To change
    a parameter **while the run is live**, use `PUT /live/{runId}/params` instead; this endpoint
    only sets the values a run starts with.

    Consuming a run's own output — its signals, and updating its parameters over a live
    connection instead of polling — is a WebSocket protocol on top of these REST endpoints; see
    the \"Live execution\" guide linked from this tag's description for the full flow (minting a
    connection token, the channel and RPC method).

    **Paper trading.** Pass a `paper` block to have the run's hints executed in simulation from
    its first tick, as a backtest would execute them: fills, closed trades, equity and KPIs,
    with one simulated account per quote currency. Omitted, the run has no paper trading. It
    takes the same economics as a backtest's `baseConfig` plus where its output goes; read it
    back with `GET /live/{runId}/paper`. A strategy that listens to its own execution events
    (it overrides `getExecutionCallback()`) has no other execution venue, so it cannot start
    without a `paper` block.

    **Warming up.** Pass `warmFrom` to choose how many seconds before its start the run replays the
    market
    feed from, so that its indicators and windows have history when the first live tick arrives. `0`
    replays
    nothing: the run delivers its first signal as soon as it is running, but its indicators start empty
    and the
    first bar of a window can be partial. Omitted, the platform replays from the start of the current
    15-minute
    block, which is between 0 and 900 seconds before the run's start, so the first bar of a 15-minute
    window is
    complete. The value in effect, yours or the platform's, comes back as `warmFrom`. It can be set only
    here,
    when the run is started. See the \"Live execution\" guide, \"Warming up\".

    **How long the sandbox lasts.** A new run is tried in the sandbox for at least as long as the
    shortest trial your plan
    gives, and for no more than 24 hours. Pass `sandboxMinutes` (an integer from 5 to 1440) to ask for a
    longer one; asking
    for less than your plan gives is `429`. Omitted, the run gets your plan's shortest trial. The value
    in effect comes back
    as `sandboxMinutes`. It can be set only here, when the run is started. See the \"Live execution\"
    guide, \"How long the
    sandbox lasts\".

    **A plain WebSocket stream.** Pass `stream: true` to get a secret URL for this run's signals that a
    simple
    client, or a service that passes them on to others, can open as an ordinary WebSocket, from the
    sandbox stage
    on. The URL is in the response (`streamUrl`) and in `GET /strategy/{strategyId}/live`; treat it like
    a
    password. See the \"Live execution\" guide.

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
        Response[InsufficientScopeError | LiveRunWithStream | PlanRequiredError | ResponseError]
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
) -> InsufficientScopeError | LiveRunWithStream | PlanRequiredError | ResponseError | None:
    r"""Start a strategy on a live market feed

     Starts your strategy against a live market feed. A new run begins in the **sandbox**
    stage — a short trial that compares an independent second execution against the first for
    agreement — before it is eligible for promotion to the live stage where it actually
    publishes signals other systems can act on. Poll `GET /strategy/{strategyId}/live` (or
    `PATCH`/`DELETE` `/live/{runId}` once you have the `runId`) to watch `stage` move from
    `SANDBOX` to `LIVE`.

    A strategy that has already been through that trial does not go through it again. When an
    earlier run of yours of the same compiled strategy was promoted to `LIVE`, and none of that
    compilation's runs was stopped for using more resources than allowed, the new run starts in
    `LIVE` at once: the response says `stage: LIVE` and carries the earlier verdict in `gate`.
    The parameters, sources and instruments may differ from the earlier run. Submitting the
    strategy again (`POST /strategy`) compiles it anew, and a new compilation goes through the
    sandbox like a first run. Send `sandbox: true` to start in the sandbox anyway — for
    example to read the run's signals back over the connection while you debug it, which the
    live stage does not keep.

    Only one run per strategy at a time — starting again while one is already running is `409`;
    stop the current one first.

    `sources` takes exactly one entry today (multi-source strategies are not supported yet).
    `type` is `ticker` or `kline`; anything else is rejected. Both connect to the lightest
    (fastest) cadence available for the exchange — today that is 1 tick/second on every
    supported exchange; choosing among several cadences is not offered yet.

    `venueType` is `cex` (a centralized exchange) or `dex` (one pool on a decentralized exchange). A
    `dex` source reads one
    pool, takes only `kline`, and needs the pool's address as its single instrument. See the \"Live
    execution\" guide,
    \"Sources\".

    `venueType`, `exchange` and `segment` have to be ones `GET /exchanges` lists together: the exchange
    under that
    venue type, and the segment among its `liveSegments`. Case and the spaces around a value do not
    matter, and the
    run reports them back in lower case (`cx`, the older spelling of `cex`, is still read). Anything
    else is refused
    with `400`, naming what the list has.

    `instruments` can be left out, except for a `dex` source. A QTScript strategy can declare which
    instruments it accepts with an `instruments`
    line in its source; when the compilation of the strategy records that selection as a list of pairs,
    a
    start that leaves `instruments` out, or sends `[\"*\"]`, takes that list, and otherwise the run
    reads every
    instrument the exchange/segment offers. A list you send is taken as sent. Either side of an entry
    can be `*`
    (any base paired with USDT). The instruments the run reads come back in `sources`. See the \"Live
    execution\" guide, \"Sources\".

    `params` is passed straight through to the strategy at start — the same free-form object
    `POST /strategy/{strategyId}/validate` and the backtest endpoints already accept. To change
    a parameter **while the run is live**, use `PUT /live/{runId}/params` instead; this endpoint
    only sets the values a run starts with.

    Consuming a run's own output — its signals, and updating its parameters over a live
    connection instead of polling — is a WebSocket protocol on top of these REST endpoints; see
    the \"Live execution\" guide linked from this tag's description for the full flow (minting a
    connection token, the channel and RPC method).

    **Paper trading.** Pass a `paper` block to have the run's hints executed in simulation from
    its first tick, as a backtest would execute them: fills, closed trades, equity and KPIs,
    with one simulated account per quote currency. Omitted, the run has no paper trading. It
    takes the same economics as a backtest's `baseConfig` plus where its output goes; read it
    back with `GET /live/{runId}/paper`. A strategy that listens to its own execution events
    (it overrides `getExecutionCallback()`) has no other execution venue, so it cannot start
    without a `paper` block.

    **Warming up.** Pass `warmFrom` to choose how many seconds before its start the run replays the
    market
    feed from, so that its indicators and windows have history when the first live tick arrives. `0`
    replays
    nothing: the run delivers its first signal as soon as it is running, but its indicators start empty
    and the
    first bar of a window can be partial. Omitted, the platform replays from the start of the current
    15-minute
    block, which is between 0 and 900 seconds before the run's start, so the first bar of a 15-minute
    window is
    complete. The value in effect, yours or the platform's, comes back as `warmFrom`. It can be set only
    here,
    when the run is started. See the \"Live execution\" guide, \"Warming up\".

    **How long the sandbox lasts.** A new run is tried in the sandbox for at least as long as the
    shortest trial your plan
    gives, and for no more than 24 hours. Pass `sandboxMinutes` (an integer from 5 to 1440) to ask for a
    longer one; asking
    for less than your plan gives is `429`. Omitted, the run gets your plan's shortest trial. The value
    in effect comes back
    as `sandboxMinutes`. It can be set only here, when the run is started. See the \"Live execution\"
    guide, \"How long the
    sandbox lasts\".

    **A plain WebSocket stream.** Pass `stream: true` to get a secret URL for this run's signals that a
    simple
    client, or a service that passes them on to others, can open as an ordinary WebSocket, from the
    sandbox stage
    on. The URL is in the response (`streamUrl`) and in `GET /strategy/{strategyId}/live`; treat it like
    a
    password. See the \"Live execution\" guide.

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
        InsufficientScopeError | LiveRunWithStream | PlanRequiredError | ResponseError
    """

    return (
        await asyncio_detailed(
            strategy_id=strategy_id,
            client=client,
            body=body,
        )
    ).parsed
