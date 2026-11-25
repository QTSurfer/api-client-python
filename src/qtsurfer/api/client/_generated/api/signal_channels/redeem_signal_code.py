from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.response_error import ResponseError
from ...models.signal_code_redemption import SignalCodeRedemption
from ...models.signal_subscription import SignalSubscription
from ...types import Response


def _get_kwargs(
    *,
    body: SignalCodeRedemption,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/signals/subscriptions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InsufficientScopeError | ResponseError | SignalSubscription | None:
    if response.status_code == 200:
        response_200 = SignalSubscription.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = SignalSubscription.from_dict(response.json())

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
) -> Response[InsufficientScopeError | ResponseError | SignalSubscription]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SignalCodeRedemption,
) -> Response[InsufficientScopeError | ResponseError | SignalSubscription]:
    """Redeem a code

     Redeems a code you bought: you get a subscription to its offer, with the offer's delay, number of
    runs and
    duration (counted from now). Feed your runs with it (`POST
    /signals/subscriptions/{subscriptionId}/runs`).

    A code is used once. Sending the same code again yourself answers the subscription it gave you
    (`200`), so a
    retried request is safe; a code someone else redeemed is `409` with `reason: CODE_USED`.

    Args:
        body (SignalCodeRedemption):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalSubscription]
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
    body: SignalCodeRedemption,
) -> InsufficientScopeError | ResponseError | SignalSubscription | None:
    """Redeem a code

     Redeems a code you bought: you get a subscription to its offer, with the offer's delay, number of
    runs and
    duration (counted from now). Feed your runs with it (`POST
    /signals/subscriptions/{subscriptionId}/runs`).

    A code is used once. Sending the same code again yourself answers the subscription it gave you
    (`200`), so a
    retried request is safe; a code someone else redeemed is `409` with `reason: CODE_USED`.

    Args:
        body (SignalCodeRedemption):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalSubscription
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SignalCodeRedemption,
) -> Response[InsufficientScopeError | ResponseError | SignalSubscription]:
    """Redeem a code

     Redeems a code you bought: you get a subscription to its offer, with the offer's delay, number of
    runs and
    duration (counted from now). Feed your runs with it (`POST
    /signals/subscriptions/{subscriptionId}/runs`).

    A code is used once. Sending the same code again yourself answers the subscription it gave you
    (`200`), so a
    retried request is safe; a code someone else redeemed is `409` with `reason: CODE_USED`.

    Args:
        body (SignalCodeRedemption):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalSubscription]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SignalCodeRedemption,
) -> InsufficientScopeError | ResponseError | SignalSubscription | None:
    """Redeem a code

     Redeems a code you bought: you get a subscription to its offer, with the offer's delay, number of
    runs and
    duration (counted from now). Feed your runs with it (`POST
    /signals/subscriptions/{subscriptionId}/runs`).

    A code is used once. Sending the same code again yourself answers the subscription it gave you
    (`200`), so a
    retried request is safe; a code someone else redeemed is `409` with `reason: CODE_USED`.

    Args:
        body (SignalCodeRedemption):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalSubscription
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
