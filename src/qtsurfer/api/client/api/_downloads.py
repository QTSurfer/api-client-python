"""Binary response adapter shared by the hourly download endpoints."""

from http import HTTPStatus
from typing import Any
from urllib.parse import quote as encode_path

import httpx

from qtsurfer.api.client._generated import errors
from qtsurfer.api.client._generated.client import AuthenticatedClient, Client
from qtsurfer.api.client._generated.models import ResponseError
from qtsurfer.api.client._generated.types import Response


def request_kwargs(kind: str, exchange_id: str, base: str, quote: str, hour: str, format_: str) -> dict[str, Any]:
    """Encode each path value independently, including the quote currency."""
    path = "/exchange/{}/{}/{}/{}".format(
        encode_path(exchange_id, safe=""), kind, encode_path(base, safe=""), encode_path(quote, safe="")
    )
    return {"method": "get", "url": path, "params": {"hour": hour, "format": format_}}


def build_response(client: AuthenticatedClient | Client, response: httpx.Response) -> Response[bytes | ResponseError]:
    """Keep successful bytes and metadata; parse documented errors without discarding recovery."""
    parsed: bytes | ResponseError | None
    if response.status_code == 200:
        parsed = response.content
    elif response.status_code in (400, 404, 500, 503):
        parsed = ResponseError.from_dict(response.json())
    elif client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        parsed = None
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=parsed,
    )
