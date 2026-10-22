from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.instrument_list_response import InstrumentListResponse
from ...models.insufficient_scope_error import InsufficientScopeError
from ...models.pool_list_response import PoolListResponse
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    exchange_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/exchange/{exchange_id}/instruments".format(
            exchange_id=quote(str(exchange_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InstrumentListResponse | PoolListResponse | InsufficientScopeError | ResponseError | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> InstrumentListResponse | PoolListResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_instrument_catalogue_response_type_0 = InstrumentListResponse.from_dict(data)

                return componentsschemas_instrument_catalogue_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_instrument_catalogue_response_type_1 = PoolListResponse.from_dict(data)

            return componentsschemas_instrument_catalogue_response_type_1

        response_200 = _parse_response_200(response.json())

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
) -> Response[InstrumentListResponse | PoolListResponse | InsufficientScopeError | ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    exchange_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[InstrumentListResponse | PoolListResponse | InsufficientScopeError | ResponseError]:
    r"""List an exchange's instruments (default spot segment)

     \"Give me binance instruments\" — returns the exchange's DEFAULT segment (`spot`)
    in `data`, each instrument with per-data-type coverage and market info. `meta`
    confirms the served `segment` (`spot`); HAL `_links` carry `self` plus the
    `spot` / `futures` segment-discovery links.

    For a decentralized exchange (`venueType` `dex` in `GET /exchanges`) the instruments are its pools,
    each a `PoolDetail`, and the default segment is the first one the exchange lists (`uniswap-v3` for
    `robinhood`).

    Args:
        exchange_id (str):  Example: binance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstrumentListResponse | PoolListResponse | InsufficientScopeError | ResponseError]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    exchange_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> InstrumentListResponse | PoolListResponse | InsufficientScopeError | ResponseError | None:
    r"""List an exchange's instruments (default spot segment)

     \"Give me binance instruments\" — returns the exchange's DEFAULT segment (`spot`)
    in `data`, each instrument with per-data-type coverage and market info. `meta`
    confirms the served `segment` (`spot`); HAL `_links` carry `self` plus the
    `spot` / `futures` segment-discovery links.

    For a decentralized exchange (`venueType` `dex` in `GET /exchanges`) the instruments are its pools,
    each a `PoolDetail`, and the default segment is the first one the exchange lists (`uniswap-v3` for
    `robinhood`).

    Args:
        exchange_id (str):  Example: binance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstrumentListResponse | PoolListResponse | InsufficientScopeError | ResponseError
    """

    return sync_detailed(
        exchange_id=exchange_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    exchange_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[InstrumentListResponse | PoolListResponse | InsufficientScopeError | ResponseError]:
    r"""List an exchange's instruments (default spot segment)

     \"Give me binance instruments\" — returns the exchange's DEFAULT segment (`spot`)
    in `data`, each instrument with per-data-type coverage and market info. `meta`
    confirms the served `segment` (`spot`); HAL `_links` carry `self` plus the
    `spot` / `futures` segment-discovery links.

    For a decentralized exchange (`venueType` `dex` in `GET /exchanges`) the instruments are its pools,
    each a `PoolDetail`, and the default segment is the first one the exchange lists (`uniswap-v3` for
    `robinhood`).

    Args:
        exchange_id (str):  Example: binance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstrumentListResponse | PoolListResponse | InsufficientScopeError | ResponseError]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    exchange_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> InstrumentListResponse | PoolListResponse | InsufficientScopeError | ResponseError | None:
    r"""List an exchange's instruments (default spot segment)

     \"Give me binance instruments\" — returns the exchange's DEFAULT segment (`spot`)
    in `data`, each instrument with per-data-type coverage and market info. `meta`
    confirms the served `segment` (`spot`); HAL `_links` carry `self` plus the
    `spot` / `futures` segment-discovery links.

    For a decentralized exchange (`venueType` `dex` in `GET /exchanges`) the instruments are its pools,
    each a `PoolDetail`, and the default segment is the first one the exchange lists (`uniswap-v3` for
    `robinhood`).

    Args:
        exchange_id (str):  Example: binance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstrumentListResponse | PoolListResponse | InsufficientScopeError | ResponseError
    """

    return (
        await asyncio_detailed(
            exchange_id=exchange_id,
            client=client,
        )
    ).parsed
