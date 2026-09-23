from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_import_state import DatasetImportState
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    dataset_id: str,
    import_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasets/{dataset_id}/imports/{import_id}".format(
            dataset_id=quote(str(dataset_id), safe=""),
            import_id=quote(str(import_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatasetImportState | ResponseError | None:
    if response.status_code == 200:
        response_200 = DatasetImportState.from_dict(response.json())

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
) -> Response[DatasetImportState | ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: str,
    import_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DatasetImportState | ResponseError]:
    """Get the state of an import/ingest

     Poll after `POST /datasets/imports` until `status` is `ready` or `failed`. An import spends
    real time fetching from its source before anything is even staged — `fetching` is the one
    status only an import ever reports; `ingesting`/`ready`/`failed` mean exactly what they do
    on `GET /datasets/{datasetId}/uploads/{uploadId}`, since an import re-enters that same
    ingest chain once it has fetched and staged its data.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.
        import_id (str):  Example: imp_01j9z1x2y3z4a5b6c7d8e9f0g1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetImportState | ResponseError]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        import_id=import_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    import_id: str,
    *,
    client: AuthenticatedClient,
) -> DatasetImportState | ResponseError | None:
    """Get the state of an import/ingest

     Poll after `POST /datasets/imports` until `status` is `ready` or `failed`. An import spends
    real time fetching from its source before anything is even staged — `fetching` is the one
    status only an import ever reports; `ingesting`/`ready`/`failed` mean exactly what they do
    on `GET /datasets/{datasetId}/uploads/{uploadId}`, since an import re-enters that same
    ingest chain once it has fetched and staged its data.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.
        import_id (str):  Example: imp_01j9z1x2y3z4a5b6c7d8e9f0g1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetImportState | ResponseError
    """

    return sync_detailed(
        dataset_id=dataset_id,
        import_id=import_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    import_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DatasetImportState | ResponseError]:
    """Get the state of an import/ingest

     Poll after `POST /datasets/imports` until `status` is `ready` or `failed`. An import spends
    real time fetching from its source before anything is even staged — `fetching` is the one
    status only an import ever reports; `ingesting`/`ready`/`failed` mean exactly what they do
    on `GET /datasets/{datasetId}/uploads/{uploadId}`, since an import re-enters that same
    ingest chain once it has fetched and staged its data.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.
        import_id (str):  Example: imp_01j9z1x2y3z4a5b6c7d8e9f0g1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetImportState | ResponseError]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        import_id=import_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    import_id: str,
    *,
    client: AuthenticatedClient,
) -> DatasetImportState | ResponseError | None:
    """Get the state of an import/ingest

     Poll after `POST /datasets/imports` until `status` is `ready` or `failed`. An import spends
    real time fetching from its source before anything is even staged — `fetching` is the one
    status only an import ever reports; `ingesting`/`ready`/`failed` mean exactly what they do
    on `GET /datasets/{datasetId}/uploads/{uploadId}`, since an import re-enters that same
    ingest chain once it has fetched and staged its data.

    Args:
        dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.
        import_id (str):  Example: imp_01j9z1x2y3z4a5b6c7d8e9f0g1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetImportState | ResponseError
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            import_id=import_id,
            client=client,
        )
    ).parsed
