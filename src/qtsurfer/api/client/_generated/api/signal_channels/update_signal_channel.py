from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.response_error import ResponseError
from ...models.signal_channel import SignalChannel
from ...models.update_signal_channel_request import UpdateSignalChannelRequest
from ...types import Response


def _get_kwargs(
    channel_id: str,
    *,
    body: UpdateSignalChannelRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/signals/channels/{channel_id}".format(
            channel_id=quote(str(channel_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InsufficientScopeError | ResponseError | SignalChannel | None:
    if response.status_code == 200:
        response_200 = SignalChannel.from_dict(response.json())

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
) -> Response[InsufficientScopeError | ResponseError | SignalChannel]:
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
    body: UpdateSignalChannelRequest,
) -> Response[InsufficientScopeError | ResponseError | SignalChannel]:
    """Change a signal channel of yours

     Changes any of `name`, `description` and `visibility`; what is left out stays as it is.
    `rotateWebhook: true`
    replaces the `webhookUrl`: the old address stops publishing at once. Owner only.

    Args:
        channel_id (str):
        body (UpdateSignalChannelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalChannel]
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
    body: UpdateSignalChannelRequest,
) -> InsufficientScopeError | ResponseError | SignalChannel | None:
    """Change a signal channel of yours

     Changes any of `name`, `description` and `visibility`; what is left out stays as it is.
    `rotateWebhook: true`
    replaces the `webhookUrl`: the old address stops publishing at once. Owner only.

    Args:
        channel_id (str):
        body (UpdateSignalChannelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalChannel
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
    body: UpdateSignalChannelRequest,
) -> Response[InsufficientScopeError | ResponseError | SignalChannel]:
    """Change a signal channel of yours

     Changes any of `name`, `description` and `visibility`; what is left out stays as it is.
    `rotateWebhook: true`
    replaces the `webhookUrl`: the old address stops publishing at once. Owner only.

    Args:
        channel_id (str):
        body (UpdateSignalChannelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalChannel]
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
    body: UpdateSignalChannelRequest,
) -> InsufficientScopeError | ResponseError | SignalChannel | None:
    """Change a signal channel of yours

     Changes any of `name`, `description` and `visibility`; what is left out stays as it is.
    `rotateWebhook: true`
    replaces the `webhookUrl`: the old address stops publishing at once. Owner only.

    Args:
        channel_id (str):
        body (UpdateSignalChannelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalChannel
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            body=body,
        )
    ).parsed
