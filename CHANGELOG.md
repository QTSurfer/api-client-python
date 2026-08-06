# Changelog

All notable changes to `qtsurfer-api-client` are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project's version tracks the OpenAPI spec version it was generated against rather than following independent SemVer.

## [Unreleased]

## [0.102.0] — 2026-08-06

### Changed 🔄

- `get_strategy` now returns `StrategyState` instead of the old job-status shape
  (`jobId`/`status: New|Started|Completed|Aborted|Failed`/`statusDetail`). `StrategyState` carries
  `strategy_id`, `validation` (`not_validated` / `pending` / `passed` / `failed`), `compiled_at`,
  `required_sources`, `validated_at`, `detail`, `notices`, `notices_truncated`, `dry_run_incomplete`,
  and `validation_stalled`.
- `ResultMap` (in `BacktestJobResult.results`) gains optional `notices` (`list[Notice]`) and
  `notices_truncated`.

### Added ✨

- `validate_strategy` — `POST /strategy/{strategyId}/validate` — generates cleanly (no request body,
  JSON in/out) and is re-exported from `qtsurfer.api.client.api.strategy` alongside `get_strategy`.
- `Notice` — the engine-diagnostic shape (`level`, `code`, `message`, `provenance`:
  `execute` / `compile-dry-run`) now carried by both `StrategyState.notices` and `ResultMap.notices`.

### Not changed

- `compile_strategy` (`POST /strategy`) remains absent — its `text/plain` request body is still
  unsupported by `openapi-python-client`. This was true before 0.102.0 and is unrelated to it; call
  it directly via the underlying `httpx` client (see the README).

## [0.99.2] — 2026-07-27

### Fixed 🐛

- `get_backtest_result` now reflects the spec's documented `202`: the execute-result endpoint
  answers with an empty body when a job is known but its result is not yet readable. The generated
  response type widens accordingly.

## [0.99.1] — 2026-07-18

### Changed 🔄

- Regenerated against OpenAPI spec `0.99.1`, which renames operation ids — no request/response
  shape, field, or endpoint changes. Generated function names follow the operation id 1:1, so every
  renamed operation gets a new function name.

## [0.98.0] — 2026-07-11

### Changed 🔄

- The single-instrument `get_prepare_status` now returns `PrepareJobState` (`JobState` plus
  `coverage_ratio`, `total_hours`, `hours_with_data`, and a per-hour `hours_without_data`
  breakdown), and `Partial` is removed from the job status enum. The 0.97.0 instruments HAL envelope
  and per-data-type coverage are unchanged.
