from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_import_created import DatasetImportCreated
from ...models.dataset_import_request import DatasetImportRequest
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.plan_required_error import PlanRequiredError
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
) -> DatasetImportCreated | InsufficientScopeError | PlanRequiredError | ResponseError | None:
    if response.status_code == 202:
        response_202 = DatasetImportCreated.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ResponseError.from_dict(response.json())

        return response_400

    if response.status_code == 402:
        response_402 = PlanRequiredError.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = InsufficientScopeError.from_dict(response.json())

        return response_403

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
) -> Response[DatasetImportCreated | InsufficientScopeError | PlanRequiredError | ResponseError]:
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
) -> Response[DatasetImportCreated | InsufficientScopeError | PlanRequiredError | ResponseError]:
    r"""Create a dataset by importing history instead of uploading it

     A second way to get data into a dataset, alongside `POST /datasets`: instead of `PUT`ting a
    file yourself, ask the API to go fetch history on your behalf. Creates the dataset and
    starts the fetch in the same call — there is no separate upload step, and the result lands
    as a dataset version indistinguishable from an uploaded one once it's ready. Poll
    `GET /datasets/{datasetId}/imports/{importId}` for progress.

    `type` selects the kind of venue the history comes from, with the same two values as the
    `venueType` of `GET /exchanges`: `dex` — history over a pool/pair's own on-chain market —
    and `cex` — the history of a centralized exchange's market, kept by the platform. Each
    has its own block (`dex`, `cex`). The exchange id of a `cex` import has to be a centralized
    exchange of `GET /exchanges`; a decentralized one (`robinhood`, say) is `400`, and is imported
    with `type: dex`.

    A `cex` import covers one instrument over a range: the API reads that range of the
    exchange's history, builds the bars of the requested `cadence` from the finest data it has
    for it, and stores the result as a dataset version, exactly as for an upload. `cex.dataType`
    picks tickers or klines and is also the resulting dataset's `type`. The range is capped by
    your tier like any import (`maxImportRangeHours` of `GET /account`).

    **An import is held to your plan's cadences,** the same ones as the preparation of an
    exchange's data (the \"Cadences by plan\" section of the Backtests guide). A `cadence` your plan
    does not include is `402`; a
    request that names none gets the plan's default; any other cadence your plan includes can be
    asked for. The `202` says the `cadence` the dataset is built at. An upload is not held to
    this: it is stored at the cadence detected in it.

    A `dex` import has two data shapes:

    * Candles at the `cadence` you ask for, or at the plan's default when you ask for none. Every
      cadence of the list is built, from the nearest width the source serves. The resulting dataset's
    `type` is `klines`, not `ticker`, and
      `dex.id` / `dex.version` are not needed. Not every network supports candles yet — an
      unsupported combination fails asynchronously, same as an unresolvable pool (see the
      `failed` status on the poll endpoint below).
    * On-chain swap history (per-trade data), replayed directly from the pool/pair's own chain —
      **only on a plan that includes the native rate of a source, and when `cadence` is omitted**.
      Cadence is native, not resampled: each swap
      keeps the timestamp it happened at rather than being bucketed into candles, so the
      resulting version's `cadence` is `rt` unless the swaps happen to sit on a fixed grid (see
      `DatasetVersion.cadence`). Needs `dex.id` and `dex.version`.

    Args:
        body (DatasetImportRequest): `POST /datasets/imports`'s request body. A common block plus
            one type-specific block,
            selected by `type`: `dex` (block `dex`) or `cex` (block `cex`), the two `venueType`s of
            `GET /exchanges`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetImportCreated | InsufficientScopeError | PlanRequiredError | ResponseError]
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
) -> DatasetImportCreated | InsufficientScopeError | PlanRequiredError | ResponseError | None:
    r"""Create a dataset by importing history instead of uploading it

     A second way to get data into a dataset, alongside `POST /datasets`: instead of `PUT`ting a
    file yourself, ask the API to go fetch history on your behalf. Creates the dataset and
    starts the fetch in the same call — there is no separate upload step, and the result lands
    as a dataset version indistinguishable from an uploaded one once it's ready. Poll
    `GET /datasets/{datasetId}/imports/{importId}` for progress.

    `type` selects the kind of venue the history comes from, with the same two values as the
    `venueType` of `GET /exchanges`: `dex` — history over a pool/pair's own on-chain market —
    and `cex` — the history of a centralized exchange's market, kept by the platform. Each
    has its own block (`dex`, `cex`). The exchange id of a `cex` import has to be a centralized
    exchange of `GET /exchanges`; a decentralized one (`robinhood`, say) is `400`, and is imported
    with `type: dex`.

    A `cex` import covers one instrument over a range: the API reads that range of the
    exchange's history, builds the bars of the requested `cadence` from the finest data it has
    for it, and stores the result as a dataset version, exactly as for an upload. `cex.dataType`
    picks tickers or klines and is also the resulting dataset's `type`. The range is capped by
    your tier like any import (`maxImportRangeHours` of `GET /account`).

    **An import is held to your plan's cadences,** the same ones as the preparation of an
    exchange's data (the \"Cadences by plan\" section of the Backtests guide). A `cadence` your plan
    does not include is `402`; a
    request that names none gets the plan's default; any other cadence your plan includes can be
    asked for. The `202` says the `cadence` the dataset is built at. An upload is not held to
    this: it is stored at the cadence detected in it.

    A `dex` import has two data shapes:

    * Candles at the `cadence` you ask for, or at the plan's default when you ask for none. Every
      cadence of the list is built, from the nearest width the source serves. The resulting dataset's
    `type` is `klines`, not `ticker`, and
      `dex.id` / `dex.version` are not needed. Not every network supports candles yet — an
      unsupported combination fails asynchronously, same as an unresolvable pool (see the
      `failed` status on the poll endpoint below).
    * On-chain swap history (per-trade data), replayed directly from the pool/pair's own chain —
      **only on a plan that includes the native rate of a source, and when `cadence` is omitted**.
      Cadence is native, not resampled: each swap
      keeps the timestamp it happened at rather than being bucketed into candles, so the
      resulting version's `cadence` is `rt` unless the swaps happen to sit on a fixed grid (see
      `DatasetVersion.cadence`). Needs `dex.id` and `dex.version`.

    Args:
        body (DatasetImportRequest): `POST /datasets/imports`'s request body. A common block plus
            one type-specific block,
            selected by `type`: `dex` (block `dex`) or `cex` (block `cex`), the two `venueType`s of
            `GET /exchanges`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetImportCreated | InsufficientScopeError | PlanRequiredError | ResponseError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DatasetImportRequest,
) -> Response[DatasetImportCreated | InsufficientScopeError | PlanRequiredError | ResponseError]:
    r"""Create a dataset by importing history instead of uploading it

     A second way to get data into a dataset, alongside `POST /datasets`: instead of `PUT`ting a
    file yourself, ask the API to go fetch history on your behalf. Creates the dataset and
    starts the fetch in the same call — there is no separate upload step, and the result lands
    as a dataset version indistinguishable from an uploaded one once it's ready. Poll
    `GET /datasets/{datasetId}/imports/{importId}` for progress.

    `type` selects the kind of venue the history comes from, with the same two values as the
    `venueType` of `GET /exchanges`: `dex` — history over a pool/pair's own on-chain market —
    and `cex` — the history of a centralized exchange's market, kept by the platform. Each
    has its own block (`dex`, `cex`). The exchange id of a `cex` import has to be a centralized
    exchange of `GET /exchanges`; a decentralized one (`robinhood`, say) is `400`, and is imported
    with `type: dex`.

    A `cex` import covers one instrument over a range: the API reads that range of the
    exchange's history, builds the bars of the requested `cadence` from the finest data it has
    for it, and stores the result as a dataset version, exactly as for an upload. `cex.dataType`
    picks tickers or klines and is also the resulting dataset's `type`. The range is capped by
    your tier like any import (`maxImportRangeHours` of `GET /account`).

    **An import is held to your plan's cadences,** the same ones as the preparation of an
    exchange's data (the \"Cadences by plan\" section of the Backtests guide). A `cadence` your plan
    does not include is `402`; a
    request that names none gets the plan's default; any other cadence your plan includes can be
    asked for. The `202` says the `cadence` the dataset is built at. An upload is not held to
    this: it is stored at the cadence detected in it.

    A `dex` import has two data shapes:

    * Candles at the `cadence` you ask for, or at the plan's default when you ask for none. Every
      cadence of the list is built, from the nearest width the source serves. The resulting dataset's
    `type` is `klines`, not `ticker`, and
      `dex.id` / `dex.version` are not needed. Not every network supports candles yet — an
      unsupported combination fails asynchronously, same as an unresolvable pool (see the
      `failed` status on the poll endpoint below).
    * On-chain swap history (per-trade data), replayed directly from the pool/pair's own chain —
      **only on a plan that includes the native rate of a source, and when `cadence` is omitted**.
      Cadence is native, not resampled: each swap
      keeps the timestamp it happened at rather than being bucketed into candles, so the
      resulting version's `cadence` is `rt` unless the swaps happen to sit on a fixed grid (see
      `DatasetVersion.cadence`). Needs `dex.id` and `dex.version`.

    Args:
        body (DatasetImportRequest): `POST /datasets/imports`'s request body. A common block plus
            one type-specific block,
            selected by `type`: `dex` (block `dex`) or `cex` (block `cex`), the two `venueType`s of
            `GET /exchanges`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetImportCreated | InsufficientScopeError | PlanRequiredError | ResponseError]
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
) -> DatasetImportCreated | InsufficientScopeError | PlanRequiredError | ResponseError | None:
    r"""Create a dataset by importing history instead of uploading it

     A second way to get data into a dataset, alongside `POST /datasets`: instead of `PUT`ting a
    file yourself, ask the API to go fetch history on your behalf. Creates the dataset and
    starts the fetch in the same call — there is no separate upload step, and the result lands
    as a dataset version indistinguishable from an uploaded one once it's ready. Poll
    `GET /datasets/{datasetId}/imports/{importId}` for progress.

    `type` selects the kind of venue the history comes from, with the same two values as the
    `venueType` of `GET /exchanges`: `dex` — history over a pool/pair's own on-chain market —
    and `cex` — the history of a centralized exchange's market, kept by the platform. Each
    has its own block (`dex`, `cex`). The exchange id of a `cex` import has to be a centralized
    exchange of `GET /exchanges`; a decentralized one (`robinhood`, say) is `400`, and is imported
    with `type: dex`.

    A `cex` import covers one instrument over a range: the API reads that range of the
    exchange's history, builds the bars of the requested `cadence` from the finest data it has
    for it, and stores the result as a dataset version, exactly as for an upload. `cex.dataType`
    picks tickers or klines and is also the resulting dataset's `type`. The range is capped by
    your tier like any import (`maxImportRangeHours` of `GET /account`).

    **An import is held to your plan's cadences,** the same ones as the preparation of an
    exchange's data (the \"Cadences by plan\" section of the Backtests guide). A `cadence` your plan
    does not include is `402`; a
    request that names none gets the plan's default; any other cadence your plan includes can be
    asked for. The `202` says the `cadence` the dataset is built at. An upload is not held to
    this: it is stored at the cadence detected in it.

    A `dex` import has two data shapes:

    * Candles at the `cadence` you ask for, or at the plan's default when you ask for none. Every
      cadence of the list is built, from the nearest width the source serves. The resulting dataset's
    `type` is `klines`, not `ticker`, and
      `dex.id` / `dex.version` are not needed. Not every network supports candles yet — an
      unsupported combination fails asynchronously, same as an unresolvable pool (see the
      `failed` status on the poll endpoint below).
    * On-chain swap history (per-trade data), replayed directly from the pool/pair's own chain —
      **only on a plan that includes the native rate of a source, and when `cadence` is omitted**.
      Cadence is native, not resampled: each swap
      keeps the timestamp it happened at rather than being bucketed into candles, so the
      resulting version's `cadence` is `rt` unless the swaps happen to sit on a fixed grid (see
      `DatasetVersion.cadence`). Needs `dex.id` and `dex.version`.

    Args:
        body (DatasetImportRequest): `POST /datasets/imports`'s request body. A common block plus
            one type-specific block,
            selected by `type`: `dex` (block `dex`) or `cex` (block `cex`), the two `venueType`s of
            `GET /exchanges`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetImportCreated | InsufficientScopeError | PlanRequiredError | ResponseError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
