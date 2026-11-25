from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection_list import CollectionList
from ...models.insufficient_scope_error import InsufficientScopeError
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/collections",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CollectionList | InsufficientScopeError | None:
    if response.status_code == 200:
        response_200 = CollectionList.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = InsufficientScopeError.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CollectionList | InsufficientScopeError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[CollectionList | InsufficientScopeError]:
    """List your collections

     Every collection you have, in one response: there is no paging. Ordered by `name`, then by
    `collectionId`. Never a `404`: an empty array if you have none. A collection is deleted for
    good, so there is no `includeDeleted`: one that is not in the list no longer exists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CollectionList | InsufficientScopeError]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> CollectionList | InsufficientScopeError | None:
    """List your collections

     Every collection you have, in one response: there is no paging. Ordered by `name`, then by
    `collectionId`. Never a `404`: an empty array if you have none. A collection is deleted for
    good, so there is no `includeDeleted`: one that is not in the list no longer exists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CollectionList | InsufficientScopeError
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[CollectionList | InsufficientScopeError]:
    """List your collections

     Every collection you have, in one response: there is no paging. Ordered by `name`, then by
    `collectionId`. Never a `404`: an empty array if you have none. A collection is deleted for
    good, so there is no `includeDeleted`: one that is not in the list no longer exists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CollectionList | InsufficientScopeError]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> CollectionList | InsufficientScopeError | None:
    """List your collections

     Every collection you have, in one response: there is no paging. Ordered by `name`, then by
    `collectionId`. Never a `404`: an empty array if you have none. A collection is deleted for
    good, so there is no `includeDeleted`: one that is not in the list no longer exists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CollectionList | InsufficientScopeError
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
