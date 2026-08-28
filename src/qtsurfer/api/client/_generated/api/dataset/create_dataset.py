from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_dataset_body import CreateDatasetBody
from ...models.dataset_created import DatasetCreated
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    *,
    body: CreateDatasetBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/datasets",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatasetCreated | ResponseError | None:
    if response.status_code == 201:
        response_201 = DatasetCreated.from_dict(response.json())

        return response_201

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
) -> Response[DatasetCreated | ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateDatasetBody,
) -> Response[DatasetCreated | ResponseError]:
    r"""Create a dataset and get a URL to upload it to

     Creates a dataset AND its first upload session in one call — a presigned URL your client
    PUTs the file to directly, no API credentials involved in that PUT. Call
    `POST /datasets/{datasetId}/uploads/{uploadId}/finalize` once the upload completes to kick
    off ingest.

    Losing this response loses nothing: calling this dataset's
    `POST /datasets/{datasetId}/uploads` returns the very same upload session again rather than
    opening a new one, as long as nothing has been finalized against it yet.

    v1 is ticker data only — `type` is not a request field, it is always `\"ticker\"` in the
    response. `instrument` must be a plain spot pair (`BASE/QUOTE`, exactly one `/`); derivative
    forms (e.g. `BTC/USDT:USDT`) are rejected.

    **Upload format.** A CSV with a header row. Required columns: `timestamp` (ISO-8601, or
    numeric epoch seconds/millis/micros — detected from the first row, then enforced for every
    later row), `close`. Optional columns: `open`, `high`, `low`, `volume`, `quoteVolume`,
    `bid`, `bidSize`, `ask`, `askSize`. Cadence and timestamp unit are discovered from the data,
    not declared.

    Args:
        body (CreateDatasetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetCreated | ResponseError]
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
    body: CreateDatasetBody,
) -> DatasetCreated | ResponseError | None:
    r"""Create a dataset and get a URL to upload it to

     Creates a dataset AND its first upload session in one call — a presigned URL your client
    PUTs the file to directly, no API credentials involved in that PUT. Call
    `POST /datasets/{datasetId}/uploads/{uploadId}/finalize` once the upload completes to kick
    off ingest.

    Losing this response loses nothing: calling this dataset's
    `POST /datasets/{datasetId}/uploads` returns the very same upload session again rather than
    opening a new one, as long as nothing has been finalized against it yet.

    v1 is ticker data only — `type` is not a request field, it is always `\"ticker\"` in the
    response. `instrument` must be a plain spot pair (`BASE/QUOTE`, exactly one `/`); derivative
    forms (e.g. `BTC/USDT:USDT`) are rejected.

    **Upload format.** A CSV with a header row. Required columns: `timestamp` (ISO-8601, or
    numeric epoch seconds/millis/micros — detected from the first row, then enforced for every
    later row), `close`. Optional columns: `open`, `high`, `low`, `volume`, `quoteVolume`,
    `bid`, `bidSize`, `ask`, `askSize`. Cadence and timestamp unit are discovered from the data,
    not declared.

    Args:
        body (CreateDatasetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetCreated | ResponseError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateDatasetBody,
) -> Response[DatasetCreated | ResponseError]:
    r"""Create a dataset and get a URL to upload it to

     Creates a dataset AND its first upload session in one call — a presigned URL your client
    PUTs the file to directly, no API credentials involved in that PUT. Call
    `POST /datasets/{datasetId}/uploads/{uploadId}/finalize` once the upload completes to kick
    off ingest.

    Losing this response loses nothing: calling this dataset's
    `POST /datasets/{datasetId}/uploads` returns the very same upload session again rather than
    opening a new one, as long as nothing has been finalized against it yet.

    v1 is ticker data only — `type` is not a request field, it is always `\"ticker\"` in the
    response. `instrument` must be a plain spot pair (`BASE/QUOTE`, exactly one `/`); derivative
    forms (e.g. `BTC/USDT:USDT`) are rejected.

    **Upload format.** A CSV with a header row. Required columns: `timestamp` (ISO-8601, or
    numeric epoch seconds/millis/micros — detected from the first row, then enforced for every
    later row), `close`. Optional columns: `open`, `high`, `low`, `volume`, `quoteVolume`,
    `bid`, `bidSize`, `ask`, `askSize`. Cadence and timestamp unit are discovered from the data,
    not declared.

    Args:
        body (CreateDatasetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetCreated | ResponseError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateDatasetBody,
) -> DatasetCreated | ResponseError | None:
    r"""Create a dataset and get a URL to upload it to

     Creates a dataset AND its first upload session in one call — a presigned URL your client
    PUTs the file to directly, no API credentials involved in that PUT. Call
    `POST /datasets/{datasetId}/uploads/{uploadId}/finalize` once the upload completes to kick
    off ingest.

    Losing this response loses nothing: calling this dataset's
    `POST /datasets/{datasetId}/uploads` returns the very same upload session again rather than
    opening a new one, as long as nothing has been finalized against it yet.

    v1 is ticker data only — `type` is not a request field, it is always `\"ticker\"` in the
    response. `instrument` must be a plain spot pair (`BASE/QUOTE`, exactly one `/`); derivative
    forms (e.g. `BTC/USDT:USDT`) are rejected.

    **Upload format.** A CSV with a header row. Required columns: `timestamp` (ISO-8601, or
    numeric epoch seconds/millis/micros — detected from the first row, then enforced for every
    later row), `close`. Optional columns: `open`, `high`, `low`, `volume`, `quoteVolume`,
    `bid`, `bidSize`, `ask`, `askSize`. Cadence and timestamp unit are discovered from the data,
    not declared.

    Args:
        body (CreateDatasetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetCreated | ResponseError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
