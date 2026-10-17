"""Contract regressions for venue discovery, import requests and scope maps."""

import json

import httpx
import pytest
import respx

from qtsurfer.api.client import AuthenticatedClient, types
from qtsurfer.api.client.api.dataset import import_dataset
from qtsurfer.api.client.api.exchange import list_instruments, list_segment_instruments
from qtsurfer.api.client.models import (
    AuthTokenResponse,
    DatasetImportRequest,
    KeyScopes,
    LiveSourceRequest,
    PoolListResponse,
)

BASE = "https://api.example/v1"
POOL = "0x52e65b17fb6e5ba00ed806f37afcd2daa50271ca"


@pytest.mark.parametrize("segment", [None, "uniswap-v3"])
@respx.mock
def test_dex_catalogue_has_typed_pool_envelope(segment: str | None) -> None:
    payload = {
        "data": [
            {
                "id": POOL,
                "symbol": "WETH/USDG",
                "base": "WETH",
                "quote": "USDG",
                "baseAddress": "0xbase",
                "quoteAddress": "0xquote",
                "feePercent": 0.01,
                "tvlUsd": 10000,
                "volume24hUsd": 100,
            }
        ],
        "meta": {
            "updatedAt": "2026-10-17T10:00:00Z",
            "exchange": "robinhood",
            "segment": "uniswap-v3",
            "venueType": "dex",
            "minTvlUsd": 10000,
            "limit": 50,
        },
        "_links": {
            "self": {"href": "/v1/exchange/robinhood/instruments"},
            "uniswap-v3": {"href": "/v1/exchange/robinhood/uniswap-v3/instruments"},
        },
    }
    path = f"/exchange/robinhood/{segment}/instruments" if segment else "/exchange/robinhood/instruments"
    respx.get(BASE + path).mock(return_value=httpx.Response(200, json=payload))
    client = AuthenticatedClient(base_url=BASE, token="jwt")
    result = (
        list_segment_instruments.sync("robinhood", segment, client=client)
        if segment
        else list_instruments.sync("robinhood", client=client)
    )
    assert isinstance(result, PoolListResponse)
    assert result.meta.venue_type.value == "dex"
    assert result.data[0].id == POOL
    assert isinstance(result.data[0].last_price, types.Unset)
    assert isinstance(result.data[0].volume24h, types.Unset)
    assert isinstance(result.data[0].created_at, types.Unset)
    assert result.to_dict()["data"] == payload["data"]
    assert result.field_links["uniswap-v3"].href.endswith("/uniswap-v3/instruments")


def test_nonempty_scope_map_roundtrips() -> None:
    payload = {
        "access_token": "jwt",
        "token_type": "Bearer",
        "expires_in": 3600,
        "tier": "pro",
        "scopes": {"backtests": ["read", "write", "execute"], "exchanges": ["read"]},
    }
    token = AuthTokenResponse.from_dict(payload)
    assert isinstance(token.scopes, KeyScopes)
    assert token.scopes["backtests"] == ["read", "write", "execute"]
    assert token.to_dict() == payload


@respx.mock
def test_cex_import_posts_typed_source_and_expanded_cadence() -> None:
    payload = {
        "name": "BTC history",
        "instrument": "BTC/USDT",
        "type": "cex",
        "cadence": "8h",
        "from": "2026-09-01T00:00:00Z",
        "to": "2026-09-02T00:00:00Z",
        "cex": {"exchange": "binance", "segment": "spot", "dataType": "klines"},
    }
    route = respx.post(BASE + "/datasets/imports").mock(
        return_value=httpx.Response(
            202,
            json={
                "datasetId": "ds-1",
                "importId": "im-1",
                "jobId": "job-1",
                "name": "BTC history",
                "instrument": "BTC/USDT",
                "status": "fetching",
            },
        )
    )
    result = import_dataset.sync_detailed(
        client=AuthenticatedClient(base_url=BASE, token="jwt"), body=DatasetImportRequest.from_dict(payload)
    )
    assert result.status_code == 202
    sent = json.loads(route.calls.last.request.content)
    assert sent["cex"] == payload["cex"]
    assert sent["type"] == "cex"
    assert sent["cadence"] == "8h"


def test_dex_live_source_uses_pool_address_and_kline() -> None:
    payload = {
        "venueType": "dex",
        "exchange": "robinhood",
        "segment": "uniswap-v3",
        "type": "kline",
        "instruments": [POOL],
    }
    assert LiveSourceRequest.from_dict(payload).to_dict() == payload
