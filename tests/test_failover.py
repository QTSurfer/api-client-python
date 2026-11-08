"""One-shot failover is restricted to the production API host and network errors."""

import asyncio

import httpx
import pytest

from qtsurfer.api.client import AuthenticatedClient


@pytest.mark.parametrize("suffix", ["qtsurfer.net", "qtsurfer.com"])
def test_sync_connection_failure_retries_backup_then_next_request_starts_primary(suffix: str) -> None:
    hosts: list[str] = []
    primary = f"api.{suffix}"
    backup = f"api2.{suffix}"

    def handler(request: httpx.Request) -> httpx.Response:
        hosts.append(request.url.host)
        if request.url.host == primary and hosts.count(primary) == 1:
            raise httpx.ConnectError("primary unavailable", request=request)
        return httpx.Response(200, json={"ok": True})

    client = AuthenticatedClient(
        base_url=f"https://{primary}/v1",
        token="test-token",
        httpx_args={"transport": httpx.MockTransport(handler)},
    )

    http = client.get_httpx_client()
    assert http.get("/status").json() == {"ok": True}
    assert http.get("/status").json() == {"ok": True}

    assert hosts == [primary, backup, primary]


def test_api2_host_is_not_rewritten_again() -> None:
    hosts: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        hosts.append(request.url.host)
        raise httpx.ConnectError("backup unavailable", request=request)

    client = AuthenticatedClient(
        base_url="https://api2.qtsurfer.com/v1",
        token="test-token",
        httpx_args={"transport": httpx.MockTransport(handler)},
    )

    with pytest.raises(httpx.ConnectError):
        client.get_httpx_client().get("/status")
    assert hosts == ["api2.qtsurfer.com"]


def test_http_response_does_not_retry() -> None:
    hosts: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        hosts.append(request.url.host)
        return httpx.Response(503)

    client = AuthenticatedClient(
        base_url="https://api.qtsurfer.net/v1",
        token="test-token",
        httpx_args={"transport": httpx.MockTransport(handler)},
    )

    assert client.get_httpx_client().get("/status").status_code == 503
    assert hosts == ["api.qtsurfer.net"]


def test_async_connection_failure_retries_backup() -> None:
    hosts: list[str] = []

    class Transport(httpx.AsyncBaseTransport):
        async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
            hosts.append(request.url.host)
            if request.url.host == "api.qtsurfer.net":
                raise httpx.ConnectError("primary unavailable", request=request)
            return httpx.Response(200, json={"ok": True})

    client = AuthenticatedClient(
        base_url="https://api.qtsurfer.net/v1",
        token="test-token",
        httpx_args={"transport": Transport()},
    )

    async def run() -> None:
        response = await client.get_async_httpx_client().get("/status")
        assert response.json() == {"ok": True}

    asyncio.run(run())
    assert hosts == ["api.qtsurfer.net", "api2.qtsurfer.net"]
