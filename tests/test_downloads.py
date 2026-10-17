"""The public binary adapters preserve payloads, headers and recovery instructions."""

import asyncio
from types import ModuleType

import httpx
import pytest
import respx

from qtsurfer.api.client import AuthenticatedClient
from qtsurfer.api.client._generated.types import Unset
from qtsurfer.api.client.api.exchange import download_klines, download_tickers
from qtsurfer.api.client.models import DownloadKlinesFormat, ResponseError

BASE = "https://api.example/v1"


@pytest.mark.parametrize("endpoint", [download_tickers, download_klines])
@respx.mock
def test_download_preserves_success_bytes_and_provisional_metadata(endpoint: ModuleType) -> None:
    route = respx.get(url__regex=r"https://api.example/v1/exchange/.+").mock(
        return_value=httpx.Response(
            200,
            content=b"\x00Lastra\xff",
            headers={
                "Content-Type": "application/vnd.qtsurfer.lastra",
                "X-Ts-Unit": "micros",
                "X-Data-Status": "provisional",
                "X-Data-Through": "2026-10-17T10:03:00.175Z",
            },
        )
    )
    client = AuthenticatedClient(base_url=BASE, token="jwt", raise_on_unexpected_status=True)
    result = endpoint.sync_detailed("test venue", "W ETH", "USD+G", hour="2026-10-17T10", client=client)
    assert result.content == result.parsed == b"\x00Lastra\xff"
    assert result.headers["x-ts-unit"] == "micros"
    assert result.headers["x-data-status"] == "provisional"
    assert result.headers["x-data-through"] == "2026-10-17T10:03:00.175Z"
    assert route.calls.last.request.headers["Authorization"] == "Bearer jwt"
    assert b"test%20venue" in route.calls.last.request.url.raw_path
    assert b"USD%2BG" in route.calls.last.request.url.raw_path
    assert route.calls.last.request.url.params["format"] == "lastra"


@pytest.mark.parametrize(
    "status,reason",
    [(404, "NOT_YET_AVAILABLE"), (404, "NO_DATA"), (503, "TEMPORARILY_UNAVAILABLE"), (400, "OUTSIDE_WINDOW")],
)
@respx.mock
def test_download_parses_typed_recovery(status: int, reason: str) -> None:
    payload = {
        "code": status,
        "message": "Try another route",
        "reason": reason,
        "next": {"method": "POST", "path": "/datasets/imports", "body": {"type": "cex"}},
    }
    respx.get(f"{BASE}/exchange/binance/tickers/BTC/USDT").mock(
        return_value=httpx.Response(status, json=payload, headers={"Retry-After": "30"})
    )
    response = download_tickers.sync_detailed(
        "binance", "BTC", "USDT", hour="2026-10-17T10", client=AuthenticatedClient(base_url=BASE, token="jwt")
    )
    assert isinstance(response.parsed, ResponseError)
    assert response.parsed.reason == reason
    assert not isinstance(response.parsed.next_, Unset)
    assert response.parsed.next_.path == "/datasets/imports"
    assert not isinstance(response.parsed.next_.body, Unset)
    assert response.parsed.next_.body.to_dict() == {"type": "cex"}
    assert response.headers["retry-after"] == "30"


@respx.mock
def test_async_parquet_preserves_bytes() -> None:
    route = respx.get(f"{BASE}/exchange/binance/klines/BTC/USDT").mock(
        return_value=httpx.Response(200, content=b"PAR1")
    )
    client = AuthenticatedClient(base_url=BASE, token="jwt", raise_on_unexpected_status=True)
    response = asyncio.run(
        download_klines.asyncio_detailed(
            "binance", "BTC", "USDT", hour="2026-10-17T10", format_=DownloadKlinesFormat.PARQUET, client=client
        )
    )
    assert response.parsed == b"PAR1"
    assert route.calls.last.request.url.params["format"] == "parquet"
