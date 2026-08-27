from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_source_type import DataSourceType
from ...models.equity_curve_out_mode import EquityCurveOutMode
from ...models.equity_curve_result import EquityCurveResult
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    exchange_id: str,
    type_: DataSourceType,
    request_id: str,
    sweep_id: str,
    run_ix: int,
    *,
    out_mode: EquityCurveOutMode | Unset = EquityCurveOutMode.ARRAY,
    resample: int | Unset = UNSET,
    differential: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_out_mode: str | Unset = UNSET
    if not isinstance(out_mode, Unset):
        json_out_mode = out_mode.value

    params["outMode"] = json_out_mode

    params["resample"] = resample

    params["differential"] = differential

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/backtest/{exchange_id}/{type_}/executeSweep/{request_id}/{sweep_id}/runs/{run_ix}/equityCurve".format(
            exchange_id=quote(str(exchange_id), safe=""),
            type_=quote(str(type_), safe=""),
            request_id=quote(str(request_id), safe=""),
            sweep_id=quote(str(sweep_id), safe=""),
            run_ix=quote(str(run_ix), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EquityCurveResult | ResponseError | None:
    if response.status_code == 200:
        response_200 = EquityCurveResult.from_dict(response.json())

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
) -> Response[EquityCurveResult | ResponseError]:
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
    run_ix: int,
    *,
    client: AuthenticatedClient,
    out_mode: EquityCurveOutMode | Unset = EquityCurveOutMode.ARRAY,
    resample: int | Unset = UNSET,
    differential: bool | Unset = False,
) -> Response[EquityCurveResult | ResponseError]:
    """Get one sweep trial's equity curve

     The resource a leaderboard row's `equityCurve.url` points at — only reachable when that
    trial's curve was actually selected (`equityCurve.mode: topN` or `topPct` on the sweep
    submission, and this trial ranked among the winners). Returns the exact same
    `{points|timestamps+equities, meta}` shape a plain backtest's inline `equityCurve` carries.

    Query params reshape the response the same way a plain backtest's `equityCurve` options do.
    A param genuinely absent from the query string falls back to the `equityCurve` transform
    preference the sweep was submitted with — a param
    present but malformed does not fall back, it degrades the same way it always has. Above a
    server-side size threshold, the shape is forced regardless of either — `meta.outMode` in
    the response, not the query string or the submitted default, is the source of truth for
    what shape actually came back.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        request_id (str):
        sweep_id (str):
        run_ix (int):
        out_mode (EquityCurveOutMode | Unset): JSON shape for an equity curve's points. `ARRAY` is
            `[{timestamp, equity}, ...]`; `SHORT` is `{timestamps: [...], equities: [...]}` (parallel
            arrays, no repeated key text). The one schema shared by every place `outMode` appears,
            request or response, so the two cannot drift to different value sets. Default:
            EquityCurveOutMode.ARRAY.
        resample (int | Unset):
        differential (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EquityCurveResult | ResponseError]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        type_=type_,
        request_id=request_id,
        sweep_id=sweep_id,
        run_ix=run_ix,
        out_mode=out_mode,
        resample=resample,
        differential=differential,
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
    run_ix: int,
    *,
    client: AuthenticatedClient,
    out_mode: EquityCurveOutMode | Unset = EquityCurveOutMode.ARRAY,
    resample: int | Unset = UNSET,
    differential: bool | Unset = False,
) -> EquityCurveResult | ResponseError | None:
    """Get one sweep trial's equity curve

     The resource a leaderboard row's `equityCurve.url` points at — only reachable when that
    trial's curve was actually selected (`equityCurve.mode: topN` or `topPct` on the sweep
    submission, and this trial ranked among the winners). Returns the exact same
    `{points|timestamps+equities, meta}` shape a plain backtest's inline `equityCurve` carries.

    Query params reshape the response the same way a plain backtest's `equityCurve` options do.
    A param genuinely absent from the query string falls back to the `equityCurve` transform
    preference the sweep was submitted with — a param
    present but malformed does not fall back, it degrades the same way it always has. Above a
    server-side size threshold, the shape is forced regardless of either — `meta.outMode` in
    the response, not the query string or the submitted default, is the source of truth for
    what shape actually came back.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        request_id (str):
        sweep_id (str):
        run_ix (int):
        out_mode (EquityCurveOutMode | Unset): JSON shape for an equity curve's points. `ARRAY` is
            `[{timestamp, equity}, ...]`; `SHORT` is `{timestamps: [...], equities: [...]}` (parallel
            arrays, no repeated key text). The one schema shared by every place `outMode` appears,
            request or response, so the two cannot drift to different value sets. Default:
            EquityCurveOutMode.ARRAY.
        resample (int | Unset):
        differential (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EquityCurveResult | ResponseError
    """

    return sync_detailed(
        exchange_id=exchange_id,
        type_=type_,
        request_id=request_id,
        sweep_id=sweep_id,
        run_ix=run_ix,
        client=client,
        out_mode=out_mode,
        resample=resample,
        differential=differential,
    ).parsed


async def asyncio_detailed(
    exchange_id: str,
    type_: DataSourceType,
    request_id: str,
    sweep_id: str,
    run_ix: int,
    *,
    client: AuthenticatedClient,
    out_mode: EquityCurveOutMode | Unset = EquityCurveOutMode.ARRAY,
    resample: int | Unset = UNSET,
    differential: bool | Unset = False,
) -> Response[EquityCurveResult | ResponseError]:
    """Get one sweep trial's equity curve

     The resource a leaderboard row's `equityCurve.url` points at — only reachable when that
    trial's curve was actually selected (`equityCurve.mode: topN` or `topPct` on the sweep
    submission, and this trial ranked among the winners). Returns the exact same
    `{points|timestamps+equities, meta}` shape a plain backtest's inline `equityCurve` carries.

    Query params reshape the response the same way a plain backtest's `equityCurve` options do.
    A param genuinely absent from the query string falls back to the `equityCurve` transform
    preference the sweep was submitted with — a param
    present but malformed does not fall back, it degrades the same way it always has. Above a
    server-side size threshold, the shape is forced regardless of either — `meta.outMode` in
    the response, not the query string or the submitted default, is the source of truth for
    what shape actually came back.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        request_id (str):
        sweep_id (str):
        run_ix (int):
        out_mode (EquityCurveOutMode | Unset): JSON shape for an equity curve's points. `ARRAY` is
            `[{timestamp, equity}, ...]`; `SHORT` is `{timestamps: [...], equities: [...]}` (parallel
            arrays, no repeated key text). The one schema shared by every place `outMode` appears,
            request or response, so the two cannot drift to different value sets. Default:
            EquityCurveOutMode.ARRAY.
        resample (int | Unset):
        differential (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EquityCurveResult | ResponseError]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        type_=type_,
        request_id=request_id,
        sweep_id=sweep_id,
        run_ix=run_ix,
        out_mode=out_mode,
        resample=resample,
        differential=differential,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    exchange_id: str,
    type_: DataSourceType,
    request_id: str,
    sweep_id: str,
    run_ix: int,
    *,
    client: AuthenticatedClient,
    out_mode: EquityCurveOutMode | Unset = EquityCurveOutMode.ARRAY,
    resample: int | Unset = UNSET,
    differential: bool | Unset = False,
) -> EquityCurveResult | ResponseError | None:
    """Get one sweep trial's equity curve

     The resource a leaderboard row's `equityCurve.url` points at — only reachable when that
    trial's curve was actually selected (`equityCurve.mode: topN` or `topPct` on the sweep
    submission, and this trial ranked among the winners). Returns the exact same
    `{points|timestamps+equities, meta}` shape a plain backtest's inline `equityCurve` carries.

    Query params reshape the response the same way a plain backtest's `equityCurve` options do.
    A param genuinely absent from the query string falls back to the `equityCurve` transform
    preference the sweep was submitted with — a param
    present but malformed does not fall back, it degrades the same way it always has. Above a
    server-side size threshold, the shape is forced regardless of either — `meta.outMode` in
    the response, not the query string or the submitted default, is the source of truth for
    what shape actually came back.

    Args:
        exchange_id (str):  Example: binance.
        type_ (DataSourceType): Managed exchange data sources available for backtesting. Example:
            ticker.
        request_id (str):
        sweep_id (str):
        run_ix (int):
        out_mode (EquityCurveOutMode | Unset): JSON shape for an equity curve's points. `ARRAY` is
            `[{timestamp, equity}, ...]`; `SHORT` is `{timestamps: [...], equities: [...]}` (parallel
            arrays, no repeated key text). The one schema shared by every place `outMode` appears,
            request or response, so the two cannot drift to different value sets. Default:
            EquityCurveOutMode.ARRAY.
        resample (int | Unset):
        differential (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EquityCurveResult | ResponseError
    """

    return (
        await asyncio_detailed(
            exchange_id=exchange_id,
            type_=type_,
            request_id=request_id,
            sweep_id=sweep_id,
            run_ix=run_ix,
            client=client,
            out_mode=out_mode,
            resample=resample,
            differential=differential,
        )
    ).parsed
