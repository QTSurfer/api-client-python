"""qtsurfer-api-client — auto-generated Python client for the QTSurfer API.

Low-level: one function per OpenAPI endpoint. For workflow orchestration
(``backtest = compile + prepare + execute + poll``), use
`qtsurfer-sdk <https://github.com/QTSurfer/sdk-python>`_ (coming soon).

Public surface (re-exported from the generated package):

* :class:`Client` — unauthenticated client (rarely useful in practice).
* :class:`AuthenticatedClient` — Bearer-token client; pass to every
  endpoint function as ``client=...``.
* :mod:`qtsurfer.api.client.api` — endpoint modules grouped by tag.
* :mod:`qtsurfer.api.client.models` — request/response dataclasses.

Endpoint modules expose four entry points: ``sync``, ``sync_detailed``,
``asyncio``, ``asyncio_detailed``. See the README for examples.
"""

from importlib.metadata import PackageNotFoundError, version

import httpx

# Re-export the generated public types.
from qtsurfer.api.client._generated import api, errors, models, types
from qtsurfer.api.client._generated.client import AuthenticatedClient as _GeneratedAuthenticatedClient
from qtsurfer.api.client._generated.client import Client as _GeneratedClient
from qtsurfer.api.client._network_failover import _FailoverAsyncClient, _FailoverClient


class Client(_GeneratedClient):
    """Unauthenticated client with one-shot API connection failover."""

    def get_httpx_client(self) -> httpx.Client:
        if self._client is None:
            self._client = _FailoverClient(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._client

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        if self._async_client is None:
            self._async_client = _FailoverAsyncClient(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._async_client


class AuthenticatedClient(_GeneratedAuthenticatedClient):
    """Bearer-token client with one-shot API connection failover."""

    def get_httpx_client(self) -> httpx.Client:
        if self._client is None:
            self._headers[self.auth_header_name] = f"{self.prefix} {self.token}" if self.prefix else self.token
            self._client = _FailoverClient(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._client

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        if self._async_client is None:
            self._headers[self.auth_header_name] = f"{self.prefix} {self.token}" if self.prefix else self.token
            self._async_client = _FailoverAsyncClient(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._async_client


try:
    __version__ = version("qtsurfer-api-client")
except PackageNotFoundError:  # pragma: no cover - editable installs in dev
    __version__ = "0.0.0+unknown"

__all__ = [
    "AuthenticatedClient",
    "Client",
    "__version__",
    "api",
    "errors",
    "models",
    "types",
]
