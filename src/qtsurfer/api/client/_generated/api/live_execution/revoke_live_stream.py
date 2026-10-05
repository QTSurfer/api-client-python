from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.live_stream_revoked import LiveStreamRevoked
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    run_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/live/{run_id}/stream".format(
            run_id=quote(str(run_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LiveStreamRevoked | ResponseError | None:
    if response.status_code == 200:
        response_200 = LiveStreamRevoked.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ResponseError.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ResponseError.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LiveStreamRevoked | ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[LiveStreamRevoked | ResponseError]:
    """Revoke a run's stream URL

     Revokes a run's stream URL **for good**: connections open on it are closed within about 15 seconds
    and it
    answers `404` from then on. The run itself is not touched, and a stream cannot be added to it again;
    start
    the run again with `stream: true` for a new URL. Owner only, and always allowed, whatever your plan
    or the
    run's state. Repeating it is not an error.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiveStreamRevoked | ResponseError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> LiveStreamRevoked | ResponseError | None:
    """Revoke a run's stream URL

     Revokes a run's stream URL **for good**: connections open on it are closed within about 15 seconds
    and it
    answers `404` from then on. The run itself is not touched, and a stream cannot be added to it again;
    start
    the run again with `stream: true` for a new URL. Owner only, and always allowed, whatever your plan
    or the
    run's state. Repeating it is not an error.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiveStreamRevoked | ResponseError
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[LiveStreamRevoked | ResponseError]:
    """Revoke a run's stream URL

     Revokes a run's stream URL **for good**: connections open on it are closed within about 15 seconds
    and it
    answers `404` from then on. The run itself is not touched, and a stream cannot be added to it again;
    start
    the run again with `stream: true` for a new URL. Owner only, and always allowed, whatever your plan
    or the
    run's state. Repeating it is not an error.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiveStreamRevoked | ResponseError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> LiveStreamRevoked | ResponseError | None:
    """Revoke a run's stream URL

     Revokes a run's stream URL **for good**: connections open on it are closed within about 15 seconds
    and it
    answers `404` from then on. The run itself is not touched, and a stream cannot be added to it again;
    start
    the run again with `stream: true` for a new URL. Owner only, and always allowed, whatever your plan
    or the
    run's state. Repeating it is not an error.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiveStreamRevoked | ResponseError
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
        )
    ).parsed
