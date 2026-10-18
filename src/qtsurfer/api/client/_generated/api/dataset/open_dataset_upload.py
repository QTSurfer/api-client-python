from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_upload_session import DatasetUploadSession
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    dataset_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/datasets/{dataset_id}/uploads".format(
            dataset_id=quote(str(dataset_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatasetUploadSession | ResponseError | None:
    if response.status_code == 201:
        response_201 = DatasetUploadSession.from_dict(response.json())

        return response_201

    if response.status_code == 404:
        response_404 = ResponseError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatasetUploadSession | ResponseError]:
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
) -> Response[DatasetUploadSession | ResponseError]:
    """Open a new upload session for an existing dataset

     Get a fresh presigned URL to upload a new version into a dataset you already have — a
    corrected file, or the next chunk of history. Behaves the same way `POST /datasets` does
    for a brand-new dataset's own upload: at most one upload session is open per dataset at a
    time, so calling this again before finalizing just hands back that same session rather
    than opening a second one — safe to call repeatedly if a response gets lost.

    Once a session has been finalized (successfully or not), the next call here opens a
    genuinely new one for that dataset's next version.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetUploadSession | ResponseError]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
) -> DatasetUploadSession | ResponseError | None:
    """Open a new upload session for an existing dataset

     Get a fresh presigned URL to upload a new version into a dataset you already have — a
    corrected file, or the next chunk of history. Behaves the same way `POST /datasets` does
    for a brand-new dataset's own upload: at most one upload session is open per dataset at a
    time, so calling this again before finalizing just hands back that same session rather
    than opening a second one — safe to call repeatedly if a response gets lost.

    Once a session has been finalized (successfully or not), the next call here opens a
    genuinely new one for that dataset's next version.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetUploadSession | ResponseError
    """

    return sync_detailed(
        dataset_id=dataset_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DatasetUploadSession | ResponseError]:
    """Open a new upload session for an existing dataset

     Get a fresh presigned URL to upload a new version into a dataset you already have — a
    corrected file, or the next chunk of history. Behaves the same way `POST /datasets` does
    for a brand-new dataset's own upload: at most one upload session is open per dataset at a
    time, so calling this again before finalizing just hands back that same session rather
    than opening a second one — safe to call repeatedly if a response gets lost.

    Once a session has been finalized (successfully or not), the next call here opens a
    genuinely new one for that dataset's next version.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetUploadSession | ResponseError]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
) -> DatasetUploadSession | ResponseError | None:
    """Open a new upload session for an existing dataset

     Get a fresh presigned URL to upload a new version into a dataset you already have — a
    corrected file, or the next chunk of history. Behaves the same way `POST /datasets` does
    for a brand-new dataset's own upload: at most one upload session is open per dataset at a
    time, so calling this again before finalizing just hands back that same session rather
    than opening a second one — safe to call repeatedly if a response gets lost.

    Once a session has been finalized (successfully or not), the next call here opens a
    genuinely new one for that dataset's next version.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetUploadSession | ResponseError
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            client=client,
        )
    ).parsed
