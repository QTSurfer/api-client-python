from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.finalize_dataset_upload_response_202 import FinalizeDatasetUploadResponse202
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    dataset_id: str,
    upload_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/datasets/{dataset_id}/uploads/{upload_id}/finalize".format(
            dataset_id=quote(str(dataset_id), safe=""),
            upload_id=quote(str(upload_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FinalizeDatasetUploadResponse202 | ResponseError | None:
    if response.status_code == 202:
        response_202 = FinalizeDatasetUploadResponse202.from_dict(response.json())

        return response_202

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
) -> Response[FinalizeDatasetUploadResponse202 | ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: str,
    upload_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[FinalizeDatasetUploadResponse202 | ResponseError]:
    """Finalize an uploaded file and start ingest

     Call once the file has been PUT to the `upload.url` from `POST /datasets` (or from
    `POST /datasets/{datasetId}/uploads`). Enqueues ingest and returns immediately; poll
    `GET /datasets/{datasetId}/uploads/{uploadId}` for the result.

    Idempotent while the upload is still open — a repeat finalize before it has produced a
    version returns the same `jobId` rather than enqueueing a second ingest. Once it HAS
    produced a version, `uploadId` is spent: finalizing it again is a `409`, even with
    different bytes freshly PUT to the same URL — open a new upload session instead
    (`POST /datasets/{datasetId}/uploads`) rather than reusing a spent one.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.
        upload_id (str):  Example: up_1a2b3c4d5e6f7a8b.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinalizeDatasetUploadResponse202 | ResponseError]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        upload_id=upload_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    upload_id: str,
    *,
    client: AuthenticatedClient,
) -> FinalizeDatasetUploadResponse202 | ResponseError | None:
    """Finalize an uploaded file and start ingest

     Call once the file has been PUT to the `upload.url` from `POST /datasets` (or from
    `POST /datasets/{datasetId}/uploads`). Enqueues ingest and returns immediately; poll
    `GET /datasets/{datasetId}/uploads/{uploadId}` for the result.

    Idempotent while the upload is still open — a repeat finalize before it has produced a
    version returns the same `jobId` rather than enqueueing a second ingest. Once it HAS
    produced a version, `uploadId` is spent: finalizing it again is a `409`, even with
    different bytes freshly PUT to the same URL — open a new upload session instead
    (`POST /datasets/{datasetId}/uploads`) rather than reusing a spent one.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.
        upload_id (str):  Example: up_1a2b3c4d5e6f7a8b.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinalizeDatasetUploadResponse202 | ResponseError
    """

    return sync_detailed(
        dataset_id=dataset_id,
        upload_id=upload_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    upload_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[FinalizeDatasetUploadResponse202 | ResponseError]:
    """Finalize an uploaded file and start ingest

     Call once the file has been PUT to the `upload.url` from `POST /datasets` (or from
    `POST /datasets/{datasetId}/uploads`). Enqueues ingest and returns immediately; poll
    `GET /datasets/{datasetId}/uploads/{uploadId}` for the result.

    Idempotent while the upload is still open — a repeat finalize before it has produced a
    version returns the same `jobId` rather than enqueueing a second ingest. Once it HAS
    produced a version, `uploadId` is spent: finalizing it again is a `409`, even with
    different bytes freshly PUT to the same URL — open a new upload session instead
    (`POST /datasets/{datasetId}/uploads`) rather than reusing a spent one.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.
        upload_id (str):  Example: up_1a2b3c4d5e6f7a8b.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinalizeDatasetUploadResponse202 | ResponseError]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        upload_id=upload_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    upload_id: str,
    *,
    client: AuthenticatedClient,
) -> FinalizeDatasetUploadResponse202 | ResponseError | None:
    """Finalize an uploaded file and start ingest

     Call once the file has been PUT to the `upload.url` from `POST /datasets` (or from
    `POST /datasets/{datasetId}/uploads`). Enqueues ingest and returns immediately; poll
    `GET /datasets/{datasetId}/uploads/{uploadId}` for the result.

    Idempotent while the upload is still open — a repeat finalize before it has produced a
    version returns the same `jobId` rather than enqueueing a second ingest. Once it HAS
    produced a version, `uploadId` is spent: finalizing it again is a `409`, even with
    different bytes freshly PUT to the same URL — open a new upload session instead
    (`POST /datasets/{datasetId}/uploads`) rather than reusing a spent one.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.
        upload_id (str):  Example: up_1a2b3c4d5e6f7a8b.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinalizeDatasetUploadResponse202 | ResponseError
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            upload_id=upload_id,
            client=client,
        )
    ).parsed
