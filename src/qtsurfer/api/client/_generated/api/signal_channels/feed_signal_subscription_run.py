from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.response_error import ResponseError
from ...models.signal_subscription import SignalSubscription
from ...models.signal_subscription_run_request import SignalSubscriptionRunRequest
from ...types import Response


def _get_kwargs(
    subscription_id: str,
    *,
    body: SignalSubscriptionRunRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/signals/subscriptions/{subscription_id}/runs".format(
            subscription_id=quote(str(subscription_id), safe=""),
        ),
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
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    body: SignalSubscriptionRunRequest,
) -> Response[InsufficientScopeError | ResponseError | SignalSubscription]:
    """Feed one of your runs from a subscription

     From now on every notice of the subscription's channel reaches the run at the subscription's delay,
    as an
    attachment of the instrument as a source of `type`, with `warmFrom` seconds of warm-up. A run that
    waits with
    no source is the natural target: the first delivery starts it.

    `type` is how the run reads a centralized exchange's instrument, `ticker` or `kline`, and must be
    one the run's
    strategy consumes; left out, `kline`. A pool is always read as `kline`. `warmFrom` is as for an
    attachment,
    `0` to `3600`; left out, `0`, so the run reads from the moment of the delivery. A pool delivered to
    a run that
    already reads another is read from that moment whatever `warmFrom` says. `resolveInstrument` is as
    for an
    attachment.

    A subscription feeds at most its `maxRuns` runs at once, and a run is fed by one subscription of a
    channel at a
    time. The same run sent again answers the subscription unchanged.

    Args:
        subscription_id (str):
        body (SignalSubscriptionRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalSubscription]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    body: SignalSubscriptionRunRequest,
) -> InsufficientScopeError | ResponseError | SignalSubscription | None:
    """Feed one of your runs from a subscription

     From now on every notice of the subscription's channel reaches the run at the subscription's delay,
    as an
    attachment of the instrument as a source of `type`, with `warmFrom` seconds of warm-up. A run that
    waits with
    no source is the natural target: the first delivery starts it.

    `type` is how the run reads a centralized exchange's instrument, `ticker` or `kline`, and must be
    one the run's
    strategy consumes; left out, `kline`. A pool is always read as `kline`. `warmFrom` is as for an
    attachment,
    `0` to `3600`; left out, `0`, so the run reads from the moment of the delivery. A pool delivered to
    a run that
    already reads another is read from that moment whatever `warmFrom` says. `resolveInstrument` is as
    for an
    attachment.

    A subscription feeds at most its `maxRuns` runs at once, and a run is fed by one subscription of a
    channel at a
    time. The same run sent again answers the subscription unchanged.

    Args:
        subscription_id (str):
        body (SignalSubscriptionRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalSubscription
    """

    return sync_detailed(
        subscription_id=subscription_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    body: SignalSubscriptionRunRequest,
) -> Response[InsufficientScopeError | ResponseError | SignalSubscription]:
    """Feed one of your runs from a subscription

     From now on every notice of the subscription's channel reaches the run at the subscription's delay,
    as an
    attachment of the instrument as a source of `type`, with `warmFrom` seconds of warm-up. A run that
    waits with
    no source is the natural target: the first delivery starts it.

    `type` is how the run reads a centralized exchange's instrument, `ticker` or `kline`, and must be
    one the run's
    strategy consumes; left out, `kline`. A pool is always read as `kline`. `warmFrom` is as for an
    attachment,
    `0` to `3600`; left out, `0`, so the run reads from the moment of the delivery. A pool delivered to
    a run that
    already reads another is read from that moment whatever `warmFrom` says. `resolveInstrument` is as
    for an
    attachment.

    A subscription feeds at most its `maxRuns` runs at once, and a run is fed by one subscription of a
    channel at a
    time. The same run sent again answers the subscription unchanged.

    Args:
        subscription_id (str):
        body (SignalSubscriptionRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalSubscription]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    body: SignalSubscriptionRunRequest,
) -> InsufficientScopeError | ResponseError | SignalSubscription | None:
    """Feed one of your runs from a subscription

     From now on every notice of the subscription's channel reaches the run at the subscription's delay,
    as an
    attachment of the instrument as a source of `type`, with `warmFrom` seconds of warm-up. A run that
    waits with
    no source is the natural target: the first delivery starts it.

    `type` is how the run reads a centralized exchange's instrument, `ticker` or `kline`, and must be
    one the run's
    strategy consumes; left out, `kline`. A pool is always read as `kline`. `warmFrom` is as for an
    attachment,
    `0` to `3600`; left out, `0`, so the run reads from the moment of the delivery. A pool delivered to
    a run that
    already reads another is read from that moment whatever `warmFrom` says. `resolveInstrument` is as
    for an
    attachment.

    A subscription feeds at most its `maxRuns` runs at once, and a run is fed by one subscription of a
    channel at a
    time. The same run sent again answers the subscription unchanged.

    Args:
        subscription_id (str):
        body (SignalSubscriptionRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalSubscription
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            client=client,
            body=body,
        )
    ).parsed
