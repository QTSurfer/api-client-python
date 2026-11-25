from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection_deleted import CollectionDeleted
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    collection_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/collections/{collection_id}".format(
            collection_id=quote(str(collection_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CollectionDeleted | InsufficientScopeError | ResponseError | None:
    if response.status_code == 200:
        response_200 = CollectionDeleted.from_dict(response.json())

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
) -> Response[CollectionDeleted | InsufficientScopeError | ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CollectionDeleted | InsufficientScopeError | ResponseError]:
    """Delete a collection

     Deletes the collection for good; its name is free again at once. **The datasets in it are
    kept**: they go back to the root, as if they had never been in a collection. Nothing else
    about them changes.

    Args:
        collection_id (str):  Example: dc_3f9a1c2e7b0d4a5f.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CollectionDeleted | InsufficientScopeError | ResponseError]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    *,
    client: AuthenticatedClient,
) -> CollectionDeleted | InsufficientScopeError | ResponseError | None:
    """Delete a collection

     Deletes the collection for good; its name is free again at once. **The datasets in it are
    kept**: they go back to the root, as if they had never been in a collection. Nothing else
    about them changes.

    Args:
        collection_id (str):  Example: dc_3f9a1c2e7b0d4a5f.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CollectionDeleted | InsufficientScopeError | ResponseError
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CollectionDeleted | InsufficientScopeError | ResponseError]:
    """Delete a collection

     Deletes the collection for good; its name is free again at once. **The datasets in it are
    kept**: they go back to the root, as if they had never been in a collection. Nothing else
    about them changes.

    Args:
        collection_id (str):  Example: dc_3f9a1c2e7b0d4a5f.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CollectionDeleted | InsufficientScopeError | ResponseError]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    *,
    client: AuthenticatedClient,
) -> CollectionDeleted | InsufficientScopeError | ResponseError | None:
    """Delete a collection

     Deletes the collection for good; its name is free again at once. **The datasets in it are
    kept**: they go back to the root, as if they had never been in a collection. Nothing else
    about them changes.

    Args:
        collection_id (str):  Example: dc_3f9a1c2e7b0d4a5f.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CollectionDeleted | InsufficientScopeError | ResponseError
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
        )
    ).parsed
