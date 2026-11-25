from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.response_error import ResponseError
from ...models.signal_notice_page import SignalNoticePage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    channel_id: str,
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/signals/channels/{channel_id}/notices".format(
            channel_id=quote(str(channel_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InsufficientScopeError | ResponseError | SignalNoticePage | None:
    if response.status_code == 200:
        response_200 = SignalNoticePage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ResponseError.from_dict(response.json())

        return response_400

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
) -> Response[InsufficientScopeError | ResponseError | SignalNoticePage]:
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
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[InsufficientScopeError | ResponseError | SignalNoticePage]:
    """List the notices of a channel of yours

     The notices you published on the channel, most recent first, each with how its deliveries stand, as
    counts.
    Who received them is never shown. Owner only.

    Args:
        channel_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalNoticePage]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> InsufficientScopeError | ResponseError | SignalNoticePage | None:
    """List the notices of a channel of yours

     The notices you published on the channel, most recent first, each with how its deliveries stand, as
    counts.
    Who received them is never shown. Owner only.

    Args:
        channel_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalNoticePage
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[InsufficientScopeError | ResponseError | SignalNoticePage]:
    """List the notices of a channel of yours

     The notices you published on the channel, most recent first, each with how its deliveries stand, as
    counts.
    Who received them is never shown. Owner only.

    Args:
        channel_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalNoticePage]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> InsufficientScopeError | ResponseError | SignalNoticePage | None:
    """List the notices of a channel of yours

     The notices you published on the channel, most recent first, each with how its deliveries stand, as
    counts.
    Who received them is never shown. Owner only.

    Args:
        channel_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalNoticePage
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
