"""Download one recent UTC hour of klines with binary data and recovery metadata.

Lastra timestamps are microseconds; Parquet timestamps remain milliseconds.
Detailed calls retain provisional headers and ``Retry-After``. Older history is
available through dataset imports; ``OUTSIDE_WINDOW`` supplies the next call.
"""

from qtsurfer.api.client._generated.client import AuthenticatedClient, Client
from qtsurfer.api.client._generated.models import DownloadKlinesFormat, ResponseError
from qtsurfer.api.client._generated.types import UNSET, Response, Unset

from ._downloads import build_response, request_kwargs


def sync_detailed(
    exchange_id: str,
    base: str,
    quote: str,
    *,
    client: AuthenticatedClient | Client,
    hour: str,
    format_: DownloadKlinesFormat | Unset = DownloadKlinesFormat.LASTRA,
) -> Response[bytes | ResponseError]:
    """Return bytes on 200, or a typed error, retaining status and all response headers."""
    fmt = DownloadKlinesFormat.LASTRA if format_ is UNSET else format_
    kwargs = request_kwargs("klines", exchange_id, base, quote, hour, str(fmt))
    return build_response(client, client.get_httpx_client().request(**kwargs))


def sync(
    exchange_id: str,
    base: str,
    quote: str,
    *,
    client: AuthenticatedClient | Client,
    hour: str,
    format_: DownloadKlinesFormat | Unset = DownloadKlinesFormat.LASTRA,
) -> bytes | ResponseError | None:
    """Return successful bytes or a typed error; use the detailed variant for metadata."""
    return sync_detailed(exchange_id, base, quote, client=client, hour=hour, format_=format_).parsed


async def asyncio_detailed(
    exchange_id: str,
    base: str,
    quote: str,
    *,
    client: AuthenticatedClient | Client,
    hour: str,
    format_: DownloadKlinesFormat | Unset = DownloadKlinesFormat.LASTRA,
) -> Response[bytes | ResponseError]:
    """Asynchronously return successful bytes or a typed error and response metadata."""
    fmt = DownloadKlinesFormat.LASTRA if format_ is UNSET else format_
    kwargs = request_kwargs("klines", exchange_id, base, quote, hour, str(fmt))
    return build_response(client, await client.get_async_httpx_client().request(**kwargs))


async def asyncio(
    exchange_id: str,
    base: str,
    quote: str,
    *,
    client: AuthenticatedClient | Client,
    hour: str,
    format_: DownloadKlinesFormat | Unset = DownloadKlinesFormat.LASTRA,
) -> bytes | ResponseError | None:
    """Asynchronously return bytes or a typed error; detailed calls retain metadata."""
    return (await asyncio_detailed(exchange_id, base, quote, client=client, hour=hour, format_=format_)).parsed
