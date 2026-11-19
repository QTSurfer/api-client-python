from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attach_live_source_request import AttachLiveSourceRequest
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.live_attachment_accepted import LiveAttachmentAccepted
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    run_id: str,
    *,
    body: AttachLiveSourceRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/live/{run_id}/attachments".format(
            run_id=quote(str(run_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InsufficientScopeError | LiveAttachmentAccepted | ResponseError | None:
    if response.status_code == 202:
        response_202 = LiveAttachmentAccepted.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ResponseError.from_dict(response.json())

        return response_400

    if response.status_code == 402:
        response_402 = ResponseError.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = InsufficientScopeError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ResponseError.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ResponseError.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = ResponseError.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ResponseError.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[InsufficientScopeError | LiveAttachmentAccepted | ResponseError]:
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
    body: AttachLiveSourceRequest,
) -> Response[InsufficientScopeError | LiveAttachmentAccepted | ResponseError]:
    r"""Attach a market-data source to a run

     Attaches one market-data source to a run, **while it stays live**. A run can start with no `sources`
    and
    wait; this is how it is given something to read, and how a run that is already reading something is
    given
    another. Owner only.

    `source` is the same entry `sources` takes at start and is checked the same way (see \"Sources\" in
    the Live
    execution guide). `warmFrom` is how many seconds of the feed before the attachment the strategy sees
    first,
    `0` to `3600`, for this source only; left out, the same default as at start. `ref` is a string of
    yours, up to
    64 characters: sending the same `ref` to the same run answers the attachment it already made instead
    of
    making another one, so a retried request or a repeated alert is safe. So does sending a source the
    run
    already has attached or being attached, whatever its `ref`.

    Every source attached to a run at the same time is on the same market feed: the same exchange for a
    `cex`, the
    same chain for a `dex`.

    The first source of a waiting run starts it. Any other attach takes effect at `effectiveAtMs`, a
    moment a few
    seconds ahead that every execution behind the run applies at the same market position. The `202` is
    the
    acceptance: read the run's `attachments` for the `state`.

    Args:
        run_id (str):
        body (AttachLiveSourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | LiveAttachmentAccepted | ResponseError]
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
    body: AttachLiveSourceRequest,
) -> InsufficientScopeError | LiveAttachmentAccepted | ResponseError | None:
    r"""Attach a market-data source to a run

     Attaches one market-data source to a run, **while it stays live**. A run can start with no `sources`
    and
    wait; this is how it is given something to read, and how a run that is already reading something is
    given
    another. Owner only.

    `source` is the same entry `sources` takes at start and is checked the same way (see \"Sources\" in
    the Live
    execution guide). `warmFrom` is how many seconds of the feed before the attachment the strategy sees
    first,
    `0` to `3600`, for this source only; left out, the same default as at start. `ref` is a string of
    yours, up to
    64 characters: sending the same `ref` to the same run answers the attachment it already made instead
    of
    making another one, so a retried request or a repeated alert is safe. So does sending a source the
    run
    already has attached or being attached, whatever its `ref`.

    Every source attached to a run at the same time is on the same market feed: the same exchange for a
    `cex`, the
    same chain for a `dex`.

    The first source of a waiting run starts it. Any other attach takes effect at `effectiveAtMs`, a
    moment a few
    seconds ahead that every execution behind the run applies at the same market position. The `202` is
    the
    acceptance: read the run's `attachments` for the `state`.

    Args:
        run_id (str):
        body (AttachLiveSourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | LiveAttachmentAccepted | ResponseError
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
    body: AttachLiveSourceRequest,
) -> Response[InsufficientScopeError | LiveAttachmentAccepted | ResponseError]:
    r"""Attach a market-data source to a run

     Attaches one market-data source to a run, **while it stays live**. A run can start with no `sources`
    and
    wait; this is how it is given something to read, and how a run that is already reading something is
    given
    another. Owner only.

    `source` is the same entry `sources` takes at start and is checked the same way (see \"Sources\" in
    the Live
    execution guide). `warmFrom` is how many seconds of the feed before the attachment the strategy sees
    first,
    `0` to `3600`, for this source only; left out, the same default as at start. `ref` is a string of
    yours, up to
    64 characters: sending the same `ref` to the same run answers the attachment it already made instead
    of
    making another one, so a retried request or a repeated alert is safe. So does sending a source the
    run
    already has attached or being attached, whatever its `ref`.

    Every source attached to a run at the same time is on the same market feed: the same exchange for a
    `cex`, the
    same chain for a `dex`.

    The first source of a waiting run starts it. Any other attach takes effect at `effectiveAtMs`, a
    moment a few
    seconds ahead that every execution behind the run applies at the same market position. The `202` is
    the
    acceptance: read the run's `attachments` for the `state`.

    Args:
        run_id (str):
        body (AttachLiveSourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | LiveAttachmentAccepted | ResponseError]
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
    body: AttachLiveSourceRequest,
) -> InsufficientScopeError | LiveAttachmentAccepted | ResponseError | None:
    r"""Attach a market-data source to a run

     Attaches one market-data source to a run, **while it stays live**. A run can start with no `sources`
    and
    wait; this is how it is given something to read, and how a run that is already reading something is
    given
    another. Owner only.

    `source` is the same entry `sources` takes at start and is checked the same way (see \"Sources\" in
    the Live
    execution guide). `warmFrom` is how many seconds of the feed before the attachment the strategy sees
    first,
    `0` to `3600`, for this source only; left out, the same default as at start. `ref` is a string of
    yours, up to
    64 characters: sending the same `ref` to the same run answers the attachment it already made instead
    of
    making another one, so a retried request or a repeated alert is safe. So does sending a source the
    run
    already has attached or being attached, whatever its `ref`.

    Every source attached to a run at the same time is on the same market feed: the same exchange for a
    `cex`, the
    same chain for a `dex`.

    The first source of a waiting run starts it. Any other attach takes effect at `effectiveAtMs`, a
    moment a few
    seconds ahead that every execution behind the run applies at the same market position. The `202` is
    the
    acceptance: read the run's `attachments` for the `state`.

    Args:
        run_id (str):
        body (AttachLiveSourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | LiveAttachmentAccepted | ResponseError
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
            body=body,
        )
    ).parsed
