from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    channel_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/signals/channels/{channel_id}".format(
            channel_id=quote(str(channel_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | InsufficientScopeError | ResponseError | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | InsufficientScopeError | ResponseError]:
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
) -> Response[Any | InsufficientScopeError | ResponseError]:
    """Delete a signal channel of yours

     Deletes the channel. Its subscriptions end (`state: ENDED`), notices already published and not yet
    delivered
    are not delivered (`SKIPPED`), and its `webhookUrl` stops publishing. Owner only. Deleting it again
    is not an
    error.

    Args:
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InsufficientScopeError | ResponseError]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | InsufficientScopeError | ResponseError | None:
    """Delete a signal channel of yours

     Deletes the channel. Its subscriptions end (`state: ENDED`), notices already published and not yet
    delivered
    are not delivered (`SKIPPED`), and its `webhookUrl` stops publishing. Owner only. Deleting it again
    is not an
    error.

    Args:
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InsufficientScopeError | ResponseError
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | InsufficientScopeError | ResponseError]:
    """Delete a signal channel of yours

     Deletes the channel. Its subscriptions end (`state: ENDED`), notices already published and not yet
    delivered
    are not delivered (`SKIPPED`), and its `webhookUrl` stops publishing. Owner only. Deleting it again
    is not an
    error.

    Args:
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InsufficientScopeError | ResponseError]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | InsufficientScopeError | ResponseError | None:
    """Delete a signal channel of yours

     Deletes the channel. Its subscriptions end (`state: ENDED`), notices already published and not yet
    delivered
    are not delivered (`SKIPPED`), and its `webhookUrl` stops publishing. Owner only. Deleting it again
    is not an
    error.

    Args:
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InsufficientScopeError | ResponseError
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
        )
    ).parsed
