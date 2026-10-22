from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.live_connection_token import LiveConnectionToken
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/live/token",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InsufficientScopeError | LiveConnectionToken | None:
    if response.status_code == 200:
        response_200 = LiveConnectionToken.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = InsufficientScopeError.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[InsufficientScopeError | LiveConnectionToken]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[InsufficientScopeError | LiveConnectionToken]:
    r"""Mint a WebSocket connection token

     Mints a short-lived token for the WebSocket connection used to receive a run's signals in
    real time and to call `live.params` (the WebSocket form of `PUT /live/{runId}/params`) —
    see the \"Live execution\" guide linked from this tag's description for the full protocol.
    Carries no request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | LiveConnectionToken]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> InsufficientScopeError | LiveConnectionToken | None:
    r"""Mint a WebSocket connection token

     Mints a short-lived token for the WebSocket connection used to receive a run's signals in
    real time and to call `live.params` (the WebSocket form of `PUT /live/{runId}/params`) —
    see the \"Live execution\" guide linked from this tag's description for the full protocol.
    Carries no request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | LiveConnectionToken
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[InsufficientScopeError | LiveConnectionToken]:
    r"""Mint a WebSocket connection token

     Mints a short-lived token for the WebSocket connection used to receive a run's signals in
    real time and to call `live.params` (the WebSocket form of `PUT /live/{runId}/params`) —
    see the \"Live execution\" guide linked from this tag's description for the full protocol.
    Carries no request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | LiveConnectionToken]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> InsufficientScopeError | LiveConnectionToken | None:
    r"""Mint a WebSocket connection token

     Mints a short-lived token for the WebSocket connection used to receive a run's signals in
    real time and to call `live.params` (the WebSocket form of `PUT /live/{runId}/params`) —
    see the \"Live execution\" guide linked from this tag's description for the full protocol.
    Carries no request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | LiveConnectionToken
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
