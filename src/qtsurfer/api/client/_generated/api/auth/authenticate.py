from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.auth_token_error import AuthTokenError
from ...models.auth_token_rejected import AuthTokenRejected
from ...models.auth_token_response import AuthTokenResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/token",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | AuthTokenError | AuthTokenRejected | AuthTokenResponse | None:
    if response.status_code == 200:
        response_200 = AuthTokenResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = AuthTokenRejected.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AuthTokenError.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | AuthTokenError | AuthTokenRejected | AuthTokenResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | AuthTokenError | AuthTokenRejected | AuthTokenResponse]:
    """Exchange API key for a short-lived JWT

     Exchanges a long-lived API key for a short-lived JWT used by every other
    endpoint. This is the only endpoint that accepts an API key directly —
    callers should obtain a JWT here, then send it as `Authorization: Bearer
    <token>` to all other operations.

    The returned JWT carries the caller's subscription `tier` as a claim and
    expires after `expires_in` seconds. Callers should refresh the token
    before expiry (or on a `401` response) by calling this endpoint again.

    An API key can have an expiry of its own. When it does, the answer's `key_exp` says when
    the key stops working, in seconds since epoch, so you can rotate it ahead of time instead
    of finding out from a `401`. The same value is the `key_exp` claim of the token and the
    `apiKeyExpiresAt` of `GET /account`. A key that never expires has no `key_exp`. It is the
    key's expiry, not the token's: a token issued just before the key lapses keeps working
    until its own `expires_in` is over.

    The answer's `scopes` say what the key may do. Where a deployment requires scopes, a key
    that carries none is refused with `403` and the code `apikey_without_scopes`: create a key
    with at least one scope.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AuthTokenError | AuthTokenRejected | AuthTokenResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Any | AuthTokenError | AuthTokenRejected | AuthTokenResponse | None:
    """Exchange API key for a short-lived JWT

     Exchanges a long-lived API key for a short-lived JWT used by every other
    endpoint. This is the only endpoint that accepts an API key directly —
    callers should obtain a JWT here, then send it as `Authorization: Bearer
    <token>` to all other operations.

    The returned JWT carries the caller's subscription `tier` as a claim and
    expires after `expires_in` seconds. Callers should refresh the token
    before expiry (or on a `401` response) by calling this endpoint again.

    An API key can have an expiry of its own. When it does, the answer's `key_exp` says when
    the key stops working, in seconds since epoch, so you can rotate it ahead of time instead
    of finding out from a `401`. The same value is the `key_exp` claim of the token and the
    `apiKeyExpiresAt` of `GET /account`. A key that never expires has no `key_exp`. It is the
    key's expiry, not the token's: a token issued just before the key lapses keeps working
    until its own `expires_in` is over.

    The answer's `scopes` say what the key may do. Where a deployment requires scopes, a key
    that carries none is refused with `403` and the code `apikey_without_scopes`: create a key
    with at least one scope.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AuthTokenError | AuthTokenRejected | AuthTokenResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | AuthTokenError | AuthTokenRejected | AuthTokenResponse]:
    """Exchange API key for a short-lived JWT

     Exchanges a long-lived API key for a short-lived JWT used by every other
    endpoint. This is the only endpoint that accepts an API key directly —
    callers should obtain a JWT here, then send it as `Authorization: Bearer
    <token>` to all other operations.

    The returned JWT carries the caller's subscription `tier` as a claim and
    expires after `expires_in` seconds. Callers should refresh the token
    before expiry (or on a `401` response) by calling this endpoint again.

    An API key can have an expiry of its own. When it does, the answer's `key_exp` says when
    the key stops working, in seconds since epoch, so you can rotate it ahead of time instead
    of finding out from a `401`. The same value is the `key_exp` claim of the token and the
    `apiKeyExpiresAt` of `GET /account`. A key that never expires has no `key_exp`. It is the
    key's expiry, not the token's: a token issued just before the key lapses keeps working
    until its own `expires_in` is over.

    The answer's `scopes` say what the key may do. Where a deployment requires scopes, a key
    that carries none is refused with `403` and the code `apikey_without_scopes`: create a key
    with at least one scope.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AuthTokenError | AuthTokenRejected | AuthTokenResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Any | AuthTokenError | AuthTokenRejected | AuthTokenResponse | None:
    """Exchange API key for a short-lived JWT

     Exchanges a long-lived API key for a short-lived JWT used by every other
    endpoint. This is the only endpoint that accepts an API key directly —
    callers should obtain a JWT here, then send it as `Authorization: Bearer
    <token>` to all other operations.

    The returned JWT carries the caller's subscription `tier` as a claim and
    expires after `expires_in` seconds. Callers should refresh the token
    before expiry (or on a `401` response) by calling this endpoint again.

    An API key can have an expiry of its own. When it does, the answer's `key_exp` says when
    the key stops working, in seconds since epoch, so you can rotate it ahead of time instead
    of finding out from a `401`. The same value is the `key_exp` claim of the token and the
    `apiKeyExpiresAt` of `GET /account`. A key that never expires has no `key_exp`. It is the
    key's expiry, not the token's: a token issued just before the key lapses keeps working
    until its own `expires_in` is over.

    The answer's `scopes` say what the key may do. Where a deployment requires scopes, a key
    that carries none is refused with `403` and the code `apikey_without_scopes`: create a key
    with at least one scope.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AuthTokenError | AuthTokenRejected | AuthTokenResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
