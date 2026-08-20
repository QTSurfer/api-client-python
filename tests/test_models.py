"""Round-trip a few representative attrs-generated models through their
``to_dict`` / ``from_dict`` plumbing — proves the codec is wired and that
optional/datetime fields survive serialization."""

from __future__ import annotations

import datetime as _dt

from qtsurfer.api.client.models import (
    CoverageWindow,
    Exchange,
    HalLink,
    InstrumentCoverage,
    InstrumentDetail,
    JobState,
    JobStateStatus,
    ListStrategiesResponse200,
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
