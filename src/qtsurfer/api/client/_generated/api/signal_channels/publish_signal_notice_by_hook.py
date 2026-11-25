from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.response_error import ResponseError
from ...models.signal_notice_accepted import SignalNoticeAccepted
from ...models.signal_notice_request import SignalNoticeRequest
from ...types import Response


def _get_kwargs(
    hook_key: str,
    *,
    body: SignalNoticeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/signals/hook/{hook_key}".format(
            hook_key=quote(str(hook_key), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ResponseError | SignalNoticeAccepted | None:
    if response.status_code == 202:
        response_202 = SignalNoticeAccepted.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ResponseError.from_dict(response.json())

        return response_400

    if response.status_code == 402:
        response_402 = ResponseError.from_dict(response.json())

        return response_402

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
) -> Response[ResponseError | SignalNoticeAccepted]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: SignalNoticeRequest,
) -> Response[ResponseError | SignalNoticeAccepted]:
    """Publish a notice through a channel's webhook address

     The same as `POST /signals/channels/{channelId}/notices`, for a sender that cannot get a token or
    set headers:
    the address itself, the channel's `webhookUrl`, is the credential. Keep it secret; replace it with
    `PATCH /signals/channels/{channelId}` and `rotateWebhook: true` if it leaks.

    Needs no `Authorization` header. The body, the limits and the answers are those of publishing with a
    token.

    Args:
        hook_key (str):
        body (SignalNoticeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError | SignalNoticeAccepted]
    """

    kwargs = _get_kwargs(
        hook_key=hook_key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: SignalNoticeRequest,
) -> ResponseError | SignalNoticeAccepted | None:
    """Publish a notice through a channel's webhook address

     The same as `POST /signals/channels/{channelId}/notices`, for a sender that cannot get a token or
    set headers:
    the address itself, the channel's `webhookUrl`, is the credential. Keep it secret; replace it with
    `PATCH /signals/channels/{channelId}` and `rotateWebhook: true` if it leaks.

    Needs no `Authorization` header. The body, the limits and the answers are those of publishing with a
    token.

    Args:
        hook_key (str):
        body (SignalNoticeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError | SignalNoticeAccepted
    """

    return sync_detailed(
        hook_key=hook_key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: SignalNoticeRequest,
) -> Response[ResponseError | SignalNoticeAccepted]:
    """Publish a notice through a channel's webhook address

     The same as `POST /signals/channels/{channelId}/notices`, for a sender that cannot get a token or
    set headers:
    the address itself, the channel's `webhookUrl`, is the credential. Keep it secret; replace it with
    `PATCH /signals/channels/{channelId}` and `rotateWebhook: true` if it leaks.

    Needs no `Authorization` header. The body, the limits and the answers are those of publishing with a
    token.

    Args:
        hook_key (str):
        body (SignalNoticeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError | SignalNoticeAccepted]
    """

    kwargs = _get_kwargs(
        hook_key=hook_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: SignalNoticeRequest,
) -> ResponseError | SignalNoticeAccepted | None:
    """Publish a notice through a channel's webhook address

     The same as `POST /signals/channels/{channelId}/notices`, for a sender that cannot get a token or
    set headers:
    the address itself, the channel's `webhookUrl`, is the credential. Keep it secret; replace it with
    `PATCH /signals/channels/{channelId}` and `rotateWebhook: true` if it leaks.

    Needs no `Authorization` header. The body, the limits and the answers are those of publishing with a
    token.

    Args:
        hook_key (str):
        body (SignalNoticeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError | SignalNoticeAccepted
    """

    return (
        await asyncio_detailed(
            hook_key=hook_key,
            client=client,
            body=body,
        )
    ).parsed
