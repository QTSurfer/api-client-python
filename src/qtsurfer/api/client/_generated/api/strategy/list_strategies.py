from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_strategies_response_200 import ListStrategiesResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/strategies",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListStrategiesResponse200 | None:
    if response.status_code == 200:
        response_200 = ListStrategiesResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListStrategiesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ListStrategiesResponse200]:
    """List your registered strategies

     Every strategy you have registered and not deleted, most recently compiled first.

    Each entry carries the same provenance `GET /strategy/{strategyId}` does — `compiledAt`,
    `requiredSources` — but not its validation state, so listing stays cheap regardless of how
    many strategies you have. Check a specific strategy's validation with `GET
    /strategy/{strategyId}`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListStrategiesResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ListStrategiesResponse200 | None:
    """List your registered strategies

     Every strategy you have registered and not deleted, most recently compiled first.

    Each entry carries the same provenance `GET /strategy/{strategyId}` does — `compiledAt`,
    `requiredSources` — but not its validation state, so listing stays cheap regardless of how
    many strategies you have. Check a specific strategy's validation with `GET
    /strategy/{strategyId}`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListStrategiesResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ListStrategiesResponse200]:
    """List your registered strategies

     Every strategy you have registered and not deleted, most recently compiled first.

    Each entry carries the same provenance `GET /strategy/{strategyId}` does — `compiledAt`,
    `requiredSources` — but not its validation state, so listing stays cheap regardless of how
    many strategies you have. Check a specific strategy's validation with `GET
    /strategy/{strategyId}`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListStrategiesResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ListStrategiesResponse200 | None:
    """List your registered strategies

     Every strategy you have registered and not deleted, most recently compiled first.

    Each entry carries the same provenance `GET /strategy/{strategyId}` does — `compiledAt`,
    `requiredSources` — but not its validation state, so listing stays cheap regardless of how
    many strategies you have. Check a specific strategy's validation with `GET
    /strategy/{strategyId}`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListStrategiesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
