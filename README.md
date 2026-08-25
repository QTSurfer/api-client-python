<h1 align="center">QTSurfer API Client · Python</h1>

<p align="center">
  <a href="https://github.com/QTSurfer/api-client-python/actions/workflows/ci.yml"><img src="https://github.com/QTSurfer/api-client-python/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://pypi.org/project/qtsurfer-api-client/"><img src="https://img.shields.io/pypi/v/qtsurfer-api-client.svg" alt="PyPI"></a>
  <a href="https://pypi.org/project/qtsurfer-api-client/"><img src="https://img.shields.io/pypi/pyversions/qtsurfer-api-client.svg" alt="Python versions"></a>
  <a href="https://qtsurfer.github.io/api-client-python/"><img src="https://img.shields.io/badge/docs-pdoc-blue" alt="pdoc"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License"></a>
</p>

<p align="center">
  Auto-generated Python client for the <a href="https://github.com/QTSurfer/qtsurfer-api">QTSurfer API</a>, built from the OpenAPI 3.1 spec with <a href="https://github.com/openapi-generators/openapi-python-client">openapi-python-client</a> on top of <a href="https://www.python-httpx.org/">httpx</a>.
</p>

<p align="center">
  <code>pip install qtsurfer-api-client</code>
</p>

---

Intentionally thin: one function per endpoint, 1:1 with the spec. For workflow orchestration (polling, retries, domain objects, unified errors), use [`qtsurfer-sdk`](https://github.com/QTSurfer/sdk-python) (coming soon).

- **Sync-first, httpx-powered** — same call site shape as the Java/TS siblings.
- **Spec-driven** — generated sources fetched from [`QTSurfer/qtsurfer-api`](https://github.com/QTSurfer/qtsurfer-api) by `scripts/regenerate.sh`.
- **Fully typed** — `py.typed` marker, `mypy --strict` clean (consumers see precise types for every request/response).
- **Python 3.11+** — modern type hints, no compat shims.

## Installation

```bash
pip install qtsurfer-api-client
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add qtsurfer-api-client
```

## Quick start

```python
import os

from qtsurfer.api.client import AuthenticatedClient
from qtsurfer.api.client.api.exchange import list_exchanges, list_instruments

client = AuthenticatedClient(
    base_url="https://api.qtsurfer.com/v1",
    token=os.environ["QTSURFER_TOKEN"],
)

exchanges = list_exchanges.sync(client=client)
for ex in exchanges or []:
    print(ex.id, ex.name)

instruments = list_instruments.sync(client=client, exchange_id="binance")
print(f"{len(instruments.data)} instruments on binance ({instruments.meta.segment.value})")
```

### API key → JWT

Every endpoint above expects a short-lived JWT in the `Authorization: Bearer …`
header. Exchange a long-lived API key for one via `authenticate`:

```python
import os

from qtsurfer.api.client import AuthenticatedClient
from qtsurfer.api.client.api.auth import authenticate

# AuthenticatedClient also drives the apikey header — set prefix="" so it
# sends `X-API-Key: <key>` instead of `Authorization: Bearer <key>`.
apikey_client = AuthenticatedClient(
    base_url="https://api.qtsurfer.com/v1",
    token=os.environ["QTSURFER_APIKEY"],
    prefix="",
    auth_header_name="X-API-Key",
)

token_response = authenticate.sync(client=apikey_client)
jwt = token_response.access_token  # use this in subsequent calls
```

For production use, prefer the [`qtsurfer-sdk`](https://github.com/QTSurfer/sdk-python)
`auth(apikey)` helper — it handles token refresh, env-var pickup
(`QTSURFER_APIKEY`), and pluggable token storage so callers don't reinvent any
of it on top of the raw client.

Each generated endpoint module exposes four entrypoints:

| Function | Returns |
| --- | --- |
| `sync(...)` | parsed model (or `None` on a defined error response) |
| `sync_detailed(...)` | full `Response[...]` (status, headers, parsed, content) |
| `asyncio(...)` | parsed model, awaitable |
| `asyncio_detailed(...)` | full `Response[...]`, awaitable |

## API surface

| Module | Operation | Method · Path |
| --- | --- | --- |
| `api.auth` | `authenticate` | `POST /auth/token` — exchange API key for a short-lived JWT |
| `api.exchange` | `list_exchanges` | `GET /exchanges` |
| `api.exchange` | `list_instruments` | `GET /exchange/{exchangeId}/instruments` (default `spot` segment) |
| `api.exchange` | `list_segment_instruments` | `GET /exchange/{exchangeId}/{segment}/instruments` |
| `api.exchange` | `download_tickers` | `GET /exchange/{exchangeId}/tickers/{base}/{quote}` |
| `api.exchange` | `download_klines` | `GET /exchange/{exchangeId}/klines/{base}/{quote}` |
| `api.strategy` | `get_strategy` | `GET /strategy/{strategyId}` |
| `api.strategy` | `list_strategies` | `GET /strategies` |
| `api.strategy` | `delete_strategy` | `DELETE /strategy/{strategyId}` |
| `api.strategy` | `get_strategy_code` | `GET /strategy/{strategyId}/code` |
| `api.strategy` | `validate_strategy` | `POST /strategy/{strategyId}/validate` |
| `api.backtesting` | `prepare_backtest` | `POST /backtest/{exchangeId}/{type}/prepare` |
| `api.backtesting` | `get_prepare_status` | `GET /backtest/{exchangeId}/{type}/prepare/{jobId}` |
| `api.backtesting` | `execute_backtest` | `POST /backtest/{exchangeId}/{type}/execute` |
| `api.backtesting` | `cancel_backtest` | `DELETE /backtest/{exchangeId}/{type}/execute/{jobId}` |
| `api.backtesting` | `get_backtest_result` | `GET /backtest/{exchangeId}/{type}/execute/{jobId}` |
| `api.backtesting` | `execute_sweep` | `POST /backtest/{exchangeId}/{type}/executeSweep/{requestId}` |
| `api.backtesting` | `get_sweep_result` | `GET /backtest/{exchangeId}/{type}/executeSweep/{requestId}/{sweepId}` |
| `api.backtesting` | `cancel_sweep` | `DELETE /backtest/{exchangeId}/{type}/executeSweep/{requestId}/{sweepId}` |
| `api.backtesting` | `get_sweep_sensitivity` | `GET /backtest/{exchangeId}/{type}/executeSweep/{requestId}/{sweepId}/sensitivity` |
| `api.dataset` | `create_dataset` | `POST /datasets` — create a dataset and get a presigned upload URL |
| `api.dataset` | `list_datasets` | `GET /datasets` |
| `api.dataset` | `get_dataset` | `GET /datasets/{datasetId}` |
| `api.dataset` | `delete_dataset` | `DELETE /datasets/{datasetId}` |
| `api.dataset` | `finalize_dataset_upload` | `POST /datasets/{datasetId}/uploads/{uploadId}/finalize` |
| `api.dataset` | `get_dataset_upload` | `GET /datasets/{datasetId}/uploads/{uploadId}` |

Twenty-six of the spec's twenty-seven operations, all reachable through `qtsurfer.api.client.api`
as listed. The exception is `compileStrategy` (`POST /strategy`), whose `text/plain` request body
openapi-python-client does not support, so no module is generated for it — call it through the
underlying `httpx` client.

### Datasets — backtest against your own data

Upload CSV ticker data and prepare/execute a backtest against it via the reserved
`exchangeId: user` value on the existing `prepare_backtest`/`execute_backtest` endpoints:
`create_dataset` returns a `datasetId` plus a presigned URL to `PUT` the CSV to directly, then
`finalize_dataset_upload` kicks off ingest and `get_dataset_upload` polls until `status` is
`ready` or `failed`. `PrepareRequest.instrument` is optional for this reason — pass `dataset_id`
(and optionally `dataset_version_id` to pin a specific past version) instead when the exchange is
`user`. `list_datasets`/`get_dataset` never `404` for "none yet", same convention as
`list_strategies`; `delete_dataset` is a soft delete that doesn't disrupt a backtest already
running against one of the dataset's versions.

> Exact module/function names are produced from `operationId` in the OpenAPI spec. Run `scripts/regenerate.sh` to refresh and check `src/qtsurfer/api/client/_generated/api/` for the authoritative listing.

All generated model types (`Exchange`, `InstrumentDetail`, `InstrumentCoverage`, `CoverageWindow`, `JobState`, `PrepareJobState`, `StrategyState`, `StrategyLinks`, `BacktestJobResult`, `ResultMap`, `ResponseError`, `Dataset`, `DatasetWithLinks`, `DatasetCreated`, `DatasetVersion`, `DatasetUploadState`, …) live under `qtsurfer.api.client.models`. `list_instruments`/`list_segment_instruments` return an `InstrumentListResponse` (HAL envelope: `data` + `meta` + `_links`), not a bare list — each `InstrumentDetail.coverage` carries per-data-type `CoverageWindow`s instead of flat `dataFrom`/`dataTo`. A single-instrument `get_prepare_status` returns a `PrepareJobState` — always terminal (`status: Completed`), with a `coverage_ratio` and a per-hour `hours_without_data` breakdown to act on instead of polling. Against a dataset-backed prepare (`exchangeId: user`), `PrepareJobState` reports coverage on the dataset's own cadence grid instead — `cadence`/`gaps`/`largest_gap_steps` — with `total_hours`/`hours_with_data`/`hours_without_data` absent in that case. `get_strategy` returns a `StrategyState`, whose `validation` field (`not_validated` / `pending` / `passed` / `failed`) reports the outcome of the most recent `validate_strategy` check rather than a compile job status.

A full `StrategyState` (from `get_strategy`, and from `validate_strategy`'s already-validated `200`) carries an optional `field_links` (`_links` on the wire) — a `StrategyLinks` with a `code: HalLink` pointing at `get_strategy_code`. `validate_strategy`'s `202` omits it, since a check that just started has nothing to link to yet. `list_strategies` returns every strategy you've registered and not deleted, most recently compiled first, but deliberately without each one's `validation` state — check that per strategy with `get_strategy`. `delete_strategy` removes a strategy from both `get_strategy` and `list_strategies`; it doesn't touch backtests already run against it, and re-submitting the same source afterwards registers a new strategy under a new id. `get_strategy_code`'s `404` covers two indistinguishable cases: an id never registered by you, or one that resolves only through a shared/marketplace reference with no source of its own.

> **`POST /strategy` (`compileStrategy`)** is currently omitted by the generator because the spec declares its request body as `text/plain` and `openapi-python-client` only emits JSON / form / multipart bodies. Call it directly via the underlying `httpx` client (`client.get_httpx_client().post("/strategy", content=src, headers={"Content-Type": "text/plain"})`) until the spec is restructured. The other `api.strategy` operations have no such restriction and generate normally.

### Binary downloads (`/exchange/{ex}/tickers|klines/{base}/{quote}`)

These endpoints return raw [Lastra](https://github.com/QTSurfer/lastra-java) bytes (default) or Parquet (`format=parquet`). The generated `sync()` helpers parse the response body as JSON and will raise on binary payloads; use `sync_detailed()` and read `response.content` directly:

```python
from qtsurfer.api.client import AuthenticatedClient
from qtsurfer.api.client.api.exchange import download_tickers

client = AuthenticatedClient(base_url="https://api.qtsurfer.com/v1", token=token)

response = download_tickers.sync_detailed(
    client=client,
    exchange_id="binance",
    base="BTC",
    quote="USDT",
    hour="2026-01-15T10",
)
with open("BTC_USDT_2026-01-15_h10.lastra", "wb") as f:
    f.write(response.content)
```

For very large segments, drop down to the underlying `httpx.Client` (`client.get_httpx_client()`) and stream:

```python
with client.get_httpx_client().stream(
    "GET",
    "/exchange/binance/klines/BTC/USDT",
    params={"hour": "2026-01-15T10", "format": "parquet"},
) as r:
    r.raise_for_status()
    with open("out.parquet", "wb") as f:
        for chunk in r.iter_bytes():
            f.write(chunk)
```

## Configuring the client

Both `Client` and `AuthenticatedClient` accept the standard hooks of the upstream generator:

```python
from qtsurfer.api.client import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://api.qtsurfer.com/v1",
    token=token,
    timeout=httpx.Timeout(30.0),
    verify_ssl=True,
    headers={"X-Request-Id": "..."},
    raise_on_unexpected_status=True,
)
```

Need per-call customisation (e.g. swap the underlying `httpx.Client` for one with a custom transport)? Use `client.with_httpx_client(my_httpx_client)` or `client.set_httpx_client(...)`.

## Regenerating the client

The `src/qtsurfer/api/client/_generated/` directory is a committed build artifact produced from the OpenAPI spec hosted at [`QTSurfer/qtsurfer-api`](https://github.com/QTSurfer/qtsurfer-api/blob/main/openapi.yaml). Never hand-edit it.

```bash
uv sync                    # install pinned dev deps
./scripts/regenerate.sh    # fetch spec + regenerate + sync pyproject version
uv run ruff check src/ tests/
uv run mypy src/
uv run pytest -v
```

Generator configuration lives in `codegen.config.yaml`. The spec URL is hard-coded in `scripts/regenerate.sh`; point it at a tag/commit for fully reproducible builds.

## Development

| Command | Description |
| ------ | ----------- |
| `uv sync` | Install dependencies from `uv.lock` |
| `./scripts/regenerate.sh` | Re-fetch spec + regenerate client |
| `uv run ruff check src/ tests/` | Lint |
| `uv run ruff format src/ tests/` | Format |
| `uv run mypy src/` | Type-check (`--strict`) |
| `uv run pytest -v` | Run tests |
| `uv run python -m build` | Build wheel + sdist into `dist/` |

## Versioning

`pyproject.toml`'s `version` field is kept in lockstep with the `info.version` of the OpenAPI spec by `scripts/regenerate.sh`. Tags pushed to `main` (`vX.Y.Z`) trigger the PyPI publish workflow via OIDC trusted publishing.

## License

Apache-2.0 — see [LICENSE](./LICENSE).
