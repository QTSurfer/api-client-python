from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.response_error import ResponseError
from ...models.signal_codes_request import SignalCodesRequest
from ...models.signal_minted_codes import SignalMintedCodes
from ...types import Response


def _get_kwargs(
    offer_id: str,
    *,
    body: SignalCodesRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/signals/offers/{offer_id}/codes".format(
            offer_id=quote(str(offer_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InsufficientScopeError | ResponseError | SignalMintedCodes | None:
    if response.status_code == 201:
        response_201 = SignalMintedCodes.from_dict(response.json())

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
) -> Response[InsufficientScopeError | ResponseError | SignalMintedCodes]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    offer_id: str,
    *,
    client: AuthenticatedClient,
    body: SignalCodesRequest,
) -> Response[InsufficientScopeError | ResponseError | SignalMintedCodes]:
    """Mint codes for an offer of yours

     Mints `count` single-use codes, one per sale. **This answer is the only time the codes are shown**:
    the
    platform keeps only a fingerprint of each, and `GET` lists their prefixes. Hand each code to the
    buyer it was
    sold to; whoever redeems it (`POST /signals/subscriptions`) gets a subscription to the offer. Revoke
    a code you
    refund (`DELETE /signals/codes/{codeId}`). Up to 100 codes a call, and 10 000 an offer. Owner only.

    Args:
        offer_id (str):
        body (SignalCodesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalMintedCodes]
    """

    kwargs = _get_kwargs(
        offer_id=offer_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    offer_id: str,
    *,
    client: AuthenticatedClient,
    body: SignalCodesRequest,
) -> InsufficientScopeError | ResponseError | SignalMintedCodes | None:
    """Mint codes for an offer of yours

     Mints `count` single-use codes, one per sale. **This answer is the only time the codes are shown**:
    the
    platform keeps only a fingerprint of each, and `GET` lists their prefixes. Hand each code to the
    buyer it was
    sold to; whoever redeems it (`POST /signals/subscriptions`) gets a subscription to the offer. Revoke
    a code you
    refund (`DELETE /signals/codes/{codeId}`). Up to 100 codes a call, and 10 000 an offer. Owner only.

    Args:
        offer_id (str):
        body (SignalCodesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalMintedCodes
    """

    return sync_detailed(
        offer_id=offer_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    offer_id: str,
    *,
    client: AuthenticatedClient,
    body: SignalCodesRequest,
) -> Response[InsufficientScopeError | ResponseError | SignalMintedCodes]:
    """Mint codes for an offer of yours

     Mints `count` single-use codes, one per sale. **This answer is the only time the codes are shown**:
    the
    platform keeps only a fingerprint of each, and `GET` lists their prefixes. Hand each code to the
    buyer it was
    sold to; whoever redeems it (`POST /signals/subscriptions`) gets a subscription to the offer. Revoke
    a code you
    refund (`DELETE /signals/codes/{codeId}`). Up to 100 codes a call, and 10 000 an offer. Owner only.

    Args:
        offer_id (str):
        body (SignalCodesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalMintedCodes]
    """

    kwargs = _get_kwargs(
        offer_id=offer_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    offer_id: str,
    *,
    client: AuthenticatedClient,
    body: SignalCodesRequest,
) -> InsufficientScopeError | ResponseError | SignalMintedCodes | None:
    """Mint codes for an offer of yours

     Mints `count` single-use codes, one per sale. **This answer is the only time the codes are shown**:
    the
    platform keeps only a fingerprint of each, and `GET` lists their prefixes. Hand each code to the
    buyer it was
    sold to; whoever redeems it (`POST /signals/subscriptions`) gets a subscription to the offer. Revoke
    a code you
    refund (`DELETE /signals/codes/{codeId}`). Up to 100 codes a call, and 10 000 an offer. Owner only.

    Args:
        offer_id (str):
        body (SignalCodesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalMintedCodes
    """

    return (
        await asyncio_detailed(
            offer_id=offer_id,
            client=client,
            body=body,
        )
    ).parsed
