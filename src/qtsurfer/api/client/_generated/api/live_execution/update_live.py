from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.live_run_compact import LiveRunCompact
from ...models.response_error import ResponseError
from ...models.update_live_request import UpdateLiveRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    run_id: str,
    *,
    body: UpdateLiveRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/live/{run_id}".format(
            run_id=quote(str(run_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LiveRunCompact | ResponseError | None:
    if response.status_code == 200:
        response_200 = LiveRunCompact.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ResponseError.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ResponseError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LiveRunCompact | ResponseError]:
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
    body: UpdateLiveRequest | Unset = UNSET,
) -> Response[LiveRunCompact | ResponseError]:
    """Change a run's visibility, name, or description

     Owner only, addressed by `runId` directly rather than through its strategy — this is a
    run's own canonical identity, independent of which strategy started it.

    Setting `visibility` from `public` back to `private` also evicts anyone currently connected
    to the run's live signal channel who is not its owner — best-effort; the change to this
    record is not rolled back if that eviction fails.

    Args:
        run_id (str):
        body (UpdateLiveRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiveRunCompact | ResponseError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateLiveRequest | Unset = UNSET,
) -> LiveRunCompact | ResponseError | None:
    """Change a run's visibility, name, or description

     Owner only, addressed by `runId` directly rather than through its strategy — this is a
    run's own canonical identity, independent of which strategy started it.

    Setting `visibility` from `public` back to `private` also evicts anyone currently connected
    to the run's live signal channel who is not its owner — best-effort; the change to this
    record is not rolled back if that eviction fails.

    Args:
        run_id (str):
        body (UpdateLiveRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiveRunCompact | ResponseError
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateLiveRequest | Unset = UNSET,
) -> Response[LiveRunCompact | ResponseError]:
    """Change a run's visibility, name, or description

     Owner only, addressed by `runId` directly rather than through its strategy — this is a
    run's own canonical identity, independent of which strategy started it.

    Setting `visibility` from `public` back to `private` also evicts anyone currently connected
    to the run's live signal channel who is not its owner — best-effort; the change to this
    record is not rolled back if that eviction fails.

    Args:
        run_id (str):
        body (UpdateLiveRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiveRunCompact | ResponseError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateLiveRequest | Unset = UNSET,
) -> LiveRunCompact | ResponseError | None:
    """Change a run's visibility, name, or description

     Owner only, addressed by `runId` directly rather than through its strategy — this is a
    run's own canonical identity, independent of which strategy started it.

    Setting `visibility` from `public` back to `private` also evicts anyone currently connected
    to the run's live signal channel who is not its owner — best-effort; the change to this
    record is not rolled back if that eviction fails.

    Args:
        run_id (str):
        body (UpdateLiveRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiveRunCompact | ResponseError
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
            body=body,
        )
    ).parsed
