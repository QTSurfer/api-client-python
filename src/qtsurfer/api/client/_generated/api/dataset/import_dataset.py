from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_import_created import DatasetImportCreated
from ...models.dataset_import_request import DatasetImportRequest
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    *,
    body: DatasetImportRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/datasets/imports",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatasetImportCreated | ResponseError | None:
    if response.status_code == 202:
        response_202 = DatasetImportCreated.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ResponseError.from_dict(response.json())

        return response_400

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
) -> Response[DatasetImportCreated | ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DatasetImportRequest,
) -> Response[DatasetImportCreated | ResponseError]:
    """Create a dataset by importing history instead of uploading it

     A second way to get data into a dataset, alongside `POST /datasets`: instead of `PUT`ting a
    file yourself, ask the API to go fetch history on your behalf. Creates the dataset and
    starts the fetch in the same call — there is no separate upload step, and the result lands
    as a dataset version indistinguishable from an uploaded one once it's ready. Poll
    `GET /datasets/{datasetId}/imports/{importId}` for progress.

    `type` selects the source. `dex` — history over a pool/pair's own on-chain market — is the
    only value today; other source types join this same endpoint later.

    A `dex` import has two data shapes, chosen by the top-level `cadence`:

    * Omitted/blank (default) — on-chain swap history, replayed directly from the pool/pair's
      own chain. Cadence is native, not resampled: each swap keeps the timestamp it happened
      at rather than being bucketed into candles, so the resulting version's `cadence` is `rt`
      unless the swaps happen to sit on a fixed grid (see `DatasetVersion.cadence`).
    * One of `1s` / `1m` / `5m` — pre-aggregated candles at that width instead of raw trades.
      The resulting dataset's `type` is `klines`, not `ticker`. Not every network supports every
      cadence yet — an unsupported combination fails asynchronously, same as an unresolvable
      pool (see the `failed` status on the poll endpoint below).

    Args:
        body (DatasetImportRequest): `POST /datasets/imports`'s request body. A common block plus
            one type-specific block,
            selected by `type` — `dex` is the only value today.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetImportCreated | ResponseError]
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
    body: DatasetImportRequest,
) -> DatasetImportCreated | ResponseError | None:
    """Create a dataset by importing history instead of uploading it

     A second way to get data into a dataset, alongside `POST /datasets`: instead of `PUT`ting a
    file yourself, ask the API to go fetch history on your behalf. Creates the dataset and
    starts the fetch in the same call — there is no separate upload step, and the result lands
    as a dataset version indistinguishable from an uploaded one once it's ready. Poll
    `GET /datasets/{datasetId}/imports/{importId}` for progress.

    `type` selects the source. `dex` — history over a pool/pair's own on-chain market — is the
    only value today; other source types join this same endpoint later.

    A `dex` import has two data shapes, chosen by the top-level `cadence`:

    * Omitted/blank (default) — on-chain swap history, replayed directly from the pool/pair's
      own chain. Cadence is native, not resampled: each swap keeps the timestamp it happened
      at rather than being bucketed into candles, so the resulting version's `cadence` is `rt`
      unless the swaps happen to sit on a fixed grid (see `DatasetVersion.cadence`).
    * One of `1s` / `1m` / `5m` — pre-aggregated candles at that width instead of raw trades.
      The resulting dataset's `type` is `klines`, not `ticker`. Not every network supports every
      cadence yet — an unsupported combination fails asynchronously, same as an unresolvable
      pool (see the `failed` status on the poll endpoint below).

    Args:
        body (DatasetImportRequest): `POST /datasets/imports`'s request body. A common block plus
            one type-specific block,
            selected by `type` — `dex` is the only value today.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetImportCreated | ResponseError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DatasetImportRequest,
) -> Response[DatasetImportCreated | ResponseError]:
    """Create a dataset by importing history instead of uploading it

     A second way to get data into a dataset, alongside `POST /datasets`: instead of `PUT`ting a
    file yourself, ask the API to go fetch history on your behalf. Creates the dataset and
    starts the fetch in the same call — there is no separate upload step, and the result lands
    as a dataset version indistinguishable from an uploaded one once it's ready. Poll
    `GET /datasets/{datasetId}/imports/{importId}` for progress.

    `type` selects the source. `dex` — history over a pool/pair's own on-chain market — is the
    only value today; other source types join this same endpoint later.

    A `dex` import has two data shapes, chosen by the top-level `cadence`:

    * Omitted/blank (default) — on-chain swap history, replayed directly from the pool/pair's
      own chain. Cadence is native, not resampled: each swap keeps the timestamp it happened
      at rather than being bucketed into candles, so the resulting version's `cadence` is `rt`
      unless the swaps happen to sit on a fixed grid (see `DatasetVersion.cadence`).
    * One of `1s` / `1m` / `5m` — pre-aggregated candles at that width instead of raw trades.
      The resulting dataset's `type` is `klines`, not `ticker`. Not every network supports every
      cadence yet — an unsupported combination fails asynchronously, same as an unresolvable
      pool (see the `failed` status on the poll endpoint below).

    Args:
        body (DatasetImportRequest): `POST /datasets/imports`'s request body. A common block plus
            one type-specific block,
            selected by `type` — `dex` is the only value today.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetImportCreated | ResponseError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DatasetImportRequest,
) -> DatasetImportCreated | ResponseError | None:
    """Create a dataset by importing history instead of uploading it

     A second way to get data into a dataset, alongside `POST /datasets`: instead of `PUT`ting a
    file yourself, ask the API to go fetch history on your behalf. Creates the dataset and
    starts the fetch in the same call — there is no separate upload step, and the result lands
    as a dataset version indistinguishable from an uploaded one once it's ready. Poll
    `GET /datasets/{datasetId}/imports/{importId}` for progress.

    `type` selects the source. `dex` — history over a pool/pair's own on-chain market — is the
    only value today; other source types join this same endpoint later.

    A `dex` import has two data shapes, chosen by the top-level `cadence`:

    * Omitted/blank (default) — on-chain swap history, replayed directly from the pool/pair's
      own chain. Cadence is native, not resampled: each swap keeps the timestamp it happened
      at rather than being bucketed into candles, so the resulting version's `cadence` is `rt`
      unless the swaps happen to sit on a fixed grid (see `DatasetVersion.cadence`).
    * One of `1s` / `1m` / `5m` — pre-aggregated candles at that width instead of raw trades.
      The resulting dataset's `type` is `klines`, not `ticker`. Not every network supports every
      cadence yet — an unsupported combination fails asynchronously, same as an unresolvable
      pool (see the `failed` status on the poll endpoint below).

    Args:
        body (DatasetImportRequest): `POST /datasets/imports`'s request body. A common block plus
            one type-specific block,
            selected by `type` — `dex` is the only value today.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetImportCreated | ResponseError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
