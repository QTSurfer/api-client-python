"""HTTP-level tests — mount respx over the underlying httpx client and
verify that endpoint calls produce the expected request shape and parse
the response into typed models."""

from __future__ import annotations

from datetime import datetime

import httpx
import pytest
import respx

from qtsurfer.api.client import AuthenticatedClient, types
from qtsurfer.api.client.api.backtesting import get_backtest_result, get_sweep_run_equity_curve
from qtsurfer.api.client.api.dataset import finalize_dataset_upload, list_datasets, open_dataset_upload
from qtsurfer.api.client.api.exchange import list_exchanges, list_instruments
from qtsurfer.api.client.api.live_execution import get_live_run_signals, send_live_command
from qtsurfer.api.client.api.strategy import (
    delete_strategy,
    get_strategy,
    get_strategy_code,
    list_strategies,
    validate_strategy,
)
from qtsurfer.api.client.models import (
    CoverageWindow,
    DatasetUploadSession,
    DataSourceType,
    DeleteStrategyResponse200,
    EquityCurveResult,
    Exchange,
    GetBacktestResultResponse202,
    GetStrategyCodeResponse200,
    HalLink,
    InstrumentCoverage,
    InstrumentDetail,
    InstrumentListResponse,
    ListStrategiesResponse200,
    LiveCommandResult,
    ResponseError,
    SendLiveCommandRequest,
    SendLiveCommandRequestProperties,
    StrategyLinks,
    StrategyState,
    StrategySummary,
)

BASE_URL = "https://api.qtsurfer.test/v1"


@pytest.fixture
def client() -> AuthenticatedClient:
    return AuthenticatedClient(base_url=BASE_URL, token="test-token")


@respx.mock
def test_list_exchanges_request_and_response(client: AuthenticatedClient) -> None:
    route = respx.get(f"{BASE_URL}/exchanges").mock(
        return_value=httpx.Response(
            200,
            json=[
                {"id": "binance", "name": "Binance", "description": "Binance"},
                {"id": "bybit", "name": "Bybit"},
            ],
        )
    )

    exchanges = list_exchanges.sync(client=client)

    assert route.called
    # Verify request shape: bearer token + correct URL/method.
    sent = route.calls.last.request
    assert sent.method == "GET"
    assert sent.url == httpx.URL(f"{BASE_URL}/exchanges")
    assert sent.headers["Authorization"] == "Bearer test-token"

    # Verify response was parsed into typed models.
    assert exchanges is not None
    assert len(exchanges) == 2
    assert isinstance(exchanges[0], Exchange)
    assert exchanges[0].id == "binance"
    assert exchanges[1].id == "bybit"


@respx.mock
def test_list_instruments_path_param_interpolated(client: AuthenticatedClient) -> None:
    payload = {
        "data": [
            {
                "id": "BTC/USDT",
                "base": "BTC",
                "quote": "USDT",
                "coverage": {
                    "tickers": {
                        "from": "2026-01-15T00:00:00Z",
                        "to": "2026-01-15T18:00:00Z",
                    }
                },
                "lastPrice": 84250.5,
                "volume24h": 1234567.89,
            }
        ],
        "meta": {
            "updatedAt": "2026-01-15T18:00:00Z",
            "exchange": "binance",
            "segment": "spot",
        },
        "_links": {"self": {"href": "/v1/exchange/binance/instruments"}},
    }
    route = respx.get(f"{BASE_URL}/exchange/binance/instruments").mock(return_value=httpx.Response(200, json=payload))

    response = list_instruments.sync(client=client, exchange_id="binance")

    assert route.called
    assert isinstance(response, InstrumentListResponse)
    assert len(response.data) == 1
    first = response.data[0]
    assert isinstance(first, InstrumentDetail)
    assert first.base == "BTC"
    assert first.quote == "USDT"
    coverage = first.coverage
    assert isinstance(coverage, InstrumentCoverage)
    assert isinstance(coverage.tickers, CoverageWindow)
    assert isinstance(coverage.tickers.from_, datetime)
    assert isinstance(coverage.tickers.to, datetime)
    assert coverage.tickers.from_.isoformat().startswith("2026-01-15T00:00:00")
    assert coverage.tickers.to.isoformat().startswith("2026-01-15T18:00:00")


@respx.mock
def test_list_instruments_detailed_returns_status(client: AuthenticatedClient) -> None:
    respx.get(f"{BASE_URL}/exchange/unknown/instruments").mock(
        return_value=httpx.Response(
            404,
            json={"code": "EXCHANGE_NOT_FOUND", "message": "no such exchange"},
        )
    )

    response = list_instruments.sync_detailed(client=client, exchange_id="unknown")

    assert response.status_code == 404
    # parsed is the ResponseError model on the documented 404 branch.
    assert response.parsed is not None


@respx.mock
def test_get_backtest_result_202_is_not_deserialized_as_a_result_map(client: AuthenticatedClient) -> None:
    respx.get(f"{BASE_URL}/backtest/binance/ticker/execute/queued-job").mock(return_value=httpx.Response(202, json={}))

    response = get_backtest_result.sync_detailed(
        client=client,
        exchange_id="binance",
        type_=DataSourceType.TICKER,
        job_id="queued-job",
    )

    assert response.status_code == 202
    assert isinstance(response.parsed, GetBacktestResultResponse202)


@respx.mock
def test_list_strategies_request_and_response(client: AuthenticatedClient) -> None:
    payload = {
        "strategies": [
            {
                "strategyId": "6bsh31ikwkuivhtgcoa6s4",
                "compiledAt": "2026-08-19T10:15:00Z",
                "requiredSources": ["Ticker"],
            },
            {"strategyId": "2ul144qe9tlwzu5anhwvc6"},
        ]
    }
    route = respx.get(f"{BASE_URL}/strategies").mock(return_value=httpx.Response(200, json=payload))

    response = list_strategies.sync(client=client)

    assert route.called
    assert route.calls.last.request.method == "GET"
    assert isinstance(response, ListStrategiesResponse200)
    assert len(response.strategies) == 2
    first = response.strategies[0]
    assert isinstance(first, StrategySummary)
    assert first.strategy_id == "6bsh31ikwkuivhtgcoa6s4"
    assert first.required_sources == ["Ticker"]
    # list_strategies never 404s and deliberately omits validation state — the
    # item model carries no such field at all, unlike get_strategy's StrategyState.
    assert not hasattr(first, "validation")


@respx.mock
def test_list_strategies_can_include_deleted(client: AuthenticatedClient) -> None:
    route = respx.get(f"{BASE_URL}/strategies").mock(return_value=httpx.Response(200, json={
        "strategies": [{"strategyId": "deleted-1", "deletedAt": "2026-09-01T12:00:00Z"}],
    }))

    response = list_strategies.sync(client=client, include_deleted=True)

    assert route.called
    assert route.calls.last.request.url.params["includeDeleted"] == "true"
    assert isinstance(response, ListStrategiesResponse200)
    assert not isinstance(response.strategies[0].deleted_at, types.Unset)
    assert response.strategies[0].deleted_at.isoformat() == "2026-09-01T12:00:00+00:00"


@respx.mock
def test_list_datasets_can_include_deleted(client: AuthenticatedClient) -> None:
    route = respx.get(f"{BASE_URL}/datasets").mock(
        return_value=httpx.Response(200, json={"datasets": []})
    )

    response = list_datasets.sync(client=client, include_deleted=True)

    assert route.called
    assert route.calls.last.request.url.params["includeDeleted"] == "true"
    assert response is not None


@respx.mock
def test_send_live_command_posts_properties_and_parses_accepted_response(
    client: AuthenticatedClient,
) -> None:
    route = respx.post(f"{BASE_URL}/live/run-1/commands").mock(return_value=httpx.Response(202, json={
        "runId": "run-1", "commandId": "cmd-1", "effectiveAtMs": 1_758_330_015_000,
    }))
    properties = SendLiveCommandRequestProperties()
    properties["targetWeight"] = 0.25

    response = send_live_command.sync_detailed(
        run_id="run-1",
        body=SendLiveCommandRequest(command="rebalance", properties=properties),
        client=client,
    )

    assert route.called
    sent = route.calls.last.request
    assert sent.headers["Authorization"] == "Bearer test-token"
    assert sent.read() == b'{"command":"rebalance","properties":{"targetWeight":0.25}}'
    assert response.status_code == 202
    assert isinstance(response.parsed, LiveCommandResult)
    assert response.parsed.command_id == "cmd-1"


@respx.mock
def test_delete_strategy_request_and_response(client: AuthenticatedClient) -> None:
    route = respx.delete(f"{BASE_URL}/strategy/6bsh31ikwkuivhtgcoa6s4").mock(
        return_value=httpx.Response(200, json={"strategyId": "6bsh31ikwkuivhtgcoa6s4", "deleted": True})
    )

    response = delete_strategy.sync(strategy_id="6bsh31ikwkuivhtgcoa6s4", client=client)

    assert route.called
    sent = route.calls.last.request
    assert sent.method == "DELETE"
    assert sent.url == httpx.URL(f"{BASE_URL}/strategy/6bsh31ikwkuivhtgcoa6s4")
    assert isinstance(response, DeleteStrategyResponse200)
    assert response.strategy_id == "6bsh31ikwkuivhtgcoa6s4"
    assert response.deleted is True


@respx.mock
def test_delete_strategy_not_found(client: AuthenticatedClient) -> None:
    respx.delete(f"{BASE_URL}/strategy/unknown-id").mock(
        return_value=httpx.Response(404, json={"code": 404, "message": "no such registered strategy"})
    )

    response = delete_strategy.sync_detailed(strategy_id="unknown-id", client=client)

    assert response.status_code == 404
    assert isinstance(response.parsed, ResponseError)
    assert response.parsed.message == "no such registered strategy"


@respx.mock
def test_get_strategy_code_request_and_response(client: AuthenticatedClient) -> None:
    source = "package strategy;\npublic class EmaCrossStrategy extends AbstractTickerStrategy { }\n"
    route = respx.get(f"{BASE_URL}/strategy/6bsh31ikwkuivhtgcoa6s4/code").mock(
        return_value=httpx.Response(200, json={"strategyId": "6bsh31ikwkuivhtgcoa6s4", "code": source})
    )

    response = get_strategy_code.sync(strategy_id="6bsh31ikwkuivhtgcoa6s4", client=client)

    assert route.called
    assert isinstance(response, GetStrategyCodeResponse200)
    assert response.strategy_id == "6bsh31ikwkuivhtgcoa6s4"
    assert response.code == source


@respx.mock
def test_get_strategy_response_carries_links(client: AuthenticatedClient) -> None:
    payload = {
        "strategyId": "6bsh31ikwkuivhtgcoa6s4",
        "validation": "passed",
        "_links": {"code": {"href": "/v1/strategy/6bsh31ikwkuivhtgcoa6s4/code"}},
    }
    route = respx.get(f"{BASE_URL}/strategy/6bsh31ikwkuivhtgcoa6s4").mock(
        return_value=httpx.Response(200, json=payload)
    )

    response = get_strategy.sync(strategy_id="6bsh31ikwkuivhtgcoa6s4", client=client)

    assert route.called
    assert isinstance(response, StrategyState)
    assert isinstance(response.field_links, StrategyLinks)
    assert isinstance(response.field_links.code, HalLink)
    assert response.field_links.code.href == "/v1/strategy/6bsh31ikwkuivhtgcoa6s4/code"


@respx.mock
def test_validate_strategy_202_omits_links(client: AuthenticatedClient) -> None:
    # A 202 means a check was just queued — a deliberately partial stub with
    # nothing to link to yet, so `_links` is absent entirely rather than null.
    # `field_links` must come back Unset, not None or a default StrategyLinks.
    payload = {"strategyId": "6bsh31ikwkuivhtgcoa6s4", "validation": "pending"}
    respx.post(f"{BASE_URL}/strategy/6bsh31ikwkuivhtgcoa6s4/validate").mock(
        return_value=httpx.Response(202, json=payload)
    )

    response = validate_strategy.sync_detailed(strategy_id="6bsh31ikwkuivhtgcoa6s4", client=client)

    assert response.status_code == 202
    assert isinstance(response.parsed, StrategyState)
    assert isinstance(response.parsed.field_links, types.Unset)


@respx.mock
def test_get_strategy_code_not_found_covers_two_cases(client: AuthenticatedClient) -> None:
    # 404 here is deliberately the same shape whether the id was never
    # registered by this caller or resolves only through a shared/marketplace
    # reference with no source of its own — the response cannot and does not
    # distinguish them.
    respx.get(f"{BASE_URL}/strategy/reference-only/code").mock(
        return_value=httpx.Response(404, json={"code": 404, "message": "no source available for this strategy"})
    )

    response = get_strategy_code.sync_detailed(strategy_id="reference-only", client=client)

    assert response.status_code == 404
    assert isinstance(response.parsed, ResponseError)


@respx.mock
def test_get_sweep_run_equity_curve_request_and_response(client: AuthenticatedClient) -> None:
    route = respx.get(f"{BASE_URL}/backtest/binance/ticker/executeSweep/request-1/sweep-1/runs/3/equityCurve").mock(
        return_value=httpx.Response(
            200,
            json={
                "points": [{"timestamp": 1_700_000_000_000, "equity": 100.0}],
                "meta": {
                    "inputPointCount": 1,
                    "outputPointCount": 1,
                    "resampled": False,
                    "differential": False,
                    "outMode": "ARRAY",
                },
            },
        )
    )

    response = get_sweep_run_equity_curve.sync(
        exchange_id="binance",
        type_=DataSourceType.TICKER,
        request_id="request-1",
        sweep_id="sweep-1",
        run_ix=3,
        resample=200,
        client=client,
    )

    assert route.called
    assert route.calls.last.request.url.params["outMode"] == "ARRAY"
    assert route.calls.last.request.url.params["resample"] == "200"
    assert isinstance(response, EquityCurveResult)
    assert not isinstance(response.points, types.Unset)
    assert response.points[0].timestamp == 1_700_000_000_000


@respx.mock
def test_open_dataset_upload_and_finalize_spent_upload(client: AuthenticatedClient) -> None:
    session_route = respx.post(f"{BASE_URL}/datasets/dataset-1/uploads").mock(
        return_value=httpx.Response(
            201,
            json={
                "uploadId": "upload-2",
                "upload": {"url": "https://storage.example/upload-2", "expiresInMinutes": 15},
            },
        )
    )
    finalized_route = respx.post(f"{BASE_URL}/datasets/dataset-1/uploads/upload-1/finalize").mock(
        return_value=httpx.Response(409, json={"code": 409, "message": "upload already finalized"})
    )

    opened = open_dataset_upload.sync(dataset_id="dataset-1", client=client)
    finalized = finalize_dataset_upload.sync_detailed(dataset_id="dataset-1", upload_id="upload-1", client=client)

    assert session_route.called
    assert isinstance(opened, DatasetUploadSession)
    assert opened.upload_id == "upload-2"
    assert opened.upload.url == "https://storage.example/upload-2"
    assert finalized_route.called
    assert finalized.status_code == 409
    assert isinstance(finalized.parsed, ResponseError)


@respx.mock
def test_get_live_run_signals_expired_cursor_is_a_typed_response(client: AuthenticatedClient) -> None:
    route = respx.get(f"{BASE_URL}/live/run-1/signals").mock(
        return_value=httpx.Response(
            410,
            json={"code": 410, "message": "cursor expired", "availableSinceMs": 1_700_000_000_000},
        )
    )

    response = get_live_run_signals.sync_detailed(run_id="run-1", cursor="expired", client=client)

    assert route.called
    assert route.calls.last.request.url.params["cursor"] == "expired"
    assert response.status_code == 410
    assert isinstance(response.parsed, ResponseError)
    assert response.parsed.additional_properties["availableSinceMs"] == 1_700_000_000_000
