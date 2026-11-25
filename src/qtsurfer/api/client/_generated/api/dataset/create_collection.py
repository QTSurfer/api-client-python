from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection import Collection
from ...models.collection_create_request import CollectionCreateRequest
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    *,
    body: CollectionCreateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/collections",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Collection | InsufficientScopeError | ResponseError | None:
    if response.status_code == 201:
        response_201 = Collection.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ResponseError.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = InsufficientScopeError.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = ResponseError.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = ResponseError.from_dict(response.json())

        return response_413

    if response.status_code == 429:
        response_429 = ResponseError.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Collection | InsufficientScopeError | ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CollectionCreateRequest,
) -> Response[Collection | InsufficientScopeError | ResponseError]:
    """Create a collection

     Creates an empty collection, a folder to keep datasets in. A collection is one level deep:
    it holds datasets and nothing else. The Datasets guide explains how collections work.

    `name` is required; it is trimmed, and the trimmed text has 1 to 100 characters. It is
    unique among your collections, compared as written (`Majors` and `majors` are two names).
    `description` is optional, up to 500 characters; a blank one is the same as none. The `201`
    is the collection, with `datasetCount` `0`.

    Args:
        body (CollectionCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Collection | InsufficientScopeError | ResponseError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CollectionCreateRequest,
) -> Collection | InsufficientScopeError | ResponseError | None:
    """Create a collection

     Creates an empty collection, a folder to keep datasets in. A collection is one level deep:
    it holds datasets and nothing else. The Datasets guide explains how collections work.

    `name` is required; it is trimmed, and the trimmed text has 1 to 100 characters. It is
    unique among your collections, compared as written (`Majors` and `majors` are two names).
    `description` is optional, up to 500 characters; a blank one is the same as none. The `201`
    is the collection, with `datasetCount` `0`.

    Args:
        body (CollectionCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Collection | InsufficientScopeError | ResponseError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CollectionCreateRequest,
) -> Response[Collection | InsufficientScopeError | ResponseError]:
    """Create a collection

     Creates an empty collection, a folder to keep datasets in. A collection is one level deep:
    it holds datasets and nothing else. The Datasets guide explains how collections work.

    `name` is required; it is trimmed, and the trimmed text has 1 to 100 characters. It is
    unique among your collections, compared as written (`Majors` and `majors` are two names).
    `description` is optional, up to 500 characters; a blank one is the same as none. The `201`
    is the collection, with `datasetCount` `0`.

    Args:
        body (CollectionCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Collection | InsufficientScopeError | ResponseError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CollectionCreateRequest,
) -> Collection | InsufficientScopeError | ResponseError | None:
    """Create a collection

     Creates an empty collection, a folder to keep datasets in. A collection is one level deep:
    it holds datasets and nothing else. The Datasets guide explains how collections work.

    `name` is required; it is trimmed, and the trimmed text has 1 to 100 characters. It is
    unique among your collections, compared as written (`Majors` and `majors` are two names).
    `description` is optional, up to 500 characters; a blank one is the same as none. The `201`
    is the collection, with `datasetCount` `0`.

    Args:
        body (CollectionCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Collection | InsufficientScopeError | ResponseError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
