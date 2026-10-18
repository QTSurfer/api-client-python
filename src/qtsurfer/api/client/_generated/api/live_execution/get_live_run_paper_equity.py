from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.live_paper_equity_page import LivePaperEquityPage
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    run_id: str,
    *,
    currency: str | Unset = UNSET,
    since_ms: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["currency"] = currency

    params["sinceMs"] = since_ms

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/live/{run_id}/paper/equity".format(
            run_id=quote(str(run_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LivePaperEquityPage | ResponseError | None:
    if response.status_code == 200:
        response_200 = LivePaperEquityPage.from_dict(response.json())

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
) -> Response[LivePaperEquityPage | ResponseError]:
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
    currency: str | Unset = UNSET,
    since_ms: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[LivePaperEquityPage | ResponseError]:
    """Read a run's paper equity curve

     The run's paper equity curve, oldest first, page by page. It is kept for the life of the
    run, so unlike signals it has no moving window. Points are `equity` at every closed trade,
    `mark` every minute of market time while positions are open, and `gap` where the run was
    restarted with positions open: those positions are not carried over, so the curve has no
    value there.

    `currency` narrows to one account; without it, every account's points come interleaved by
    time, each carrying its currency.

    Readable by the run's owner, and by anyone if the run is `public` and has reached the `live`
    stage.

    Args:
        run_id (str):
        currency (str | Unset):
        since_ms (int | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LivePaperEquityPage | ResponseError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        currency=currency,
        since_ms=since_ms,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: str,
    *,
    client: AuthenticatedClient,
    currency: str | Unset = UNSET,
    since_ms: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> LivePaperEquityPage | ResponseError | None:
    """Read a run's paper equity curve

     The run's paper equity curve, oldest first, page by page. It is kept for the life of the
    run, so unlike signals it has no moving window. Points are `equity` at every closed trade,
    `mark` every minute of market time while positions are open, and `gap` where the run was
    restarted with positions open: those positions are not carried over, so the curve has no
    value there.

    `currency` narrows to one account; without it, every account's points come interleaved by
    time, each carrying its currency.

    Readable by the run's owner, and by anyone if the run is `public` and has reached the `live`
    stage.

    Args:
        run_id (str):
        currency (str | Unset):
        since_ms (int | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LivePaperEquityPage | ResponseError
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
        currency=currency,
        since_ms=since_ms,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
    currency: str | Unset = UNSET,
    since_ms: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[LivePaperEquityPage | ResponseError]:
    """Read a run's paper equity curve

     The run's paper equity curve, oldest first, page by page. It is kept for the life of the
    run, so unlike signals it has no moving window. Points are `equity` at every closed trade,
    `mark` every minute of market time while positions are open, and `gap` where the run was
    restarted with positions open: those positions are not carried over, so the curve has no
    value there.

    `currency` narrows to one account; without it, every account's points come interleaved by
    time, each carrying its currency.

    Readable by the run's owner, and by anyone if the run is `public` and has reached the `live`
    stage.

    Args:
        run_id (str):
        currency (str | Unset):
        since_ms (int | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LivePaperEquityPage | ResponseError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        currency=currency,
        since_ms=since_ms,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    *,
    client: AuthenticatedClient,
    currency: str | Unset = UNSET,
    since_ms: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> LivePaperEquityPage | ResponseError | None:
    """Read a run's paper equity curve

     The run's paper equity curve, oldest first, page by page. It is kept for the life of the
    run, so unlike signals it has no moving window. Points are `equity` at every closed trade,
    `mark` every minute of market time while positions are open, and `gap` where the run was
    restarted with positions open: those positions are not carried over, so the curve has no
    value there.

    `currency` narrows to one account; without it, every account's points come interleaved by
    time, each carrying its currency.

    Readable by the run's owner, and by anyone if the run is `public` and has reached the `live`
    stage.

    Args:
        run_id (str):
        currency (str | Unset):
        since_ms (int | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LivePaperEquityPage | ResponseError
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
            currency=currency,
            since_ms=since_ms,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
