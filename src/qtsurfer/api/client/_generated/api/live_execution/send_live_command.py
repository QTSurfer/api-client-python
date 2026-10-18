from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.live_command_result import LiveCommandResult
from ...models.response_error import ResponseError
from ...models.send_live_command_request import SendLiveCommandRequest
from ...types import Response


def _get_kwargs(
    run_id: str,
    *,
    body: SendLiveCommandRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/live/{run_id}/commands".format(
            run_id=quote(str(run_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LiveCommandResult | ResponseError | None:
    if response.status_code == 202:
        response_202 = LiveCommandResult.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ResponseError.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ResponseError.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ResponseError.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = ResponseError.from_dict(response.json())

        return response_413

    if response.status_code == 503:
        response_503 = ResponseError.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LiveCommandResult | ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
    body: SendLiveCommandRequest,
) -> Response[LiveCommandResult | ResponseError]:
    r"""Tell a running strategy a command

     Tells a running strategy something **while it stays live**, without restarting it — for a strategy
    that
    implements the engine's `CommandRequestHandler`. Owner only.

    A command is an event, not a stored setting: it is delivered once to every execution behind the run,
    at
    the same market position, and nothing about it is written to the run's state. **It is transient** —
    a
    replica that restarts replays only its recent market history, so a command from before that only
    reaches
    one that was already running when it arrived. Anything the strategy needs to remember across a
    restart
    belongs in a parameter (`PUT /live/{runId}/params`), which does have a stored value; a command does
    not.

    The command's text is a plain string; an optional `properties` object of your own choosing travels
    alongside it. Each entry lands as a top-level entry on the `CommandRequest` the handler receives —
    `request.get(\"<key>\")` in Java, `$command.<key>` sugar in QTScript — no key is off limits, since
    the
    command's own text is kept separately.

    Args:
        run_id (str):
        body (SendLiveCommandRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiveCommandResult | ResponseError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: str,
    *,
    client: AuthenticatedClient,
    body: SendLiveCommandRequest,
) -> LiveCommandResult | ResponseError | None:
    r"""Tell a running strategy a command

     Tells a running strategy something **while it stays live**, without restarting it — for a strategy
    that
    implements the engine's `CommandRequestHandler`. Owner only.

    A command is an event, not a stored setting: it is delivered once to every execution behind the run,
    at
    the same market position, and nothing about it is written to the run's state. **It is transient** —
    a
    replica that restarts replays only its recent market history, so a command from before that only
    reaches
    one that was already running when it arrived. Anything the strategy needs to remember across a
    restart
    belongs in a parameter (`PUT /live/{runId}/params`), which does have a stored value; a command does
    not.

    The command's text is a plain string; an optional `properties` object of your own choosing travels
    alongside it. Each entry lands as a top-level entry on the `CommandRequest` the handler receives —
    `request.get(\"<key>\")` in Java, `$command.<key>` sugar in QTScript — no key is off limits, since
    the
    command's own text is kept separately.

    Args:
        run_id (str):
        body (SendLiveCommandRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiveCommandResult | ResponseError
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
    body: SendLiveCommandRequest,
) -> Response[LiveCommandResult | ResponseError]:
    r"""Tell a running strategy a command

     Tells a running strategy something **while it stays live**, without restarting it — for a strategy
    that
    implements the engine's `CommandRequestHandler`. Owner only.

    A command is an event, not a stored setting: it is delivered once to every execution behind the run,
    at
    the same market position, and nothing about it is written to the run's state. **It is transient** —
    a
    replica that restarts replays only its recent market history, so a command from before that only
    reaches
    one that was already running when it arrived. Anything the strategy needs to remember across a
    restart
    belongs in a parameter (`PUT /live/{runId}/params`), which does have a stored value; a command does
    not.

    The command's text is a plain string; an optional `properties` object of your own choosing travels
    alongside it. Each entry lands as a top-level entry on the `CommandRequest` the handler receives —
    `request.get(\"<key>\")` in Java, `$command.<key>` sugar in QTScript — no key is off limits, since
    the
    command's own text is kept separately.

    Args:
        run_id (str):
        body (SendLiveCommandRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiveCommandResult | ResponseError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    *,
    client: AuthenticatedClient,
    body: SendLiveCommandRequest,
) -> LiveCommandResult | ResponseError | None:
    r"""Tell a running strategy a command

     Tells a running strategy something **while it stays live**, without restarting it — for a strategy
    that
    implements the engine's `CommandRequestHandler`. Owner only.

    A command is an event, not a stored setting: it is delivered once to every execution behind the run,
    at
    the same market position, and nothing about it is written to the run's state. **It is transient** —
    a
    replica that restarts replays only its recent market history, so a command from before that only
    reaches
    one that was already running when it arrived. Anything the strategy needs to remember across a
    restart
    belongs in a parameter (`PUT /live/{runId}/params`), which does have a stored value; a command does
    not.

    The command's text is a plain string; an optional `properties` object of your own choosing travels
    alongside it. Each entry lands as a top-level entry on the `CommandRequest` the handler receives —
    `request.get(\"<key>\")` in Java, `$command.<key>` sugar in QTScript — no key is off limits, since
    the
    command's own text is kept separately.

    Args:
        run_id (str):
        body (SendLiveCommandRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiveCommandResult | ResponseError
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
            body=body,
        )
    ).parsed
