from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_move_request import DatasetMoveRequest
from ...models.dataset_with_links import DatasetWithLinks
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    dataset_id: str,
    *,
    body: DatasetMoveRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/datasets/{dataset_id}".format(
            dataset_id=quote(str(dataset_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatasetWithLinks | InsufficientScopeError | ResponseError | None:
    if response.status_code == 200:
        response_200 = DatasetWithLinks.from_dict(response.json())

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

    if response.status_code == 413:
        response_413 = ResponseError.from_dict(response.json())

        return response_413

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatasetWithLinks | InsufficientScopeError | ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    body: DatasetMoveRequest,
) -> Response[DatasetWithLinks | InsufficientScopeError | ResponseError]:
    r"""Move a dataset into a collection, or back to the root

     The body is exactly `{\"collectionId\": \"dc_...\"}` to move the dataset into that collection,
    or `{\"collectionId\": null}` to take it out of its collection. Nothing else about a dataset
    can be changed here: a body without `collectionId`, or with any other field, is `400`, so a
    field is never silently ignored. Any `type` can go in any collection. The dataset keeps its
    `name`, which stays unique among all your datasets, whatever collection each is in.

    Answers the dataset, as `GET /datasets/{datasetId}` does. Moving a dataset to where it
    already is succeeds and changes nothing.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.
        body (DatasetMoveRequest): The body of `PATCH /datasets/{datasetId}`: exactly one field,
            `collectionId`. A body
            without it, or with any other field, is `400`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetWithLinks | InsufficientScopeError | ResponseError]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    body: DatasetMoveRequest,
) -> DatasetWithLinks | InsufficientScopeError | ResponseError | None:
    r"""Move a dataset into a collection, or back to the root

     The body is exactly `{\"collectionId\": \"dc_...\"}` to move the dataset into that collection,
    or `{\"collectionId\": null}` to take it out of its collection. Nothing else about a dataset
    can be changed here: a body without `collectionId`, or with any other field, is `400`, so a
    field is never silently ignored. Any `type` can go in any collection. The dataset keeps its
    `name`, which stays unique among all your datasets, whatever collection each is in.

    Answers the dataset, as `GET /datasets/{datasetId}` does. Moving a dataset to where it
    already is succeeds and changes nothing.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.
        body (DatasetMoveRequest): The body of `PATCH /datasets/{datasetId}`: exactly one field,
            `collectionId`. A body
            without it, or with any other field, is `400`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetWithLinks | InsufficientScopeError | ResponseError
    """

    return sync_detailed(
        dataset_id=dataset_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    body: DatasetMoveRequest,
) -> Response[DatasetWithLinks | InsufficientScopeError | ResponseError]:
    r"""Move a dataset into a collection, or back to the root

     The body is exactly `{\"collectionId\": \"dc_...\"}` to move the dataset into that collection,
    or `{\"collectionId\": null}` to take it out of its collection. Nothing else about a dataset
    can be changed here: a body without `collectionId`, or with any other field, is `400`, so a
    field is never silently ignored. Any `type` can go in any collection. The dataset keeps its
    `name`, which stays unique among all your datasets, whatever collection each is in.

    Answers the dataset, as `GET /datasets/{datasetId}` does. Moving a dataset to where it
    already is succeeds and changes nothing.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.
        body (DatasetMoveRequest): The body of `PATCH /datasets/{datasetId}`: exactly one field,
            `collectionId`. A body
            without it, or with any other field, is `400`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetWithLinks | InsufficientScopeError | ResponseError]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    body: DatasetMoveRequest,
) -> DatasetWithLinks | InsufficientScopeError | ResponseError | None:
    r"""Move a dataset into a collection, or back to the root

     The body is exactly `{\"collectionId\": \"dc_...\"}` to move the dataset into that collection,
    or `{\"collectionId\": null}` to take it out of its collection. Nothing else about a dataset
    can be changed here: a body without `collectionId`, or with any other field, is `400`, so a
    field is never silently ignored. Any `type` can go in any collection. The dataset keeps its
    `name`, which stays unique among all your datasets, whatever collection each is in.

    Answers the dataset, as `GET /datasets/{datasetId}` does. Moving a dataset to where it
    already is succeeds and changes nothing.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.
        body (DatasetMoveRequest): The body of `PATCH /datasets/{datasetId}`: exactly one field,
            `collectionId`. A body
            without it, or with any other field, is `400`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetWithLinks | InsufficientScopeError | ResponseError
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            client=client,
            body=body,
        )
    ).parsed
