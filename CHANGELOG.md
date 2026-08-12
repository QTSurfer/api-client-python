# Changelog

All notable changes to `qtsurfer-api-client` are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project's version tracks the OpenAPI spec version it was generated against rather than following independent SemVer.

## [Unreleased]

## [0.107.0] — 2026-08-12

Regenerated against OpenAPI spec `0.107.0`. This client's version tracks the spec version it was
generated against. Both changes are additive at the wire level — no request shape changes, and no
endpoint was added or removed.

### Added ✨

- `ExecuteSweepResult` gains an optional `fail_reason` (`failReason` on the wire) — the cause
  reported by the **first** shard to fail. The backend already emitted it and the client dropped it
  silently, because the field was never declared; it now survives into the model. This is what turns
  a sweep that came back `status=ExecuteSweepResultStatus.PARTIAL` with `progress.done` at 0 into an
  answer instead of a shrug: the usual reason nothing finished is that the strategy could not be
  loaded at all, and that sentence was previously thrown away. First failure wins and later ones are
  not recorded, so on a sweep where several shards failed for different reasons this names one of
  them rather than all — read it alongside `progress.failed_shards`, not as a count. `UNSET` when no
  shard reported a cause, the normal case for a healthy sweep. Reaches callers through
  `get_sweep_result`, which returns `ExecuteSweepResult`.

### Changed 🔄

- `validate_strategy`'s `202` now deserializes into `StrategyState`, the same type as its `200`. The
  spec previously declared that response as an anonymous inline schema, from which the generator
  minted a `ValidateStrategyResponse202` model of its own; that model and its
  `ValidateStrategyResponse202Validation` enum are gone, and the union returned by all four entry
  points narrows from `ResponseError | StrategyState | ValidateStrategyResponse202` to
  `ResponseError | StrategyState`.

  **The consequence for callers: the status code, not the body, is now what tells the two responses
  apart.** `sync`/`asyncio` hand back a `StrategyState` either way and the return type keeps no trace
  of which arrived — a caller that needs to know must use `sync_detailed`/`asyncio_detailed` and read
  `.status_code`. A `200` means a verdict already existed and came straight back; a `202` means this
  call queued a check, so poll `get_strategy` until `validation` leaves `pending`. Note that
  `validation: pending` on its own does not imply `202` — a `200` can carry it too, left by a check an
  earlier call queued. The hand-written `qtsurfer.api.client.api.strategy` shim now documents this.

### Removed 🗑️

- `ValidateStrategyResponse202` and `ValidateStrategyResponse202Validation` are no longer exported
  from `qtsurfer.api.client.models` (see "Changed" above). Code that imported either — realistically
  only an `isinstance` check narrowing the old three-way union — should switch to `StrategyState`.

### Fixed 🐛

- **Five endpoints were unreachable through `qtsurfer.api.client.api`**, the package the module
  docstring points at as the endpoint surface: `list_segment_instruments`, `execute_sweep`,
  `get_sweep_result`, `cancel_sweep` and `get_sweep_sensitivity` existed in the generated tree but
  were never re-exported, so importing them the documented way raised `ImportError` — and the README
  listed `api.exchange.list_segment_instruments` as if it worked. All five are now re-exported.
  Anything already reaching into `qtsurfer.api.client._generated` for them keeps working; the point
  is that it should no longer be necessary.

### Not changed

- `compile_strategy` (`POST /strategy`) remains absent — its `text/plain` request body is still
  unsupported by `openapi-python-client`. Unrelated to this spec bump; call it directly via the
  underlying `httpx` client (see the README).

## [0.106.0] — 2026-08-12

This client's version tracks the OpenAPI spec version it was generated against. The previous
release tracked spec `0.102.0`; this entry covers the combined delta through `0.106.0` — sweep
walk-forward validation — landing all at once. No intermediate spec version was separately
published for this client.

### Added ✨

- `get_sweep_sensitivity` — `GET
  /backtest/{exchangeId}/{type}/executeSweep/{requestId}/{sweepId}/sensitivity` — aggregates a
  sweep's stored rows into per-axis **marginals** (`SweepMarginal`, best/mean/worst per value,
  collapsing every other axis) and per-axis-pair **heatmaps** (`SweepHeatmap`), answering which
  parameters actually moved the objective rather than just which point won. Returns
  `SweepSensitivity` (200) or `ResponseError` (404). Works on a sweep still in flight — the
  aggregates then describe only the runs finished so far. Generated under
  `qtsurfer.api.client._generated.api.backtesting`, alongside its sibling sweep endpoints. Like
  every sweep function, it is not wrapped by the hand-written `qtsurfer.api.client.api` shim (only
  `auth`/`backtesting`/`exchange`/`strategy` are re-exported there, and none of the sweep functions
  are among them); call it directly as
  `qtsurfer.api.client._generated.api.backtesting.get_sweep_sensitivity`. Its `SweepSensitivity` /
  `SweepMarginal` / `SweepHeatmap` model classes *are* available from `qtsurfer.api.client.models`,
  same as every other model, via that package's wildcard re-export.
- `executeSweep` accepts an optional `walkForward: WalkForwardRequest` (`folds`, `inSamplePct`) to
  run the sweep as walk-forward validation instead of a flat grid search. `ExecuteSweepAccepted`
  gains a matching optional `walkForward: WalkForwardAccepted` (`folds`, `inSamplePct`,
  `totalRuns`), present as soon as the sweep is accepted — safe to branch on before polling for
  results.
- `getSweepResult`'s `ExecuteSweepResult` gains an optional `walkForward: WalkForwardResult`
  (`folds`, `inSamplePct`, `completedFolds`, `paramDrift`, `results: WalkForwardFold[]`) once the
  sweep was submitted with `walkForward`. Its leaderboard is one row per completed fold — that
  fold's winner scored out-of-sample, with `runIx` carrying the fold index rather than a grid
  position. `ranking` is always `raw` and no plateau/DSR/PBO figure is attached to a walk-forward
  result, since layering a certification computed over the fold count on top of an already
  out-of-sample score would overstate what was measured.
- `ExecuteSweepResult` gains `ranking` (which ordering was actually applied — not always the one
  requested; see "Changed" below), and optional `pbo` / `pboSplits` (probability of backtest
  overfitting for the sweep as a whole, by combinatorially symmetric cross-validation, and the
  number of train/test splits it was averaged over).
- `SweepRunRow` gains optional `plateauScore`, `neighbourCount`, and `deflatedSharpe`, populated
  when plateau ranking applied to that row.

### Changed 🔄

- `getSweepResult` gains an optional `ranking` query param (`plateau` | `raw`), generated as
  `GetSweepResultRanking` and **defaulting client-side to `PLATEAU`** — calling `get_sweep_result`
  without passing `ranking=` now requests the plateau-ranked view, not the sweep's previous implicit
  raw-objective order. A plateau score is the objective of the worst run in a parameter point's
  neighbourhood, so a point ranks well only if the region around it also does; the raw top score is
  often a spike that does not survive nearby parameters. Pass `ranking=GetSweepResultRanking.RAW`
  for the old unadjusted-objective order. Sweeps submitted before plateau ranking existed have no
  stored parameter grid to rebuild a neighbourhood from and are always ranked raw regardless of the
  request — the response's own `ranking` field says which ordering was actually used, and is the
  only way to know for certain.
- `SweepProgress` gains three new **required** fields — `failedShards` (units that failed and will
  not be retried), `retrying` (units queued for another attempt after a transient failure — not
  counted as failed), `notStarted` (units with nothing reported yet) — plus optional
  `stalledSeconds` and `etaSeconds`. Any code constructing a `SweepProgress` by hand (rather than via
  `from_dict`) needs to supply the three new required arguments.

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
