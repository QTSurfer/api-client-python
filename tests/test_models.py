"""Round-trip a few representative attrs-generated models through their
``to_dict`` / ``from_dict`` plumbing — proves the codec is wired and that
optional/datetime fields survive serialization."""

from __future__ import annotations

import datetime as _dt

from qtsurfer.api.client import types
from qtsurfer.api.client.models import (
    CoverageWindow,
    DatasetCreated,
    DatasetCreatedType,
    DatasetStatus,
    DatasetTimestampUnit,
    DatasetType,
    DatasetUploadTarget,
    DatasetVersion,
    DatasetVersionDataFormat,
    DatasetWithLinks,
    DatasetWithLinksDataFormat,
    EquityCurveMeta,
    EquityCurveOutMode,
    EquityCurveResult,
    EquityPoint,
    Exchange,
    ExecuteBacktestBody,
    ExecuteBacktestBodyParams,
    HalLink,
    InstrumentCoverage,
    InstrumentDetail,
    JobState,
    JobStateStatus,
    ListStrategiesResponse200,
    LiveSignal,
    LiveSignalInstrument,
    LiveSignalPage,
    LiveSignalStage,
    LiveSignalType,
    ResultMap,
    ResultMapParams,
    ScalarStrategyParamValue,
    StrategyLinks,
    StrategyState,
    StrategyStateValidation,
    StrategySummary,
)


def test_exchange_roundtrip_minimal() -> None:
    original = Exchange(id="binance", name="Binance")
    payload = original.to_dict()
    parsed = Exchange.from_dict(payload)
    assert parsed.id == "binance"
    assert parsed.name == "Binance"
    # description is Unset on input, must remain Unset after round-trip.
    assert isinstance(parsed.description, type(original.description))


def test_exchange_roundtrip_full() -> None:
    original = Exchange(
        id="bybit",
        name="Bybit",
        description="Bybit derivatives exchange",
    )
    parsed = Exchange.from_dict(original.to_dict())
    assert parsed.id == "bybit"
    assert parsed.name == "Bybit"
    assert parsed.description == "Bybit derivatives exchange"


def test_instrument_detail_roundtrip_with_datetime() -> None:
    data_from = _dt.datetime(2026, 1, 15, 10, 0, 0, tzinfo=_dt.UTC)
    data_to = _dt.datetime(2026, 1, 15, 18, 0, 0, tzinfo=_dt.UTC)
    original = InstrumentDetail(
        id="BTC/USDT",
        base="BTC",
        quote="USDT",
        coverage=InstrumentCoverage(tickers=CoverageWindow(from_=data_from, to=data_to)),
        last_price=84250.5,
        volume24h=1234567.89,
    )
    payload = original.to_dict()
    # datetimes serialise to ISO-8601 strings; the wire key for `from_` is `from`.
    assert isinstance(payload["coverage"]["tickers"]["from"], str)
    assert payload["coverage"]["tickers"]["from"].startswith("2026-01-15T10:00:00")
    parsed = InstrumentDetail.from_dict(payload)
    assert parsed.base == "BTC"
    assert parsed.quote == "USDT"
    assert isinstance(parsed.coverage, InstrumentCoverage)
    assert isinstance(parsed.coverage.tickers, CoverageWindow)
    assert parsed.coverage.tickers.from_ == data_from
    assert parsed.coverage.tickers.to == data_to
    assert parsed.last_price == 84250.5


def test_strategy_state_roundtrip_with_links() -> None:
    original = StrategyState(
        strategy_id="6bsh31ikwkuivhtgcoa6s4",
        validation=StrategyStateValidation.PASSED,
        field_links=StrategyLinks(code=HalLink(href="/v1/strategy/6bsh31ikwkuivhtgcoa6s4/code")),
    )
    payload = original.to_dict()
    # wire key is `_links`, nested under it `code.href` — same envelope shape as
    # InstrumentListResponse's `_links`, just a different link set.
    assert payload["_links"]["code"]["href"] == "/v1/strategy/6bsh31ikwkuivhtgcoa6s4/code"

    parsed = StrategyState.from_dict(payload)
    assert isinstance(parsed.field_links, StrategyLinks)
    assert isinstance(parsed.field_links.code, HalLink)
    assert parsed.field_links.code.href == "/v1/strategy/6bsh31ikwkuivhtgcoa6s4/code"


def test_strategy_state_roundtrip_without_links() -> None:
    # The 202 from validate_strategy omits `_links` entirely — field_links must
    # stay Unset rather than become None or a default-constructed StrategyLinks.
    original = StrategyState(strategy_id="6bsh31ikwkuivhtgcoa6s4", validation=StrategyStateValidation.PENDING)
    payload = original.to_dict()
    assert "_links" not in payload

    parsed = StrategyState.from_dict(payload)
    assert isinstance(parsed.field_links, type(original.field_links))


def test_list_strategies_response_roundtrip() -> None:
    original = ListStrategiesResponse200(
        strategies=[
            StrategySummary(
                strategy_id="6bsh31ikwkuivhtgcoa6s4",
                compiled_at=_dt.datetime(2026, 8, 19, 10, 15, 0, tzinfo=_dt.UTC),
                required_sources=["Ticker"],
            ),
            # requiredSources/compiledAt are both optional — a strategy the platform
            # could not introspect carries neither.
            StrategySummary(strategy_id="2ul144qe9tlwzu5anhwvc6"),
        ]
    )
    payload = original.to_dict()
    first, second = payload["strategies"]
    assert first["strategyId"] == "6bsh31ikwkuivhtgcoa6s4"
    assert first["compiledAt"].startswith("2026-08-19T10:15:00")
    assert first["requiredSources"] == ["Ticker"]
    assert "compiledAt" not in second
    assert "requiredSources" not in second

    parsed = ListStrategiesResponse200.from_dict(payload)
    assert len(parsed.strategies) == 2
    assert parsed.strategies[0].compiled_at == original.strategies[0].compiled_at
    assert isinstance(parsed.strategies[1].compiled_at, type(original.strategies[1].compiled_at))


def test_job_state_roundtrip_with_enum() -> None:
    # Pick whatever the first enum member is — names vary by spec
    # (New/Started/Completed/Aborted/Failed).
    a_status = next(iter(JobStateStatus))
    original = JobState(
        context_id="ctx_abc_123",
        status=a_status,
        size=100,
        completed=42,
    )
    payload = original.to_dict()
    assert payload["status"] == a_status.value
    parsed = JobState.from_dict(payload)
    assert parsed.context_id == "ctx_abc_123"
    assert parsed.status == a_status
    assert parsed.size == 100
    assert parsed.completed == 42


def test_equity_curve_result_roundtrip() -> None:
    original = EquityCurveResult(
        meta=EquityCurveMeta(
            input_point_count=3,
            output_point_count=2,
            resampled=True,
            differential=False,
            out_mode=EquityCurveOutMode.ARRAY,
        ),
        points=[EquityPoint(timestamp=1_700_000_000_000, equity=100.0)],
    )

    payload = original.to_dict()
    assert payload["meta"]["outMode"] == "ARRAY"
    assert payload["points"] == [{"timestamp": 1_700_000_000_000, "equity": 100.0}]

    parsed = EquityCurveResult.from_dict(payload)
    assert parsed.meta.output_point_count == 2
    assert not isinstance(parsed.points, types.Unset)
    assert parsed.points[0].equity == 100.0


def test_execute_backtest_params_roundtrip_and_result_echo() -> None:
    """The single-run params map supports every documented scalar type."""
    label: ScalarStrategyParamValue = "fast"
    request_params = ExecuteBacktestBodyParams()
    request_params.additional_properties = {
        "ema.fast.period": 9,
        "risk.pct": 0.5,
        "useTrendFilter": True,
        "strategy.label": label,
    }
    request = ExecuteBacktestBody(
        prepare_job_id="prepare-1",
        strategy_id="strategy-1",
        params=request_params,
    )

    request_payload = request.to_dict()
    assert request_payload["params"] == request_params.additional_properties
    parsed_request = ExecuteBacktestBody.from_dict(request_payload)
    assert not isinstance(parsed_request.params, types.Unset)
    assert parsed_request.params.to_dict() == request_params.additional_properties

    result_params = ResultMapParams.from_dict(request_params.to_dict())
    result = ResultMap(strategy_id="strategy-1", instrument="BTC/USDT", params=result_params)
    assert result.to_dict()["params"] == request_params.additional_properties
    parsed_result = ResultMap.from_dict(result.to_dict())
    assert not isinstance(parsed_result.params, types.Unset)
    assert parsed_result.params.to_dict() == request_params.additional_properties


def test_dataset_created_roundtrip_has_only_immediate_metadata() -> None:
    original = DatasetCreated(
        upload_id="upload-1",
        upload=DatasetUploadTarget(url="https://uploads.example/upload-1", expires_in_minutes=15),
        dataset_id="dataset-1",
        name="BTC ticks",
        type_=DatasetCreatedType.TICKER,
        instrument="BTC/USDT",
    )

    payload = original.to_dict()
    assert payload["datasetId"] == "dataset-1"
    assert "createdAt" not in payload
    assert "currentVersionId" not in payload

    parsed = DatasetCreated.from_dict(payload)
    assert parsed.instrument == "BTC/USDT"
    assert parsed.upload.url == "https://uploads.example/upload-1"


def test_dataset_data_location_roundtrip() -> None:
    """Ready datasets describe the stored bytes with a URL and exact format."""
    data_url = "https://storage.example/datasets/dsv-1.parquet?signature=example"
    version = DatasetVersion(
        dataset_id="dataset-1",
        data_url=data_url,
        data_format=DatasetVersionDataFormat.PARQUET,
    )
    version_payload = version.to_dict()
    assert version_payload["dataUrl"] == data_url
    assert version_payload["dataFormat"] == "parquet"
    parsed_version = DatasetVersion.from_dict(version_payload)
    assert parsed_version.data_url == data_url
    assert parsed_version.data_format is DatasetVersionDataFormat.PARQUET

    dataset = DatasetWithLinks(
        dataset_id="dataset-1",
        name="BTC ticks",
        type_=DatasetType.TICKER,
        instrument="BTC/USDT",
        created_at=_dt.datetime(2026, 9, 7, tzinfo=_dt.UTC),
        status=DatasetStatus.READY,
        data_url=data_url,
        data_format=DatasetWithLinksDataFormat.PARQUET,
        timestamp_unit=DatasetTimestampUnit.US,
        bytes_=4_831_022,
        rows=86_400,
    )
    dataset_payload = dataset.to_dict()
    assert dataset_payload["dataUrl"] == data_url
    assert dataset_payload["dataFormat"] == "parquet"
    parsed_dataset = DatasetWithLinks.from_dict(dataset_payload)
    assert parsed_dataset.data_url == data_url
    assert parsed_dataset.data_format is DatasetWithLinksDataFormat.PARQUET
    assert parsed_dataset.timestamp_unit is DatasetTimestampUnit.US
    assert parsed_dataset.bytes_ == 4_831_022
    assert parsed_dataset.rows == 86_400


def test_live_signal_page_roundtrip() -> None:
    signal = LiveSignal(
        v=1,
        signal_id="signal-1",
        run_id="run-1",
        stage=LiveSignalStage.LIVE,
        type_=LiveSignalType.HINT,
        event_ts_ms=1_700_000_000_000,
        emitted_at_ms=1_700_000_000_001,
        instrument=LiveSignalInstrument(symbol="BTC/USDT"),
        digest="digest-1",
    )
    page = LiveSignalPage(signals=[signal], available_since_ms=1_699_999_000_000)

    payload = page.to_dict()
    assert payload["signals"][0]["signalId"] == "signal-1"
    assert payload["availableSinceMs"] == 1_699_999_000_000

    parsed = LiveSignalPage.from_dict(payload)
    assert parsed.signals[0].instrument.symbol == "BTC/USDT"
    assert parsed.available_since_ms == 1_699_999_000_000
