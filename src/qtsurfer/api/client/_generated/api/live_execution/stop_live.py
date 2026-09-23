from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.live_run import LiveRun
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    strategy_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/strategy/{strategy_id}/live".format(
            strategy_id=quote(str(strategy_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LiveRun | ResponseError | None:
    if response.status_code == 200:
        response_200 = LiveRun.from_dict(response.json())

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
) -> Response[LiveRun | ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    strategy_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[LiveRun | ResponseError]:
    """Stop this strategy's live run

     Requests a stop. The run winds down at its own next check-in rather than instantly —
    poll `GET`/`PATCH` `.../live` and expect `state` to remain `RUNNING` for a short window
    after `desired` flips to `STOPPED`. Calling this again on an already-stopped run is not an
    error; it returns the same (unchanged) state.

    Args:
        strategy_id (str): Unique identifier for a compiled strategy, derived from the source
            itself: the same code
            always yields the same id, for every caller. How much formatting the id ignores depends on
            the language — see `POST /strategy` for exactly which rewrites preserve it and which do
            not.
             Example: 6bsh31ikwkuivhtgcoa6s4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiveRun | ResponseError]
    """

    kwargs = _get_kwargs(
        strategy_id=strategy_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    strategy_id: str,
    *,
    client: AuthenticatedClient,
) -> LiveRun | ResponseError | None:
    """Stop this strategy's live run

     Requests a stop. The run winds down at its own next check-in rather than instantly —
    poll `GET`/`PATCH` `.../live` and expect `state` to remain `RUNNING` for a short window
    after `desired` flips to `STOPPED`. Calling this again on an already-stopped run is not an
    error; it returns the same (unchanged) state.

    Args:
        strategy_id (str): Unique identifier for a compiled strategy, derived from the source
            itself: the same code
            always yields the same id, for every caller. How much formatting the id ignores depends on
            the language — see `POST /strategy` for exactly which rewrites preserve it and which do
            not.
             Example: 6bsh31ikwkuivhtgcoa6s4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiveRun | ResponseError
    """

    return sync_detailed(
        strategy_id=strategy_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    strategy_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[LiveRun | ResponseError]:
    """Stop this strategy's live run

     Requests a stop. The run winds down at its own next check-in rather than instantly —
    poll `GET`/`PATCH` `.../live` and expect `state` to remain `RUNNING` for a short window
    after `desired` flips to `STOPPED`. Calling this again on an already-stopped run is not an
    error; it returns the same (unchanged) state.

    Args:
        strategy_id (str): Unique identifier for a compiled strategy, derived from the source
            itself: the same code
            always yields the same id, for every caller. How much formatting the id ignores depends on
            the language — see `POST /strategy` for exactly which rewrites preserve it and which do
            not.
             Example: 6bsh31ikwkuivhtgcoa6s4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiveRun | ResponseError]
    """

    kwargs = _get_kwargs(
        strategy_id=strategy_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    strategy_id: str,
    *,
    client: AuthenticatedClient,
) -> LiveRun | ResponseError | None:
    """Stop this strategy's live run

     Requests a stop. The run winds down at its own next check-in rather than instantly —
    poll `GET`/`PATCH` `.../live` and expect `state` to remain `RUNNING` for a short window
    after `desired` flips to `STOPPED`. Calling this again on an already-stopped run is not an
    error; it returns the same (unchanged) state.

    Args:
        strategy_id (str): Unique identifier for a compiled strategy, derived from the source
            itself: the same code
            always yields the same id, for every caller. How much formatting the id ignores depends on
            the language — see `POST /strategy` for exactly which rewrites preserve it and which do
            not.
             Example: 6bsh31ikwkuivhtgcoa6s4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiveRun | ResponseError
    """

    return (
        await asyncio_detailed(
            strategy_id=strategy_id,
            client=client,
        )
    ).parsed
