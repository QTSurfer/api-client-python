from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.response_error import ResponseError
from ...models.signal_notice_accepted import SignalNoticeAccepted
from ...models.signal_notice_request import SignalNoticeRequest
from ...types import Response


def _get_kwargs(
    channel_id: str,
    *,
    body: SignalNoticeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/signals/channels/{channel_id}/notices".format(
            channel_id=quote(str(channel_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InsufficientScopeError | ResponseError | SignalNoticeAccepted | None:
    if response.status_code == 202:
        response_202 = SignalNoticeAccepted.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ResponseError.from_dict(response.json())

        return response_400

    if response.status_code == 402:
        response_402 = ResponseError.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = InsufficientScopeError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ResponseError.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ResponseError.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[InsufficientScopeError | ResponseError | SignalNoticeAccepted]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    body: SignalNoticeRequest,
) -> Response[InsufficientScopeError | ResponseError | SignalNoticeAccepted]:
    r"""Publish a notice on a channel of yours

     Publishes a notice: an instrument that deserves attention. It is delivered to every run fed by a
    subscription
    of the channel that is active at this moment, each at its subscription's delay, by attaching the
    instrument to
    the run (see
    \"Attaching and detaching a source\" in the Live execution guide). Owner only.

    `source` names the instrument: a pair of a centralized exchange, or one pool. How the run reads it
    (`ticker` or
    `kline`, and its warm-up) is said for each run that a subscription feeds. `ref` is a string of
    yours, up to 64 characters:
    sending the same `ref` to the same channel answers the notice it already made instead of making
    another one, so
    a retried request or a repeated alert is safe, and it does not count against the rate of the
    channel.
    `expiresIn` is how long the notice is worth acting on: a delivery not made by then is `EXPIRED`.

    The `202` is the acceptance: `deliveries` is how many runs it goes to. What each delivery did is
    read
    by the subscriber, not by you; you see counts in `GET /signals/channels/{channelId}/notices`.

    Args:
        channel_id (str):
        body (SignalNoticeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalNoticeAccepted]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    body: SignalNoticeRequest,
) -> InsufficientScopeError | ResponseError | SignalNoticeAccepted | None:
    r"""Publish a notice on a channel of yours

     Publishes a notice: an instrument that deserves attention. It is delivered to every run fed by a
    subscription
    of the channel that is active at this moment, each at its subscription's delay, by attaching the
    instrument to
    the run (see
    \"Attaching and detaching a source\" in the Live execution guide). Owner only.

    `source` names the instrument: a pair of a centralized exchange, or one pool. How the run reads it
    (`ticker` or
    `kline`, and its warm-up) is said for each run that a subscription feeds. `ref` is a string of
    yours, up to 64 characters:
    sending the same `ref` to the same channel answers the notice it already made instead of making
    another one, so
    a retried request or a repeated alert is safe, and it does not count against the rate of the
    channel.
    `expiresIn` is how long the notice is worth acting on: a delivery not made by then is `EXPIRED`.

    The `202` is the acceptance: `deliveries` is how many runs it goes to. What each delivery did is
    read
    by the subscriber, not by you; you see counts in `GET /signals/channels/{channelId}/notices`.

    Args:
        channel_id (str):
        body (SignalNoticeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalNoticeAccepted
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    body: SignalNoticeRequest,
) -> Response[InsufficientScopeError | ResponseError | SignalNoticeAccepted]:
    r"""Publish a notice on a channel of yours

     Publishes a notice: an instrument that deserves attention. It is delivered to every run fed by a
    subscription
    of the channel that is active at this moment, each at its subscription's delay, by attaching the
    instrument to
    the run (see
    \"Attaching and detaching a source\" in the Live execution guide). Owner only.

    `source` names the instrument: a pair of a centralized exchange, or one pool. How the run reads it
    (`ticker` or
    `kline`, and its warm-up) is said for each run that a subscription feeds. `ref` is a string of
    yours, up to 64 characters:
    sending the same `ref` to the same channel answers the notice it already made instead of making
    another one, so
    a retried request or a repeated alert is safe, and it does not count against the rate of the
    channel.
    `expiresIn` is how long the notice is worth acting on: a delivery not made by then is `EXPIRED`.

    The `202` is the acceptance: `deliveries` is how many runs it goes to. What each delivery did is
    read
    by the subscriber, not by you; you see counts in `GET /signals/channels/{channelId}/notices`.

    Args:
        channel_id (str):
        body (SignalNoticeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalNoticeAccepted]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    body: SignalNoticeRequest,
) -> InsufficientScopeError | ResponseError | SignalNoticeAccepted | None:
    r"""Publish a notice on a channel of yours

     Publishes a notice: an instrument that deserves attention. It is delivered to every run fed by a
    subscription
    of the channel that is active at this moment, each at its subscription's delay, by attaching the
    instrument to
    the run (see
    \"Attaching and detaching a source\" in the Live execution guide). Owner only.

    `source` names the instrument: a pair of a centralized exchange, or one pool. How the run reads it
    (`ticker` or
    `kline`, and its warm-up) is said for each run that a subscription feeds. `ref` is a string of
    yours, up to 64 characters:
    sending the same `ref` to the same channel answers the notice it already made instead of making
    another one, so
    a retried request or a repeated alert is safe, and it does not count against the rate of the
    channel.
    `expiresIn` is how long the notice is worth acting on: a delivery not made by then is `EXPIRED`.

    The `202` is the acceptance: `deliveries` is how many runs it goes to. What each delivery did is
    read
    by the subscriber, not by you; you see counts in `GET /signals/channels/{channelId}/notices`.

    Args:
        channel_id (str):
        body (SignalNoticeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalNoticeAccepted
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            body=body,
        )
    ).parsed
