from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.equity_curve_out_mode import EquityCurveOutMode
from ...models.get_live_run_paper_equity_measure import GetLiveRunPaperEquityMeasure
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.live_paper_equity_curve import LivePaperEquityCurve
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    run_id: str,
    *,
    currency: str | Unset = UNSET,
    instrument: str | Unset = UNSET,
    measure: GetLiveRunPaperEquityMeasure | Unset = GetLiveRunPaperEquityMeasure.REALISEDPNL,
    since_ms: int | Unset = UNSET,
    out_mode: EquityCurveOutMode | Unset = EquityCurveOutMode.ARRAY,
    resample: int | Unset = UNSET,
    differential: bool | Unset = False,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["currency"] = currency

    params["instrument"] = instrument

    json_measure: str | Unset = UNSET
    if not isinstance(measure, Unset):
        json_measure = measure.value

    params["measure"] = json_measure

    params["sinceMs"] = since_ms

    json_out_mode: str | Unset = UNSET
    if not isinstance(out_mode, Unset):
        json_out_mode = out_mode.value

    params["outMode"] = json_out_mode

    params["resample"] = resample

    params["differential"] = differential

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/live/{run_id}/paper/equity".format(
            run_id=quote(str(run_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InsufficientScopeError | LivePaperEquityCurve | ResponseError | None:
    if response.status_code == 200:
        response_200 = LivePaperEquityCurve.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ResponseError.from_dict(response.json())

        return response_400

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
) -> Response[InsufficientScopeError | LivePaperEquityCurve | ResponseError]:
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
    currency: str | Unset = UNSET,
    instrument: str | Unset = UNSET,
    measure: GetLiveRunPaperEquityMeasure | Unset = GetLiveRunPaperEquityMeasure.REALISEDPNL,
    since_ms: int | Unset = UNSET,
    out_mode: EquityCurveOutMode | Unset = EquityCurveOutMode.ARRAY,
    resample: int | Unset = UNSET,
    differential: bool | Unset = False,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> Response[InsufficientScopeError | LivePaperEquityCurve | ResponseError]:
    """Read a run's paper equity curve

     One paper account's equity curve, oldest first, in the same shape as every other equity
    curve of this API (`EquityCurveResult`): `{points, meta}`, or `{timestamps, equities, meta}`
    with `outMode=SHORT`, shaped by the same `outMode`, `resample` and `differential` query
    parameters, with the account's `currency` and its `gaps` alongside. The curve is kept for
    the life of the run, so unlike signals it has no moving window.

    It is one series of running equity: the value after every closed trade and, every minute
    of market time while positions are open, the value marked to market. Where the run was
    restarted with positions open, those positions are not carried over, so the curve has no
    value there: that moment is listed in `gaps` and is not a point of the curve.

    A run has one account per quote currency and accounts are never summed. `currency` chooses
    the account; it may be left out only when the run has a single account, or none yet (an
    empty curve). In a run started with `accounts: instrument` each instrument is an account:
    `instrument` selects it, and the answer is that account's own curve, its `equity` with its
    `gaps`, with the `instrument` beside the `currency`. `currency` may then be given instead
    only while it names a single account, and `measure` does not apply (`400`).

    `sinceMs` reads from that market time on, inclusive, which is how a client that already
    holds a curve reads only what is new. A curve too long to be read in one request answers
    `400`: narrow it with `sinceMs`, or page it. As for any equity curve, the server may force
    a smaller representation above its size thresholds: `meta.outMode` is the source of truth
    for what came back.

    Paging is opt-in. With `limit` or `cursor` the answer is one page of the raw curve, oldest
    first, with `_links.next` while there is more: the way to read a long curve at full
    resolution, since a long one is otherwise resampled. A page has the same shape (`outMode`
    and `differential` apply to it, and each page is decoded on its own), holds at most `limit`
    entries (a gap counts as one), and `resample` cannot be combined with it. The cursor is
    opaque: follow `_links.next.href` as given.

    With `instrument` the answer is that instrument's cumulative realised PnL, from 0, in the
    same shape, with the same options and paging: a point at each of its closed trades. The
    instrument belongs to the account of its quote currency, so `currency` need not be given.
    `measure` says what the values are: `equity` for an account's curve, `realisedPnl` for an
    instrument's (the shape calls them `equity` either way). The last values of the curves of
    the instruments of an account add up to the account's `realisedPnl`. In between they
    follow the realised part of the account's own curve only up to the order the trades were
    processed in: that curve is recorded in that order and this one is served by event time,
    and two instruments that close almost together can be stamped slightly out of it, so at
    those points the two differ by one trade. The gaps of an account are not attributed to an
    instrument, so `gaps` is empty.

    An instrument's curve can include what it holds and has not sold: with `measure=totalPnl`
    each point is the instrument's realised PnL up to then plus the unrealised value of its open
    position, at each closed trade (where nothing is held, so it is the realised PnL) and at
    each mark while a position is open. The answer says `measure: totalPnl`. `measure` is only
    for an instrument's curve: an account's is `equity` and already includes its marks.

    Readable by the run's owner, and by anyone if the run is `public` and has reached the `live`
    stage.

    Args:
        run_id (str):
        currency (str | Unset):
        instrument (str | Unset):  Example: BTC/USDT.
        measure (GetLiveRunPaperEquityMeasure | Unset):  Default:
            GetLiveRunPaperEquityMeasure.REALISEDPNL.
        since_ms (int | Unset):
        out_mode (EquityCurveOutMode | Unset): JSON shape for an equity curve's points. `ARRAY` is
            `[{timestamp, equity}, ...]`; `SHORT` is `{timestamps: [...], equities: [...]}` (parallel
            arrays, no repeated key text). The one schema shared by every place `outMode` appears,
            request or response, so the two cannot drift to different value sets. Default:
            EquityCurveOutMode.ARRAY.
        resample (int | Unset):
        differential (bool | Unset):  Default: False.
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | LivePaperEquityCurve | ResponseError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        currency=currency,
        instrument=instrument,
        measure=measure,
        since_ms=since_ms,
        out_mode=out_mode,
        resample=resample,
        differential=differential,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: str,
    *,
    client: AuthenticatedClient,
    currency: str | Unset = UNSET,
    instrument: str | Unset = UNSET,
    measure: GetLiveRunPaperEquityMeasure | Unset = GetLiveRunPaperEquityMeasure.REALISEDPNL,
    since_ms: int | Unset = UNSET,
    out_mode: EquityCurveOutMode | Unset = EquityCurveOutMode.ARRAY,
    resample: int | Unset = UNSET,
    differential: bool | Unset = False,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> InsufficientScopeError | LivePaperEquityCurve | ResponseError | None:
    """Read a run's paper equity curve

     One paper account's equity curve, oldest first, in the same shape as every other equity
    curve of this API (`EquityCurveResult`): `{points, meta}`, or `{timestamps, equities, meta}`
    with `outMode=SHORT`, shaped by the same `outMode`, `resample` and `differential` query
    parameters, with the account's `currency` and its `gaps` alongside. The curve is kept for
    the life of the run, so unlike signals it has no moving window.

    It is one series of running equity: the value after every closed trade and, every minute
    of market time while positions are open, the value marked to market. Where the run was
    restarted with positions open, those positions are not carried over, so the curve has no
    value there: that moment is listed in `gaps` and is not a point of the curve.

    A run has one account per quote currency and accounts are never summed. `currency` chooses
    the account; it may be left out only when the run has a single account, or none yet (an
    empty curve). In a run started with `accounts: instrument` each instrument is an account:
    `instrument` selects it, and the answer is that account's own curve, its `equity` with its
    `gaps`, with the `instrument` beside the `currency`. `currency` may then be given instead
    only while it names a single account, and `measure` does not apply (`400`).

    `sinceMs` reads from that market time on, inclusive, which is how a client that already
    holds a curve reads only what is new. A curve too long to be read in one request answers
    `400`: narrow it with `sinceMs`, or page it. As for any equity curve, the server may force
    a smaller representation above its size thresholds: `meta.outMode` is the source of truth
    for what came back.

    Paging is opt-in. With `limit` or `cursor` the answer is one page of the raw curve, oldest
    first, with `_links.next` while there is more: the way to read a long curve at full
    resolution, since a long one is otherwise resampled. A page has the same shape (`outMode`
    and `differential` apply to it, and each page is decoded on its own), holds at most `limit`
    entries (a gap counts as one), and `resample` cannot be combined with it. The cursor is
    opaque: follow `_links.next.href` as given.

    With `instrument` the answer is that instrument's cumulative realised PnL, from 0, in the
    same shape, with the same options and paging: a point at each of its closed trades. The
    instrument belongs to the account of its quote currency, so `currency` need not be given.
    `measure` says what the values are: `equity` for an account's curve, `realisedPnl` for an
    instrument's (the shape calls them `equity` either way). The last values of the curves of
    the instruments of an account add up to the account's `realisedPnl`. In between they
    follow the realised part of the account's own curve only up to the order the trades were
    processed in: that curve is recorded in that order and this one is served by event time,
    and two instruments that close almost together can be stamped slightly out of it, so at
    those points the two differ by one trade. The gaps of an account are not attributed to an
    instrument, so `gaps` is empty.

    An instrument's curve can include what it holds and has not sold: with `measure=totalPnl`
    each point is the instrument's realised PnL up to then plus the unrealised value of its open
    position, at each closed trade (where nothing is held, so it is the realised PnL) and at
    each mark while a position is open. The answer says `measure: totalPnl`. `measure` is only
    for an instrument's curve: an account's is `equity` and already includes its marks.

    Readable by the run's owner, and by anyone if the run is `public` and has reached the `live`
    stage.

    Args:
        run_id (str):
        currency (str | Unset):
        instrument (str | Unset):  Example: BTC/USDT.
        measure (GetLiveRunPaperEquityMeasure | Unset):  Default:
            GetLiveRunPaperEquityMeasure.REALISEDPNL.
        since_ms (int | Unset):
        out_mode (EquityCurveOutMode | Unset): JSON shape for an equity curve's points. `ARRAY` is
            `[{timestamp, equity}, ...]`; `SHORT` is `{timestamps: [...], equities: [...]}` (parallel
            arrays, no repeated key text). The one schema shared by every place `outMode` appears,
            request or response, so the two cannot drift to different value sets. Default:
            EquityCurveOutMode.ARRAY.
        resample (int | Unset):
        differential (bool | Unset):  Default: False.
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | LivePaperEquityCurve | ResponseError
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
        currency=currency,
        instrument=instrument,
        measure=measure,
        since_ms=since_ms,
        out_mode=out_mode,
        resample=resample,
        differential=differential,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
    currency: str | Unset = UNSET,
    instrument: str | Unset = UNSET,
    measure: GetLiveRunPaperEquityMeasure | Unset = GetLiveRunPaperEquityMeasure.REALISEDPNL,
    since_ms: int | Unset = UNSET,
    out_mode: EquityCurveOutMode | Unset = EquityCurveOutMode.ARRAY,
    resample: int | Unset = UNSET,
    differential: bool | Unset = False,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> Response[InsufficientScopeError | LivePaperEquityCurve | ResponseError]:
    """Read a run's paper equity curve

     One paper account's equity curve, oldest first, in the same shape as every other equity
    curve of this API (`EquityCurveResult`): `{points, meta}`, or `{timestamps, equities, meta}`
    with `outMode=SHORT`, shaped by the same `outMode`, `resample` and `differential` query
    parameters, with the account's `currency` and its `gaps` alongside. The curve is kept for
    the life of the run, so unlike signals it has no moving window.

    It is one series of running equity: the value after every closed trade and, every minute
    of market time while positions are open, the value marked to market. Where the run was
    restarted with positions open, those positions are not carried over, so the curve has no
    value there: that moment is listed in `gaps` and is not a point of the curve.

    A run has one account per quote currency and accounts are never summed. `currency` chooses
    the account; it may be left out only when the run has a single account, or none yet (an
    empty curve). In a run started with `accounts: instrument` each instrument is an account:
    `instrument` selects it, and the answer is that account's own curve, its `equity` with its
    `gaps`, with the `instrument` beside the `currency`. `currency` may then be given instead
    only while it names a single account, and `measure` does not apply (`400`).

    `sinceMs` reads from that market time on, inclusive, which is how a client that already
    holds a curve reads only what is new. A curve too long to be read in one request answers
    `400`: narrow it with `sinceMs`, or page it. As for any equity curve, the server may force
    a smaller representation above its size thresholds: `meta.outMode` is the source of truth
    for what came back.

    Paging is opt-in. With `limit` or `cursor` the answer is one page of the raw curve, oldest
    first, with `_links.next` while there is more: the way to read a long curve at full
    resolution, since a long one is otherwise resampled. A page has the same shape (`outMode`
    and `differential` apply to it, and each page is decoded on its own), holds at most `limit`
    entries (a gap counts as one), and `resample` cannot be combined with it. The cursor is
    opaque: follow `_links.next.href` as given.

    With `instrument` the answer is that instrument's cumulative realised PnL, from 0, in the
    same shape, with the same options and paging: a point at each of its closed trades. The
    instrument belongs to the account of its quote currency, so `currency` need not be given.
    `measure` says what the values are: `equity` for an account's curve, `realisedPnl` for an
    instrument's (the shape calls them `equity` either way). The last values of the curves of
    the instruments of an account add up to the account's `realisedPnl`. In between they
    follow the realised part of the account's own curve only up to the order the trades were
    processed in: that curve is recorded in that order and this one is served by event time,
    and two instruments that close almost together can be stamped slightly out of it, so at
    those points the two differ by one trade. The gaps of an account are not attributed to an
    instrument, so `gaps` is empty.

    An instrument's curve can include what it holds and has not sold: with `measure=totalPnl`
    each point is the instrument's realised PnL up to then plus the unrealised value of its open
    position, at each closed trade (where nothing is held, so it is the realised PnL) and at
    each mark while a position is open. The answer says `measure: totalPnl`. `measure` is only
    for an instrument's curve: an account's is `equity` and already includes its marks.

    Readable by the run's owner, and by anyone if the run is `public` and has reached the `live`
    stage.

    Args:
        run_id (str):
        currency (str | Unset):
        instrument (str | Unset):  Example: BTC/USDT.
        measure (GetLiveRunPaperEquityMeasure | Unset):  Default:
            GetLiveRunPaperEquityMeasure.REALISEDPNL.
        since_ms (int | Unset):
        out_mode (EquityCurveOutMode | Unset): JSON shape for an equity curve's points. `ARRAY` is
            `[{timestamp, equity}, ...]`; `SHORT` is `{timestamps: [...], equities: [...]}` (parallel
            arrays, no repeated key text). The one schema shared by every place `outMode` appears,
            request or response, so the two cannot drift to different value sets. Default:
            EquityCurveOutMode.ARRAY.
        resample (int | Unset):
        differential (bool | Unset):  Default: False.
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | LivePaperEquityCurve | ResponseError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        currency=currency,
        instrument=instrument,
        measure=measure,
        since_ms=since_ms,
        out_mode=out_mode,
        resample=resample,
        differential=differential,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    *,
    client: AuthenticatedClient,
    currency: str | Unset = UNSET,
    instrument: str | Unset = UNSET,
    measure: GetLiveRunPaperEquityMeasure | Unset = GetLiveRunPaperEquityMeasure.REALISEDPNL,
    since_ms: int | Unset = UNSET,
    out_mode: EquityCurveOutMode | Unset = EquityCurveOutMode.ARRAY,
    resample: int | Unset = UNSET,
    differential: bool | Unset = False,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> InsufficientScopeError | LivePaperEquityCurve | ResponseError | None:
    """Read a run's paper equity curve

     One paper account's equity curve, oldest first, in the same shape as every other equity
    curve of this API (`EquityCurveResult`): `{points, meta}`, or `{timestamps, equities, meta}`
    with `outMode=SHORT`, shaped by the same `outMode`, `resample` and `differential` query
    parameters, with the account's `currency` and its `gaps` alongside. The curve is kept for
    the life of the run, so unlike signals it has no moving window.

    It is one series of running equity: the value after every closed trade and, every minute
    of market time while positions are open, the value marked to market. Where the run was
    restarted with positions open, those positions are not carried over, so the curve has no
    value there: that moment is listed in `gaps` and is not a point of the curve.

    A run has one account per quote currency and accounts are never summed. `currency` chooses
    the account; it may be left out only when the run has a single account, or none yet (an
    empty curve). In a run started with `accounts: instrument` each instrument is an account:
    `instrument` selects it, and the answer is that account's own curve, its `equity` with its
    `gaps`, with the `instrument` beside the `currency`. `currency` may then be given instead
    only while it names a single account, and `measure` does not apply (`400`).

    `sinceMs` reads from that market time on, inclusive, which is how a client that already
    holds a curve reads only what is new. A curve too long to be read in one request answers
    `400`: narrow it with `sinceMs`, or page it. As for any equity curve, the server may force
    a smaller representation above its size thresholds: `meta.outMode` is the source of truth
    for what came back.

    Paging is opt-in. With `limit` or `cursor` the answer is one page of the raw curve, oldest
    first, with `_links.next` while there is more: the way to read a long curve at full
    resolution, since a long one is otherwise resampled. A page has the same shape (`outMode`
    and `differential` apply to it, and each page is decoded on its own), holds at most `limit`
    entries (a gap counts as one), and `resample` cannot be combined with it. The cursor is
    opaque: follow `_links.next.href` as given.

    With `instrument` the answer is that instrument's cumulative realised PnL, from 0, in the
    same shape, with the same options and paging: a point at each of its closed trades. The
    instrument belongs to the account of its quote currency, so `currency` need not be given.
    `measure` says what the values are: `equity` for an account's curve, `realisedPnl` for an
    instrument's (the shape calls them `equity` either way). The last values of the curves of
    the instruments of an account add up to the account's `realisedPnl`. In between they
    follow the realised part of the account's own curve only up to the order the trades were
    processed in: that curve is recorded in that order and this one is served by event time,
    and two instruments that close almost together can be stamped slightly out of it, so at
    those points the two differ by one trade. The gaps of an account are not attributed to an
    instrument, so `gaps` is empty.

    An instrument's curve can include what it holds and has not sold: with `measure=totalPnl`
    each point is the instrument's realised PnL up to then plus the unrealised value of its open
    position, at each closed trade (where nothing is held, so it is the realised PnL) and at
    each mark while a position is open. The answer says `measure: totalPnl`. `measure` is only
    for an instrument's curve: an account's is `equity` and already includes its marks.

    Readable by the run's owner, and by anyone if the run is `public` and has reached the `live`
    stage.

    Args:
        run_id (str):
        currency (str | Unset):
        instrument (str | Unset):  Example: BTC/USDT.
        measure (GetLiveRunPaperEquityMeasure | Unset):  Default:
            GetLiveRunPaperEquityMeasure.REALISEDPNL.
        since_ms (int | Unset):
        out_mode (EquityCurveOutMode | Unset): JSON shape for an equity curve's points. `ARRAY` is
            `[{timestamp, equity}, ...]`; `SHORT` is `{timestamps: [...], equities: [...]}` (parallel
            arrays, no repeated key text). The one schema shared by every place `outMode` appears,
            request or response, so the two cannot drift to different value sets. Default:
            EquityCurveOutMode.ARRAY.
        resample (int | Unset):
        differential (bool | Unset):  Default: False.
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | LivePaperEquityCurve | ResponseError
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
            currency=currency,
            instrument=instrument,
            measure=measure,
            since_ms=since_ms,
            out_mode=out_mode,
            resample=resample,
            differential=differential,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
