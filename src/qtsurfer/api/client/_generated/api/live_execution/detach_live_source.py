from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.live_attachment_accepted import LiveAttachmentAccepted
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    run_id: str,
    attachment_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/live/{run_id}/attachments/{attachment_id}".format(
            run_id=quote(str(run_id), safe=""),
            attachment_id=quote(str(attachment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InsufficientScopeError | LiveAttachmentAccepted | ResponseError | None:
    if response.status_code == 202:
        response_202 = LiveAttachmentAccepted.from_dict(response.json())

        return response_202

    if response.status_code == 403:
        response_403 = InsufficientScopeError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ResponseError.from_dict(response.json())

        return response_404

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
    attachment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[InsufficientScopeError | LiveAttachmentAccepted | ResponseError]:
    """Detach a market-data source from a run

     Detaches a source from a run, **while it stays live**. Owner only. It takes effect at the
    attachment's
    `effectiveAtMs`, applied at the same market position by every execution behind the run. Positions a
    paper
    account had open in that source's instruments are reported as gaps. When the last source is detached
    the run
    waits again: the strategy's memory is released and the paper accounts are kept.

    Repeating it on an attachment already detached, or being detached, is not an error.

    Args:
        run_id (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | LiveAttachmentAccepted | ResponseError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        attachment_id=attachment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient,
) -> InsufficientScopeError | LiveAttachmentAccepted | ResponseError | None:
    """Detach a market-data source from a run

     Detaches a source from a run, **while it stays live**. Owner only. It takes effect at the
    attachment's
    `effectiveAtMs`, applied at the same market position by every execution behind the run. Positions a
    paper
    account had open in that source's instruments are reported as gaps. When the last source is detached
    the run
    waits again: the strategy's memory is released and the paper accounts are kept.

    Repeating it on an attachment already detached, or being detached, is not an error.

    Args:
        run_id (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | LiveAttachmentAccepted | ResponseError
    """

    return sync_detailed(
        run_id=run_id,
        attachment_id=attachment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[InsufficientScopeError | LiveAttachmentAccepted | ResponseError]:
    """Detach a market-data source from a run

     Detaches a source from a run, **while it stays live**. Owner only. It takes effect at the
    attachment's
    `effectiveAtMs`, applied at the same market position by every execution behind the run. Positions a
    paper
    account had open in that source's instruments are reported as gaps. When the last source is detached
    the run
    waits again: the strategy's memory is released and the paper accounts are kept.

    Repeating it on an attachment already detached, or being detached, is not an error.

    Args:
        run_id (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | LiveAttachmentAccepted | ResponseError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        attachment_id=attachment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient,
) -> InsufficientScopeError | LiveAttachmentAccepted | ResponseError | None:
    """Detach a market-data source from a run

     Detaches a source from a run, **while it stays live**. Owner only. It takes effect at the
    attachment's
    `effectiveAtMs`, applied at the same market position by every execution behind the run. Positions a
    paper
    account had open in that source's instruments are reported as gaps. When the last source is detached
    the run
    waits again: the strategy's memory is released and the paper accounts are kept.

    Repeating it on an attachment already detached, or being detached, is not an error.

    Args:
        run_id (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | LiveAttachmentAccepted | ResponseError
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            attachment_id=attachment_id,
            client=client,
        )
    ).parsed
