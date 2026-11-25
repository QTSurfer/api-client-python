from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.response_error import ResponseError
from ...models.signal_code_list import SignalCodeList
from ...types import Response


def _get_kwargs(
    offer_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/signals/offers/{offer_id}/codes".format(
            offer_id=quote(str(offer_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InsufficientScopeError | ResponseError | SignalCodeList | None:
    if response.status_code == 200:
        response_200 = SignalCodeList.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = InsufficientScopeError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ResponseError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[InsufficientScopeError | ResponseError | SignalCodeList]:
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
) -> Response[InsufficientScopeError | ResponseError | SignalCodeList]:
    """List the codes of an offer of yours

     The offer's codes, oldest first: their prefix and state (`UNUSED`, `REDEEMED` or `REVOKED`), never
    the code
    itself and never who redeemed it. Owner only.

    Args:
        offer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalCodeList]
    """

    kwargs = _get_kwargs(
        offer_id=offer_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    offer_id: str,
    *,
    client: AuthenticatedClient,
) -> InsufficientScopeError | ResponseError | SignalCodeList | None:
    """List the codes of an offer of yours

     The offer's codes, oldest first: their prefix and state (`UNUSED`, `REDEEMED` or `REVOKED`), never
    the code
    itself and never who redeemed it. Owner only.

    Args:
        offer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalCodeList
    """

    return sync_detailed(
        offer_id=offer_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    offer_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[InsufficientScopeError | ResponseError | SignalCodeList]:
    """List the codes of an offer of yours

     The offer's codes, oldest first: their prefix and state (`UNUSED`, `REDEEMED` or `REVOKED`), never
    the code
    itself and never who redeemed it. Owner only.

    Args:
        offer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalCodeList]
    """

    kwargs = _get_kwargs(
        offer_id=offer_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    offer_id: str,
    *,
    client: AuthenticatedClient,
) -> InsufficientScopeError | ResponseError | SignalCodeList | None:
    """List the codes of an offer of yours

     The offer's codes, oldest first: their prefix and state (`UNUSED`, `REDEEMED` or `REVOKED`), never
    the code
    itself and never who redeemed it. Owner only.

    Args:
        offer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalCodeList
    """

    return (
        await asyncio_detailed(
            offer_id=offer_id,
            client=client,
        )
    ).parsed
