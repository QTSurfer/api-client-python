"""HTTP-level tests — mount respx over the underlying httpx client and
verify that endpoint calls produce the expected request shape and parse
the response into typed models."""

from __future__ import annotations

import httpx
import pytest
import respx

from qtsurfer.api.client import AuthenticatedClient
from qtsurfer.api.client.api.exchange import get_exchanges, get_instruments
from qtsurfer.api.client.models import Exchange, InstrumentDetail

BASE_URL = "https://api.qtsurfer.test/v1"


@pytest.fixture
def client() -> AuthenticatedClient:
    return AuthenticatedClient(base_url=BASE_URL, token="test-token")


@respx.mock
def test_get_exchanges_request_and_response(client: AuthenticatedClient) -> None:
    route = respx.get(f"{BASE_URL}/exchanges").mock(
        return_value=httpx.Response(
            200,
            json=[
                {"id": "binance", "name": "Binance", "description": "Binance"},
                {"id": "bybit", "name": "Bybit"},
            ],
        )
    )

    exchanges = get_exchanges.sync(client=client)

    assert route.called
    # Verify request shape: bearer token + correct URL/method.
    sent = route.calls.last.request
    assert sent.method == "GET"
    assert sent.url == httpx.URL(f"{BASE_URL}/exchanges")
    assert sent.headers["Authorization"] == "Bearer test-token"

    # Verify response was parsed into typed models.
    assert exchanges is not None
    assert len(exchanges) == 2
    assert isinstance(exchanges[0], Exchange)
    assert exchanges[0].id == "binance"
    assert exchanges[1].id == "bybit"


@respx.mock
def test_get_instruments_path_param_interpolated(client: AuthenticatedClient) -> None:
    payload = [
        {
            "id": "BTC/USDT",
            "base": "BTC",
            "quote": "USDT",
            "dataFrom": "2026-01-15T00:00:00Z",
            "dataTo": "2026-01-15T18:00:00Z",
            "lastPrice": 84250.5,
            "volume24h": 1234567.89,
        }
    ]
    route = respx.get(f"{BASE_URL}/exchange/binance/instruments").mock(return_value=httpx.Response(200, json=payload))

    instruments = get_instruments.sync(client=client, exchange_id="binance")

    assert route.called
    assert isinstance(instruments, list)
    assert len(instruments) == 1
    first = instruments[0]
    assert isinstance(first, InstrumentDetail)
    assert first.base == "BTC"
    assert first.quote == "USDT"


@respx.mock
def test_get_instruments_detailed_returns_status(client: AuthenticatedClient) -> None:
    respx.get(f"{BASE_URL}/exchange/unknown/instruments").mock(
        return_value=httpx.Response(
            404,
            json={"code": "EXCHANGE_NOT_FOUND", "message": "no such exchange"},
        )
    )

    response = get_instruments.sync_detailed(client=client, exchange_id="unknown")

    assert response.status_code == 404
    # parsed is the ResponseError model on the documented 404 branch.
    assert response.parsed is not None
