from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.live_params_update_result import LiveParamsUpdateResult
from ...models.response_error import ResponseError
from ...models.update_live_params_request import UpdateLiveParamsRequest
from ...types import Response


def _get_kwargs(
    run_id: str,
    *,
    body: UpdateLiveParamsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/live/{run_id}/params".format(
            run_id=quote(str(run_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LiveParamsUpdateResult | ResponseError | None:
    if response.status_code == 200:
        response_200 = LiveParamsUpdateResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ResponseError.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ResponseError.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ResponseError.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LiveParamsUpdateResult | ResponseError]:
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
    body: UpdateLiveParamsRequest,
) -> Response[LiveParamsUpdateResult | ResponseError]:
    r"""Change a running strategy's parameters

     Updates one or more parameters of a run **while it stays live** — unlike `params` on
    `POST /strategy/{strategyId}/live`, which only sets the starting values. Owner only.

    Every key in `params` must be one your strategy declares (see `declaredProperties` on
    `POST /strategy`) as of the compilation this run is executing — recompiling the strategy
    later never changes what an already-running instance accepts; start a new run for that.

    The change does not take effect the instant this call returns: `effectiveAtMs` is the
    earliest moment it is guaranteed to apply, a few seconds out, so both the REST and
    WebSocket paths to this same update (see the \"Live execution\" guide) land on the exact same
    value at the exact same moment.

    Args:
        run_id (str):
        body (UpdateLiveParamsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiveParamsUpdateResult | ResponseError]
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
    body: UpdateLiveParamsRequest,
) -> LiveParamsUpdateResult | ResponseError | None:
    r"""Change a running strategy's parameters

     Updates one or more parameters of a run **while it stays live** — unlike `params` on
    `POST /strategy/{strategyId}/live`, which only sets the starting values. Owner only.

    Every key in `params` must be one your strategy declares (see `declaredProperties` on
    `POST /strategy`) as of the compilation this run is executing — recompiling the strategy
    later never changes what an already-running instance accepts; start a new run for that.

    The change does not take effect the instant this call returns: `effectiveAtMs` is the
    earliest moment it is guaranteed to apply, a few seconds out, so both the REST and
    WebSocket paths to this same update (see the \"Live execution\" guide) land on the exact same
    value at the exact same moment.

    Args:
        run_id (str):
        body (UpdateLiveParamsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiveParamsUpdateResult | ResponseError
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
    body: UpdateLiveParamsRequest,
) -> Response[LiveParamsUpdateResult | ResponseError]:
    r"""Change a running strategy's parameters

     Updates one or more parameters of a run **while it stays live** — unlike `params` on
    `POST /strategy/{strategyId}/live`, which only sets the starting values. Owner only.

    Every key in `params` must be one your strategy declares (see `declaredProperties` on
    `POST /strategy`) as of the compilation this run is executing — recompiling the strategy
    later never changes what an already-running instance accepts; start a new run for that.

    The change does not take effect the instant this call returns: `effectiveAtMs` is the
    earliest moment it is guaranteed to apply, a few seconds out, so both the REST and
    WebSocket paths to this same update (see the \"Live execution\" guide) land on the exact same
    value at the exact same moment.

    Args:
        run_id (str):
        body (UpdateLiveParamsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiveParamsUpdateResult | ResponseError]
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
    body: UpdateLiveParamsRequest,
) -> LiveParamsUpdateResult | ResponseError | None:
    r"""Change a running strategy's parameters

     Updates one or more parameters of a run **while it stays live** — unlike `params` on
    `POST /strategy/{strategyId}/live`, which only sets the starting values. Owner only.

    Every key in `params` must be one your strategy declares (see `declaredProperties` on
    `POST /strategy`) as of the compilation this run is executing — recompiling the strategy
    later never changes what an already-running instance accepts; start a new run for that.

    The change does not take effect the instant this call returns: `effectiveAtMs` is the
    earliest moment it is guaranteed to apply, a few seconds out, so both the REST and
    WebSocket paths to this same update (see the \"Live execution\" guide) land on the exact same
    value at the exact same moment.

    Args:
        run_id (str):
        body (UpdateLiveParamsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiveParamsUpdateResult | ResponseError
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
            body=body,
        )
    ).parsed
