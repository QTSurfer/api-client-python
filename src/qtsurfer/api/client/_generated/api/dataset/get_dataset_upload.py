from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_upload_state import DatasetUploadState
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    dataset_id: str,
    upload_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasets/{dataset_id}/uploads/{upload_id}".format(
            dataset_id=quote(str(dataset_id), safe=""),
            upload_id=quote(str(upload_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatasetUploadState | ResponseError | None:
    if response.status_code == 200:
        response_200 = DatasetUploadState.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ResponseError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatasetUploadState | ResponseError]:
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
) -> Response[DatasetUploadState | ResponseError]:
    """Get the state of an upload/ingest

     Poll after `POST .../finalize` until `status` is `ready` or `failed`. Also reports
    `uploading` (finalize not called yet, but the file was PUT) before you finalize at all.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.
        upload_id (str):  Example: up_1a2b3c4d5e6f7a8b.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetUploadState | ResponseError]
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
) -> DatasetUploadState | ResponseError | None:
    """Get the state of an upload/ingest

     Poll after `POST .../finalize` until `status` is `ready` or `failed`. Also reports
    `uploading` (finalize not called yet, but the file was PUT) before you finalize at all.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.
        upload_id (str):  Example: up_1a2b3c4d5e6f7a8b.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetUploadState | ResponseError
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
) -> Response[DatasetUploadState | ResponseError]:
    """Get the state of an upload/ingest

     Poll after `POST .../finalize` until `status` is `ready` or `failed`. Also reports
    `uploading` (finalize not called yet, but the file was PUT) before you finalize at all.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.
        upload_id (str):  Example: up_1a2b3c4d5e6f7a8b.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetUploadState | ResponseError]
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
) -> DatasetUploadState | ResponseError | None:
    """Get the state of an upload/ingest

     Poll after `POST .../finalize` until `status` is `ready` or `failed`. Also reports
    `uploading` (finalize not called yet, but the file was PUT) before you finalize at all.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.
        upload_id (str):  Example: up_1a2b3c4d5e6f7a8b.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetUploadState | ResponseError
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            upload_id=upload_id,
            client=client,
        )
    ).parsed
