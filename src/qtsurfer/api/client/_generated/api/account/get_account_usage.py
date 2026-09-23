from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_usage import AccountUsage
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/account/usage",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AccountUsage | None:
    if response.status_code == 200:
        response_200 = AccountUsage.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AccountUsage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[AccountUsage]:
    """Get your live storage usage

     How much of your account's shared storage pool (`GET /account`'s `maxTotalStorageBytes`)
    you're currently using. Datasets, strategy-execution signals, and registered strategies
    all count against the same total — they compete for the same underlying storage, so
    there's one number to watch, not one per resource type. Not guaranteed real-time — a
    just-completed upload or strategy execution may take a short moment to be reflected here.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountUsage]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> AccountUsage | None:
    """Get your live storage usage

     How much of your account's shared storage pool (`GET /account`'s `maxTotalStorageBytes`)
    you're currently using. Datasets, strategy-execution signals, and registered strategies
    all count against the same total — they compete for the same underlying storage, so
    there's one number to watch, not one per resource type. Not guaranteed real-time — a
    just-completed upload or strategy execution may take a short moment to be reflected here.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountUsage
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[AccountUsage]:
    """Get your live storage usage

     How much of your account's shared storage pool (`GET /account`'s `maxTotalStorageBytes`)
    you're currently using. Datasets, strategy-execution signals, and registered strategies
    all count against the same total — they compete for the same underlying storage, so
    there's one number to watch, not one per resource type. Not guaranteed real-time — a
    just-completed upload or strategy execution may take a short moment to be reflected here.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountUsage]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> AccountUsage | None:
    """Get your live storage usage

     How much of your account's shared storage pool (`GET /account`'s `maxTotalStorageBytes`)
    you're currently using. Datasets, strategy-execution signals, and registered strategies
    all count against the same total — they compete for the same underlying storage, so
    there's one number to watch, not one per resource type. Not guaranteed real-time — a
    just-completed upload or strategy execution may take a short moment to be reflected here.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountUsage
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
