from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.live_stream_url import LiveStreamUrl
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    run_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/live/{run_id}/stream".format(
            run_id=quote(str(run_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InsufficientScopeError | LiveStreamUrl | ResponseError | None:
    if response.status_code == 200:
        response_200 = LiveStreamUrl.from_dict(response.json())

        return response_200

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
) -> Response[InsufficientScopeError | LiveStreamUrl | ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[InsufficientScopeError | LiveStreamUrl | ResponseError]:
    r"""Rotate a run's stream URL

     Gives a run a **new** stream URL and retires the old one: connections open on the old URL are closed
    within about 15 seconds and the old URL answers `404` from then on. Use it when the URL may have
    leaked.
    Owner only, and only for a run that is running and was started with `stream: true` (the URL cannot
    be added
    to a run later, and a revoked one cannot be brought back). The plan is checked again: a plan that
    may not
    broadcast gets `429`.

    See the \"Live execution\" guide, \"A plain WebSocket stream of a run\".

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | LiveStreamUrl | ResponseError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> InsufficientScopeError | LiveStreamUrl | ResponseError | None:
    r"""Rotate a run's stream URL

     Gives a run a **new** stream URL and retires the old one: connections open on the old URL are closed
    within about 15 seconds and the old URL answers `404` from then on. Use it when the URL may have
    leaked.
    Owner only, and only for a run that is running and was started with `stream: true` (the URL cannot
    be added
    to a run later, and a revoked one cannot be brought back). The plan is checked again: a plan that
    may not
    broadcast gets `429`.

    See the \"Live execution\" guide, \"A plain WebSocket stream of a run\".

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | LiveStreamUrl | ResponseError
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[InsufficientScopeError | LiveStreamUrl | ResponseError]:
    r"""Rotate a run's stream URL

     Gives a run a **new** stream URL and retires the old one: connections open on the old URL are closed
    within about 15 seconds and the old URL answers `404` from then on. Use it when the URL may have
    leaked.
    Owner only, and only for a run that is running and was started with `stream: true` (the URL cannot
    be added
    to a run later, and a revoked one cannot be brought back). The plan is checked again: a plan that
    may not
    broadcast gets `429`.

    See the \"Live execution\" guide, \"A plain WebSocket stream of a run\".

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | LiveStreamUrl | ResponseError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> InsufficientScopeError | LiveStreamUrl | ResponseError | None:
    r"""Rotate a run's stream URL

     Gives a run a **new** stream URL and retires the old one: connections open on the old URL are closed
    within about 15 seconds and the old URL answers `404` from then on. Use it when the URL may have
    leaked.
    Owner only, and only for a run that is running and was started with `stream: true` (the URL cannot
    be added
    to a run later, and a revoked one cannot be brought back). The plan is checked again: a plan that
    may not
    broadcast gets `429`.

    See the \"Live execution\" guide, \"A plain WebSocket stream of a run\".

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | LiveStreamUrl | ResponseError
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
        )
    ).parsed
