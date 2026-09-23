from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.live_signal_page import LiveSignalPage
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    run_id: str,
    *,
    since_ms: int | Unset = UNSET,
    instrument: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["sinceMs"] = since_ms

    params["instrument"] = instrument

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/live/{run_id}/signals".format(
            run_id=quote(str(run_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LiveSignalPage | ResponseError | None:
    if response.status_code == 200:
        response_200 = LiveSignalPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ResponseError.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ResponseError.from_dict(response.json())

        return response_404

    if response.status_code == 410:
        response_410 = ResponseError.from_dict(response.json())

        return response_410

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LiveSignalPage | ResponseError]:
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
    since_ms: int | Unset = UNSET,
    instrument: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[LiveSignalPage | ResponseError]:
    """Read a run's signals

     Returns one page of the signals a run has already produced, newest-last, optionally from a
    given time and narrowed to one or more instruments.

    This is the counterpart to the real-time WebSocket channel: that channel only carries what
    happens while you are connected, and only for a run that asked for `relay`. A run's signals
    are recorded either way, so this endpoint serves them whether or not `relay` was ever on,
    in both the `sandbox` and `live` stages — use it to catch up after a disconnect, to read a
    run you never relayed, or to page back over what has already happened.

    **The available window moves.** Signals are kept for a limited span, and the oldest are
    continuously discarded as new ones arrive, so how far back you can read is not a fixed
    number of hours: on a busy run it can be a good deal shorter. Every response carries
    `availableSinceMs`, the oldest moment that can still be answered for. Asking for a
    `sinceMs` older than that is not an error — you get everything from `availableSinceMs`
    onwards, and that field tells you it happened.

    **A cursor can expire, and on a busy run it expires quickly.** If the position a cursor
    points at has since been discarded, the next page answers `410` rather than silently
    serving a shortened page that looks complete. Treat that as a normal outcome: read
    `availableSinceMs` from the error and start again from there.

    Readable by the run's owner, and by anyone if the run is `public` — the same rule the
    signal channel applies to a subscription.

    Args:
        run_id (str):
        since_ms (int | Unset):
        instrument (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiveSignalPage | ResponseError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        since_ms=since_ms,
        instrument=instrument,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: str,
    *,
    client: AuthenticatedClient,
    since_ms: int | Unset = UNSET,
    instrument: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> LiveSignalPage | ResponseError | None:
    """Read a run's signals

     Returns one page of the signals a run has already produced, newest-last, optionally from a
    given time and narrowed to one or more instruments.

    This is the counterpart to the real-time WebSocket channel: that channel only carries what
    happens while you are connected, and only for a run that asked for `relay`. A run's signals
    are recorded either way, so this endpoint serves them whether or not `relay` was ever on,
    in both the `sandbox` and `live` stages — use it to catch up after a disconnect, to read a
    run you never relayed, or to page back over what has already happened.

    **The available window moves.** Signals are kept for a limited span, and the oldest are
    continuously discarded as new ones arrive, so how far back you can read is not a fixed
    number of hours: on a busy run it can be a good deal shorter. Every response carries
    `availableSinceMs`, the oldest moment that can still be answered for. Asking for a
    `sinceMs` older than that is not an error — you get everything from `availableSinceMs`
    onwards, and that field tells you it happened.

    **A cursor can expire, and on a busy run it expires quickly.** If the position a cursor
    points at has since been discarded, the next page answers `410` rather than silently
    serving a shortened page that looks complete. Treat that as a normal outcome: read
    `availableSinceMs` from the error and start again from there.

    Readable by the run's owner, and by anyone if the run is `public` — the same rule the
    signal channel applies to a subscription.

    Args:
        run_id (str):
        since_ms (int | Unset):
        instrument (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiveSignalPage | ResponseError
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
        since_ms=since_ms,
        instrument=instrument,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
    since_ms: int | Unset = UNSET,
    instrument: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[LiveSignalPage | ResponseError]:
    """Read a run's signals

     Returns one page of the signals a run has already produced, newest-last, optionally from a
    given time and narrowed to one or more instruments.

    This is the counterpart to the real-time WebSocket channel: that channel only carries what
    happens while you are connected, and only for a run that asked for `relay`. A run's signals
    are recorded either way, so this endpoint serves them whether or not `relay` was ever on,
    in both the `sandbox` and `live` stages — use it to catch up after a disconnect, to read a
    run you never relayed, or to page back over what has already happened.

    **The available window moves.** Signals are kept for a limited span, and the oldest are
    continuously discarded as new ones arrive, so how far back you can read is not a fixed
    number of hours: on a busy run it can be a good deal shorter. Every response carries
    `availableSinceMs`, the oldest moment that can still be answered for. Asking for a
    `sinceMs` older than that is not an error — you get everything from `availableSinceMs`
    onwards, and that field tells you it happened.

    **A cursor can expire, and on a busy run it expires quickly.** If the position a cursor
    points at has since been discarded, the next page answers `410` rather than silently
    serving a shortened page that looks complete. Treat that as a normal outcome: read
    `availableSinceMs` from the error and start again from there.

    Readable by the run's owner, and by anyone if the run is `public` — the same rule the
    signal channel applies to a subscription.

    Args:
        run_id (str):
        since_ms (int | Unset):
        instrument (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiveSignalPage | ResponseError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        since_ms=since_ms,
        instrument=instrument,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    *,
    client: AuthenticatedClient,
    since_ms: int | Unset = UNSET,
    instrument: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> LiveSignalPage | ResponseError | None:
    """Read a run's signals

     Returns one page of the signals a run has already produced, newest-last, optionally from a
    given time and narrowed to one or more instruments.

    This is the counterpart to the real-time WebSocket channel: that channel only carries what
    happens while you are connected, and only for a run that asked for `relay`. A run's signals
    are recorded either way, so this endpoint serves them whether or not `relay` was ever on,
    in both the `sandbox` and `live` stages — use it to catch up after a disconnect, to read a
    run you never relayed, or to page back over what has already happened.

    **The available window moves.** Signals are kept for a limited span, and the oldest are
    continuously discarded as new ones arrive, so how far back you can read is not a fixed
    number of hours: on a busy run it can be a good deal shorter. Every response carries
    `availableSinceMs`, the oldest moment that can still be answered for. Asking for a
    `sinceMs` older than that is not an error — you get everything from `availableSinceMs`
    onwards, and that field tells you it happened.

    **A cursor can expire, and on a busy run it expires quickly.** If the position a cursor
    points at has since been discarded, the next page answers `410` rather than silently
    serving a shortened page that looks complete. Treat that as a normal outcome: read
    `availableSinceMs` from the error and start again from there.

    Readable by the run's owner, and by anyone if the run is `public` — the same rule the
    signal channel applies to a subscription.

    Args:
        run_id (str):
        since_ms (int | Unset):
        instrument (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiveSignalPage | ResponseError
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
            since_ms=since_ms,
            instrument=instrument,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
