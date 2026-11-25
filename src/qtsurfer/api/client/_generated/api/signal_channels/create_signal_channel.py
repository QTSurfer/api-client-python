from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.response_error import ResponseError
from ...models.signal_channel import SignalChannel
from ...models.signal_channel_request import SignalChannelRequest
from ...types import Response


def _get_kwargs(
    *,
    body: SignalChannelRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/signals/channels",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InsufficientScopeError | ResponseError | SignalChannel | None:
    if response.status_code == 201:
        response_201 = SignalChannel.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ResponseError.from_dict(response.json())

        return response_400

    if response.status_code == 402:
        response_402 = ResponseError.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = InsufficientScopeError.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = ResponseError.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[InsufficientScopeError | ResponseError | SignalChannel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SignalChannelRequest,
) -> Response[InsufficientScopeError | ResponseError | SignalChannel]:
    """Create a signal channel

     Creates a channel of yours: a place where you publish notices about instruments that deserve
    attention. What
    you sell are its **offers** (`POST /signals/channels/{channelId}/offers`): a delay, how many runs
    one
    subscription feeds, how long it lasts. Each sale is a single-use **code**; whoever redeems it gets a
    subscription that feeds their live runs, and each notice you publish reaches those runs, at the
    offer's delay,
    as an attachment of the instrument. See the **[Signal
    channels](https://github.com/QTSurfer/qtsurfer-api/blob/main/docs/signals.md)** guide.

    A new channel is `unlisted`: it is found only by its `channelId`. `public` also lists it in
    `GET /signals/channels/public`, with its offers.

    The answer is the channel as you, its owner, see it: with its `webhookUrl`, the secret address that
    publishes
    a notice without a token (see `POST /signals/hook/{hookKey}`).

    Args:
        body (SignalChannelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalChannel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SignalChannelRequest,
) -> InsufficientScopeError | ResponseError | SignalChannel | None:
    """Create a signal channel

     Creates a channel of yours: a place where you publish notices about instruments that deserve
    attention. What
    you sell are its **offers** (`POST /signals/channels/{channelId}/offers`): a delay, how many runs
    one
    subscription feeds, how long it lasts. Each sale is a single-use **code**; whoever redeems it gets a
    subscription that feeds their live runs, and each notice you publish reaches those runs, at the
    offer's delay,
    as an attachment of the instrument. See the **[Signal
    channels](https://github.com/QTSurfer/qtsurfer-api/blob/main/docs/signals.md)** guide.

    A new channel is `unlisted`: it is found only by its `channelId`. `public` also lists it in
    `GET /signals/channels/public`, with its offers.

    The answer is the channel as you, its owner, see it: with its `webhookUrl`, the secret address that
    publishes
    a notice without a token (see `POST /signals/hook/{hookKey}`).

    Args:
        body (SignalChannelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalChannel
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SignalChannelRequest,
) -> Response[InsufficientScopeError | ResponseError | SignalChannel]:
    """Create a signal channel

     Creates a channel of yours: a place where you publish notices about instruments that deserve
    attention. What
    you sell are its **offers** (`POST /signals/channels/{channelId}/offers`): a delay, how many runs
    one
    subscription feeds, how long it lasts. Each sale is a single-use **code**; whoever redeems it gets a
    subscription that feeds their live runs, and each notice you publish reaches those runs, at the
    offer's delay,
    as an attachment of the instrument. See the **[Signal
    channels](https://github.com/QTSurfer/qtsurfer-api/blob/main/docs/signals.md)** guide.

    A new channel is `unlisted`: it is found only by its `channelId`. `public` also lists it in
    `GET /signals/channels/public`, with its offers.

    The answer is the channel as you, its owner, see it: with its `webhookUrl`, the secret address that
    publishes
    a notice without a token (see `POST /signals/hook/{hookKey}`).

    Args:
        body (SignalChannelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalChannel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SignalChannelRequest,
) -> InsufficientScopeError | ResponseError | SignalChannel | None:
    """Create a signal channel

     Creates a channel of yours: a place where you publish notices about instruments that deserve
    attention. What
    you sell are its **offers** (`POST /signals/channels/{channelId}/offers`): a delay, how many runs
    one
    subscription feeds, how long it lasts. Each sale is a single-use **code**; whoever redeems it gets a
    subscription that feeds their live runs, and each notice you publish reaches those runs, at the
    offer's delay,
    as an attachment of the instrument. See the **[Signal
    channels](https://github.com/QTSurfer/qtsurfer-api/blob/main/docs/signals.md)** guide.

    A new channel is `unlisted`: it is found only by its `channelId`. `public` also lists it in
    `GET /signals/channels/public`, with its offers.

    The answer is the channel as you, its owner, see it: with its `webhookUrl`, the secret address that
    publishes
    a notice without a token (see `POST /signals/hook/{hookKey}`).

    Args:
        body (SignalChannelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalChannel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
