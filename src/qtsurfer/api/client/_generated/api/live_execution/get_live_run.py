from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.live_run_detail import LiveRunDetail
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    run_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/live/{run_id}".format(
            run_id=quote(str(run_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LiveRunDetail | ResponseError | None:
    if response.status_code == 200:
        response_200 = LiveRunDetail.from_dict(response.json())

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
) -> Response[LiveRunDetail | ResponseError]:
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
) -> Response[LiveRunDetail | ResponseError]:
    """Read one of your runs by its id

     Owner only, addressed by `runId` directly rather than through its strategy: the run's own
    canonical identity, which is what `POST`/`GET`/`DELETE` `.../live`, `GET /live` and
    `GET /live/public` all hand out. Use it to re-read one specific run — including one you
    stopped long ago or that is no longer your strategy's most recent — without paging through
    `GET /live`.

    Returns the same state as `GET /strategy/{strategyId}/live` (`strategyId` is the strategy's
    id, and `stats` is there too), plus `updatedAtMs`: when the run last changed, from any cause — a
    state change, a promotion, a parameter update, a stop. A refresh of `stats` is not a change of
    the run and does not move `updatedAtMs`. A run that is public is reachable by others through
    `GET /live/public`, never through this route.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiveRunDetail | ResponseError]
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
) -> LiveRunDetail | ResponseError | None:
    """Read one of your runs by its id

     Owner only, addressed by `runId` directly rather than through its strategy: the run's own
    canonical identity, which is what `POST`/`GET`/`DELETE` `.../live`, `GET /live` and
    `GET /live/public` all hand out. Use it to re-read one specific run — including one you
    stopped long ago or that is no longer your strategy's most recent — without paging through
    `GET /live`.

    Returns the same state as `GET /strategy/{strategyId}/live` (`strategyId` is the strategy's
    id, and `stats` is there too), plus `updatedAtMs`: when the run last changed, from any cause — a
    state change, a promotion, a parameter update, a stop. A refresh of `stats` is not a change of
    the run and does not move `updatedAtMs`. A run that is public is reachable by others through
    `GET /live/public`, never through this route.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiveRunDetail | ResponseError
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[LiveRunDetail | ResponseError]:
    """Read one of your runs by its id

     Owner only, addressed by `runId` directly rather than through its strategy: the run's own
    canonical identity, which is what `POST`/`GET`/`DELETE` `.../live`, `GET /live` and
    `GET /live/public` all hand out. Use it to re-read one specific run — including one you
    stopped long ago or that is no longer your strategy's most recent — without paging through
    `GET /live`.

    Returns the same state as `GET /strategy/{strategyId}/live` (`strategyId` is the strategy's
    id, and `stats` is there too), plus `updatedAtMs`: when the run last changed, from any cause — a
    state change, a promotion, a parameter update, a stop. A refresh of `stats` is not a change of
    the run and does not move `updatedAtMs`. A run that is public is reachable by others through
    `GET /live/public`, never through this route.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiveRunDetail | ResponseError]
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
) -> LiveRunDetail | ResponseError | None:
    """Read one of your runs by its id

     Owner only, addressed by `runId` directly rather than through its strategy: the run's own
    canonical identity, which is what `POST`/`GET`/`DELETE` `.../live`, `GET /live` and
    `GET /live/public` all hand out. Use it to re-read one specific run — including one you
    stopped long ago or that is no longer your strategy's most recent — without paging through
    `GET /live`.

    Returns the same state as `GET /strategy/{strategyId}/live` (`strategyId` is the strategy's
    id, and `stats` is there too), plus `updatedAtMs`: when the run last changed, from any cause — a
    state change, a promotion, a parameter update, a stop. A refresh of `stats` is not a change of
    the run and does not move `updatedAtMs`. A run that is public is reachable by others through
    `GET /live/public`, never through this route.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiveRunDetail | ResponseError
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
        )
    ).parsed
