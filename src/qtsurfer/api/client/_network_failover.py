"""Connection failover for the production API hostname."""

from __future__ import annotations

from typing import Any

import httpx


def _backup_request(request: httpx.Request) -> httpx.Request | None:
    host = request.url.host
    primary_label, separator, suffix = host.partition(".")
    if primary_label != "api" or not separator:
        return None

    return httpx.Request(
        method=request.method,
        url=request.url.copy_with(host=f"api2.{suffix}"),
        headers=request.headers,
        content=request.content,
        extensions=request.extensions,
    )


class _FailoverClient(httpx.Client):
    """Retry a failed connection to the primary API through api2 once."""

    def send(self, request: httpx.Request, **kwargs: Any) -> httpx.Response:
        try:
            return super().send(request, **kwargs)
        except (httpx.ConnectError, httpx.ConnectTimeout):
            backup = _backup_request(request)
            if backup is None:
                raise
            return super().send(backup, **kwargs)


class _FailoverAsyncClient(httpx.AsyncClient):
    """Async counterpart to :class:`_FailoverClient`."""

    async def send(self, request: httpx.Request, **kwargs: Any) -> httpx.Response:
        try:
            return await super().send(request, **kwargs)
        except (httpx.ConnectError, httpx.ConnectTimeout):
            backup = _backup_request(request)
            if backup is None:
                raise
            return await super().send(backup, **kwargs)
