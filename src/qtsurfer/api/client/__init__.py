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

# Re-export the generated public types.
from qtsurfer.api.client._generated import api, errors, models, types
from qtsurfer.api.client._generated.client import AuthenticatedClient, Client

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
