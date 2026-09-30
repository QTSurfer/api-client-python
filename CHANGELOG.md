# Changelog

All notable changes to `qtsurfer-api-client` are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project's version tracks the OpenAPI spec version it was generated against rather than following independent SemVer.

## [Unreleased]

## [0.128.14] — 2026-09-30

### Added ✨

- `send_live_command` delivers an owner-only transient command to a running strategy and returns its command ID and effective market position. `202` means accepted; `503` guarantees it was not sent. Retries after an ambiguous network failure can create a second command because the endpoint has no idempotency key.
- Paper-trading configuration, account snapshots, and paginated equity history are available on live runs.
- Strategy and dataset listings can include deleted entries with `deleted_at`; account limits include `max_sweep_cartesian`, and live runs expose an optional stop/failure `reason`.

## [0.126.2] — 2026-09-23

- Add the generated `list_live` endpoint for the caller's own live runs.

## [0.126.1] — 2026-09-23

- Represent nullable live-signal fields correctly.

## [0.126.0] — 2026-09-23

Regenerated against OpenAPI spec `0.126.0` (from `0.115.1`).

### Added ✨

- Account and account-usage endpoints.
- Dataset source imports, dataset lifecycle metadata, and timestamp-unit metadata.
- Live Execution endpoints, including recorded-signal pagination. An expired signal cursor is
  parsed as a typed `410` response; restart from its `availableSinceMs` value.

### Changed 🔄

- Backtesting accepts `kline` sources where the API permits them, with cadence represented as a
  string rather than the removed `PrepareRequestCadence` enum.

## [0.115.1] — 2026-09-08

Regenerated against OpenAPI spec `0.115.1` (from `0.111.2`).

### Added ✨

- `ExecuteBacktestBody.params` accepts one scalar strategy-property vector for an execution, and
  `ResultMap.params` echoes that vector in the result. `ScalarStrategyParamValue` is re-exported
  as the corresponding public scalar alias.
- `DatasetWithLinks` and `DatasetVersion` expose `data_url` and `data_format` (`lastra` or
  `parquet`) once a dataset version is ready.

### Changed 🔄

- Dataset creation accepts CSV or parquet data, directly or inside a gzip/zip containing one file.
  `DatasetVersion.bytes` describes stored data rather than the original upload bytes.
- `ResultMap.win_rate` is a fraction from 0.0 to 1.0, and `cagr` is a ratio (for example, `0.15`
  represents 15%).

## [0.111.2] — 2026-08-28

Regenerated against OpenAPI spec `0.111.2` (from `0.110.3`).

### Added ✨

- `open_dataset_upload` — `POST /datasets/{datasetId}/uploads` — returns a `DatasetUploadSession` for the current open upload or the next dataset version. `DatasetUploadTarget` names the presigned upload target shape shared by this response and `DatasetCreated`.

### Changed 🔄

- `finalize_dataset_upload` now parses the documented `409` response when an upload session has already produced a version. Open a new upload session instead of reusing that `upload_id`.
- `DatasetCreated` now mirrors the immediate creation response: its upload session plus `dataset_id`, `name`, `type_`, and `instrument`. Version-derived metadata is obtained through `get_dataset` after its lifecycle stage has completed.

## [0.110.3] — 2026-08-27

Regenerated against OpenAPI spec `0.110.3` (from `0.110.1`).

### Added ✨

- `get_sweep_run_equity_curve` — `GET /backtest/{exchangeId}/{type}/executeSweep/{requestId}/{sweepId}/runs/{runIx}/equityCurve` — retrieves a retained trial curve as an `EquityCurveResult`. The optional `resample`, `differential`, and `out_mode` query parameters shape the response; read `meta` to determine the shape actually served.
- `EquityCurveOptions` configures an individual backtest's returned curve. `EquityCurveRequest` adds retention selection (`mode`, `n`, `max_pct`) for sweep trials. Both use `EquityCurveOutMode` to choose point objects (`ARRAY`) or parallel arrays (`SHORT`).
- `DeclaredProperty` is available as the typed `declared_properties` field on `CompileStrategyResponse200` for callers that invoke the currently unsupported `compileStrategy` operation through the underlying HTTP client.

### Changed 🔄

- `ResultMap.equity_curve` and `SweepRunRow.equity_curve` now use `EquityCurveResult`, which carries points or compact parallel arrays together with outcome metadata, rather than a bare point list.
- `ExecuteBacktestBody` and `ExecuteSweepRequest` gain optional `equity_curve` request fields.

## [0.110.1] — 2026-08-25

Regenerated against OpenAPI spec `0.110.1` (from `0.109.2`). Adds a new Dataset feature; everything
else below is additive.

### Added ✨

- New `api.dataset` module — upload your own CSV ticker data and backtest against it via the
  reserved `exchangeId: user` value on the existing `prepare_backtest`/`execute_backtest`
  endpoints. Six endpoints, generated under `qtsurfer.api.client._generated.api.dataset` and
  re-exported from `qtsurfer.api.client.api.dataset`:
  - `create_dataset` — `POST /datasets` — creates a dataset and its first upload session in one
    call, returning `DatasetCreated` (a `Dataset` plus `upload_id` and a presigned `upload.url` to
    `PUT` the CSV to directly — no API credentials involved in that `PUT`).
  - `list_datasets` — `GET /datasets` — every dataset you've created and not deleted, most
    recently created first. Returns `ListDatasetsResponse200` (`datasets: list[Dataset]`). Never
    `404`s — an empty list if you have none, same convention as `list_strategies`.
  - `get_dataset` — `GET /datasets/{datasetId}` — returns `DatasetWithLinks` (a `Dataset` plus a
    `_links.self` href).
  - `delete_dataset` — `DELETE /datasets/{datasetId}` — returns `DeleteDatasetResponse200`
    (`dataset_id`, `deleted: True`). Soft delete: the dataset stops being listed or preparable
    from, but a backtest already running against one of its versions is not disrupted.
  - `finalize_dataset_upload` — `POST /datasets/{datasetId}/uploads/{uploadId}/finalize` — call
    once the file has been `PUT` to `upload.url`; enqueues ingest and returns
    `FinalizeDatasetUploadResponse202` (`job_id`). Idempotent — a repeat finalize of the same
    upload returns the same `job_id` rather than enqueueing a second ingest.
  - `get_dataset_upload` — `GET /datasets/{datasetId}/uploads/{uploadId}` — poll after finalize
    until `status` (`DatasetUploadStateStatus`) is `ready` or `failed`; also reports `uploading`
    before you finalize. Returns `DatasetUploadState`, which on `ready` carries a `version:
    DatasetVersion` (`bytes`, `rows`, `cadence`, `timestamp_unit`, `gaps`, `largest_gap_steps`).
- `PrepareRequest` gains optional `dataset_id` / `dataset_version_id` — send `dataset_id` (from
  `create_dataset`) instead of `instrument` when `exchangeId` is the reserved `user`;
  `dataset_version_id` optionally pins a specific past version instead of the dataset's current
  one.
- `PrepareRequest.cadence` (`PrepareRequestCadence`) gains `3m`, `30m`, `2h`, `8h`, `12h`, `1w`,
  `1q` — widened from `1s | 5s | 1m | 5m | 15m | 1h | 4h | 1d` to fifteen values.
- `PrepareJobState` gains three optional fields, populated only for a dataset-backed prepare
  (`exchangeId: user`): `cadence` (the dataset version's own discovered cadence), `gaps`, and
  `largest_gap_steps` (both from the coverage walk at its own cadence, mirroring the managed-
  exchange `total_hours`/`hours_with_data`/`hours_without_data` triplet that stays absent in this
  case).

### Changed 🔄

- `PrepareRequest.instrument` moved from required to optional — required shrank from
  `[instrument, from, to]` to `[from, to]`, since `instrument` is meaningless against a
  dataset-backed prepare. No hand-written code in this repo constructs `PrepareRequest`
  positionally, but the generated dataclass's field order changed accordingly (`from_, to,
  instrument, dataset_id, dataset_version_id, cadence` instead of `instrument, from_, to,
  cadence`) — construct it with keyword arguments, as the README examples already do.

### Not changed

- `compile_strategy` (`POST /strategy`) remains absent — its `text/plain` request body is still
  unsupported by `openapi-python-client`. Unrelated to this spec bump; call it directly via the
  underlying `httpx` client (see the README).

## [0.109.2] — 2026-08-20

Regenerated against OpenAPI spec `0.109.2` (from `0.107.0`). Everything below is additive — no
request shape changes, nothing removed, nothing renamed.

### Added ✨

- `list_strategies` — `GET /strategies` — every strategy you have registered and not deleted, most
  recently compiled first. Returns `ListStrategiesResponse200`
  (`strategies: list[StrategySummary]`), each item carrying `strategy_id`
  and the same optional `compiled_at` / `required_sources` provenance `get_strategy` reports —
  deliberately *without* `validation`, so listing stays cheap no matter how many strategies you
  have. Check a specific strategy's validation with `get_strategy`. Never `404`s — an empty list
  means you have none registered. Generated under `qtsurfer.api.client._generated.api.strategy`
  and re-exported from `qtsurfer.api.client.api.strategy`.
- `delete_strategy` — `DELETE /strategy/{strategyId}` — removes a strategy from both `get_strategy`
  and `list_strategies`. Returns `DeleteStrategyResponse200` (`strategy_id`, `deleted: True`) on
  `200`, or `ResponseError` on `404` (no such registered strategy for this caller). Doesn't undo
  anything that already happened: backtests already run against the strategy are unaffected, and
  it only ever removes your own registration — deleting your copy of a shared/marketplace strategy
  never affects anyone else's copy. Re-submitting the same source to `compile_strategy` afterwards
  registers a brand-new strategy with a brand-new id; the deleted id does not come back.
- `get_strategy_code` — `GET /strategy/{strategyId}/code` — the exact source last submitted for a
  strategy id. Returns `GetStrategyCodeResponse200` (`strategy_id`, `code`) on `200`, or
  `ResponseError` on `404`. The `404` deliberately covers two indistinguishable cases: the id was
  never registered by this caller, or it resolves only through a shared/marketplace reference that
  carries no source of its own — both read as the same "nothing to return."
- `StrategyState` gains an optional `field_links` (`_links` on the wire), typed `StrategyLinks`
  (`code: HalLink`) pointing at `get_strategy_code` (`href` = `/v1/strategy/{strategyId}/code`).
  Present on a full `StrategyState` body — `get_strategy`'s response, and `validate_strategy`'s
  already-validated `200` — and absent from that same endpoint's `202`, a deliberately partial stub
  carrying only what is known before a check has even started. Following `code` can still `404`,
  for the same two reasons `get_strategy_code` documents.

### Not changed

- `compile_strategy` (`POST /strategy`) remains absent — its `text/plain` request body is still
  unsupported by `openapi-python-client`. Unrelated to this spec bump; call it directly via the
  underlying `httpx` client (see the README).
- The spec's `servers` block renamed its staging entry's host
  (`https://api.staging.qtsurfer.com` → `https://api.qtsurfer.net`) and reworded both server
  descriptions. This repo does not hardcode the old staging hostname anywhere, so no README or
  test changes were needed for it.

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
