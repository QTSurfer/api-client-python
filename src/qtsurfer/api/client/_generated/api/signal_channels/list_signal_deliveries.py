from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.response_error import ResponseError
from ...models.signal_delivery_page import SignalDeliveryPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    subscription_id: str,
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/signals/subscriptions/{subscription_id}/deliveries".format(
            subscription_id=quote(str(subscription_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InsufficientScopeError | ResponseError | SignalDeliveryPage | None:
    if response.status_code == 200:
        response_200 = SignalDeliveryPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ResponseError.from_dict(response.json())

        return response_400

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
) -> Response[InsufficientScopeError | ResponseError | SignalDeliveryPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[InsufficientScopeError | ResponseError | SignalDeliveryPage]:
    """List what a subscription of yours received

     Every notice due to the runs the subscription feeds, one delivery per run (`runId`), most recent
    first, with
    what it did: `PENDING` (not due yet), `ATTACHED` (the instrument was attached to the run: read the
    run's
    `attachments` for how the attachment stands), `REFUSED` (the run could not take it; `reason` says
    why),
    `EXPIRED` (not made before the notice expired) or `SKIPPED` (not made: the run was not running or no
    longer fed,
    the subscription was cancelled, revoked or expired, or the channel was deleted). The notice's
    `source` and `data` come with it from `dueAtMs` on: before that a delivery says that a
    notice is coming and when, not what it is about, so a subscription at a delayed level learns of the
    instrument
    no earlier than its level.

    Args:
        subscription_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalDeliveryPage]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> InsufficientScopeError | ResponseError | SignalDeliveryPage | None:
    """List what a subscription of yours received

     Every notice due to the runs the subscription feeds, one delivery per run (`runId`), most recent
    first, with
    what it did: `PENDING` (not due yet), `ATTACHED` (the instrument was attached to the run: read the
    run's
    `attachments` for how the attachment stands), `REFUSED` (the run could not take it; `reason` says
    why),
    `EXPIRED` (not made before the notice expired) or `SKIPPED` (not made: the run was not running or no
    longer fed,
    the subscription was cancelled, revoked or expired, or the channel was deleted). The notice's
    `source` and `data` come with it from `dueAtMs` on: before that a delivery says that a
    notice is coming and when, not what it is about, so a subscription at a delayed level learns of the
    instrument
    no earlier than its level.

    Args:
        subscription_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalDeliveryPage
    """

    return sync_detailed(
        subscription_id=subscription_id,
        client=client,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[InsufficientScopeError | ResponseError | SignalDeliveryPage]:
    """List what a subscription of yours received

     Every notice due to the runs the subscription feeds, one delivery per run (`runId`), most recent
    first, with
    what it did: `PENDING` (not due yet), `ATTACHED` (the instrument was attached to the run: read the
    run's
    `attachments` for how the attachment stands), `REFUSED` (the run could not take it; `reason` says
    why),
    `EXPIRED` (not made before the notice expired) or `SKIPPED` (not made: the run was not running or no
    longer fed,
    the subscription was cancelled, revoked or expired, or the channel was deleted). The notice's
    `source` and `data` come with it from `dueAtMs` on: before that a delivery says that a
    notice is coming and when, not what it is about, so a subscription at a delayed level learns of the
    instrument
    no earlier than its level.

    Args:
        subscription_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientScopeError | ResponseError | SignalDeliveryPage]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> InsufficientScopeError | ResponseError | SignalDeliveryPage | None:
    """List what a subscription of yours received

     Every notice due to the runs the subscription feeds, one delivery per run (`runId`), most recent
    first, with
    what it did: `PENDING` (not due yet), `ATTACHED` (the instrument was attached to the run: read the
    run's
    `attachments` for how the attachment stands), `REFUSED` (the run could not take it; `reason` says
    why),
    `EXPIRED` (not made before the notice expired) or `SKIPPED` (not made: the run was not running or no
    longer fed,
    the subscription was cancelled, revoked or expired, or the channel was deleted). The notice's
    `source` and `data` come with it from `dueAtMs` on: before that a delivery says that a
    notice is coming and when, not what it is about, so a subscription at a delayed level learns of the
    instrument
    no earlier than its level.

    Args:
        subscription_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientScopeError | ResponseError | SignalDeliveryPage
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            client=client,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
