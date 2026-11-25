from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection import Collection
from ...models.collection_update_request import CollectionUpdateRequest
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    collection_id: str,
    *,
    body: CollectionUpdateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/collections/{collection_id}".format(
            collection_id=quote(str(collection_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Collection | InsufficientScopeError | ResponseError | None:
    if response.status_code == 200:
        response_200 = Collection.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = ResponseError.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = ResponseError.from_dict(response.json())

        return response_413

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
    collection_id: str,
    *,
    client: AuthenticatedClient,
    body: CollectionUpdateRequest,
) -> Response[Collection | InsufficientScopeError | ResponseError]:
    """Rename a collection or change its description

     Send `name`, `description` or both. A field you leave out is left as it is. `description:
    null`, or a blank one, removes the description; `name` cannot be `null`. The limits are
    those of creation. A body with neither field is `400`; any other field is ignored. Answers
    the collection as it is after the change. A rename frees the old name at once.

    Args:
        collection_id (str):  Example: dc_3f9a1c2e7b0d4a5f.
        body (CollectionUpdateRequest): At least one of the two fields. A field left out is not
            changed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Collection | InsufficientScopeError | ResponseError]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    *,
    client: AuthenticatedClient,
    body: CollectionUpdateRequest,
) -> Collection | InsufficientScopeError | ResponseError | None:
    """Rename a collection or change its description

     Send `name`, `description` or both. A field you leave out is left as it is. `description:
    null`, or a blank one, removes the description; `name` cannot be `null`. The limits are
    those of creation. A body with neither field is `400`; any other field is ignored. Answers
    the collection as it is after the change. A rename frees the old name at once.

    Args:
        collection_id (str):  Example: dc_3f9a1c2e7b0d4a5f.
        body (CollectionUpdateRequest): At least one of the two fields. A field left out is not
            changed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Collection | InsufficientScopeError | ResponseError
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient,
    body: CollectionUpdateRequest,
) -> Response[Collection | InsufficientScopeError | ResponseError]:
    """Rename a collection or change its description

     Send `name`, `description` or both. A field you leave out is left as it is. `description:
    null`, or a blank one, removes the description; `name` cannot be `null`. The limits are
    those of creation. A body with neither field is `400`; any other field is ignored. Answers
    the collection as it is after the change. A rename frees the old name at once.

    Args:
        collection_id (str):  Example: dc_3f9a1c2e7b0d4a5f.
        body (CollectionUpdateRequest): At least one of the two fields. A field left out is not
            changed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Collection | InsufficientScopeError | ResponseError]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    *,
    client: AuthenticatedClient,
    body: CollectionUpdateRequest,
) -> Collection | InsufficientScopeError | ResponseError | None:
    """Rename a collection or change its description

     Send `name`, `description` or both. A field you leave out is left as it is. `description:
    null`, or a blank one, removes the description; `name` cannot be `null`. The limits are
    those of creation. A body with neither field is `400`; any other field is ignored. Answers
    the collection as it is after the change. A rename frees the old name at once.

    Args:
        collection_id (str):  Example: dc_3f9a1c2e7b0d4a5f.
        body (CollectionUpdateRequest): At least one of the two fields. A field left out is not
            changed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Collection | InsufficientScopeError | ResponseError
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            body=body,
        )
    ).parsed
