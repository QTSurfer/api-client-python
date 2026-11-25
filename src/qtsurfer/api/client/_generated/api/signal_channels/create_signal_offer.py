from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.response_error import ResponseError
from ...models.signal_offer import SignalOffer
from ...models.signal_offer_request import SignalOfferRequest
from ...types import Response


def _get_kwargs(
    channel_id: str,
    *,
    body: SignalOfferRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/signals/channels/{channel_id}/offers".format(
            channel_id=quote(str(channel_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InsufficientScopeError | ResponseError | SignalOffer | None:
    if response.status_code == 201:
        response_201 = SignalOffer.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[InsufficientScopeError | ResponseError | SignalOffer]:
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
    body: SignalOfferRequest,
) -> Response[InsufficientScopeError | ResponseError | SignalOffer]:
    """Create an offer of a channel of yours

     An offer is what you sell: notices of this channel at `delay` seconds after they are published, to
    up to
    `maxRuns` of the buyer's live runs, for `durationDays` from the moment the code is redeemed (left
    out, it does
    not expire). `purchaseUrl` is where you sell it, shown with the channel; `https` only. Owner only.

    A channel has at most 10 offers; several may share a delay (for example 60 s for 1 run, and 60 s for
    5 runs).
    You sell an offer by minting codes for it (`POST /signals/offers/{offerId}/codes`).

    Args:
        channel_id (str):
        body (SignalOfferRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalOffer]
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
    body: SignalOfferRequest,
) -> InsufficientScopeError | ResponseError | SignalOffer | None:
    """Create an offer of a channel of yours

     An offer is what you sell: notices of this channel at `delay` seconds after they are published, to
    up to
    `maxRuns` of the buyer's live runs, for `durationDays` from the moment the code is redeemed (left
    out, it does
    not expire). `purchaseUrl` is where you sell it, shown with the channel; `https` only. Owner only.

    A channel has at most 10 offers; several may share a delay (for example 60 s for 1 run, and 60 s for
    5 runs).
    You sell an offer by minting codes for it (`POST /signals/offers/{offerId}/codes`).

    Args:
        channel_id (str):
        body (SignalOfferRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalOffer
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
    body: SignalOfferRequest,
) -> Response[InsufficientScopeError | ResponseError | SignalOffer]:
    """Create an offer of a channel of yours

     An offer is what you sell: notices of this channel at `delay` seconds after they are published, to
    up to
    `maxRuns` of the buyer's live runs, for `durationDays` from the moment the code is redeemed (left
    out, it does
    not expire). `purchaseUrl` is where you sell it, shown with the channel; `https` only. Owner only.

    A channel has at most 10 offers; several may share a delay (for example 60 s for 1 run, and 60 s for
    5 runs).
    You sell an offer by minting codes for it (`POST /signals/offers/{offerId}/codes`).

    Args:
        channel_id (str):
        body (SignalOfferRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalOffer]
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
    body: SignalOfferRequest,
) -> InsufficientScopeError | ResponseError | SignalOffer | None:
    """Create an offer of a channel of yours

     An offer is what you sell: notices of this channel at `delay` seconds after they are published, to
    up to
    `maxRuns` of the buyer's live runs, for `durationDays` from the moment the code is redeemed (left
    out, it does
    not expire). `purchaseUrl` is where you sell it, shown with the channel; `https` only. Owner only.

    A channel has at most 10 offers; several may share a delay (for example 60 s for 1 run, and 60 s for
    5 runs).
    You sell an offer by minting codes for it (`POST /signals/offers/{offerId}/codes`).

    Args:
        channel_id (str):
        body (SignalOfferRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalOffer
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            body=body,
        )
    ).parsed
