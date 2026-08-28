"""Smoke tests — assert the package imports and the expected public surface exists.

These are guard rails for regenerate.sh: if a future spec change drops an
endpoint silently, these tests fail loudly.
"""

from __future__ import annotations

import importlib
import pkgutil
import re
from pathlib import Path

import pytest

import qtsurfer.api.client as qac
from qtsurfer.api.client import AuthenticatedClient, Client

GENERATED_API = "qtsurfer.api.client._generated.api"
PUBLIC_API = "qtsurfer.api.client.api"

#: Operations declared by the OpenAPI spec this package is generated from.
#: Every one of them must be accounted for below, either as a generated module
#: or as a documented exception.
SPEC_OPERATION_COUNT = 29

#: Each spec ``operationId`` the generator turns into an endpoint module, mapped
#: to the ``(tag package, module name)`` it lands under.
#:
#: This literal is hand-maintained **on purpose**. It cannot be derived from the
#: spec at test time: ``openapi.yaml`` is fetched by ``scripts/regenerate.sh``
#: and deliberately not committed, so it is absent both in a fresh checkout and
#: in the CI job that runs these tests. Deriving it from the installed package
#: instead would be tautological — it would assert that whatever the generator
#: produced is whatever the generator produced, and a silently dropped endpoint
#: would still pass, which is precisely the failure this test exists to catch.
#:
#: So the literal states the intent and the assertions compare it against the
#: package in *both* directions: a listed module that disappears fails, and an
#: unlisted module that appears fails too. The second half is what forces this
#: table to be updated deliberately instead of drifting.
#:
#: Module names are transcribed from the real contents of
#: ``src/qtsurfer/api/client/_generated/api/`` — not derived from the
#: operationIds by a camelCase-to-snake_case rule.
SPEC_ENDPOINTS: dict[str, tuple[str, str]] = {
    "authenticate": ("auth", "authenticate"),
    "listExchanges": ("exchange", "list_exchanges"),
    "listInstruments": ("exchange", "list_instruments"),
    "listSegmentInstruments": ("exchange", "list_segment_instruments"),
    "downloadTickers": ("exchange", "download_tickers"),
    "downloadKlines": ("exchange", "download_klines"),
    "validateStrategy": ("strategy", "validate_strategy"),
    "getStrategy": ("strategy", "get_strategy"),
    "listStrategies": ("strategy", "list_strategies"),
    "deleteStrategy": ("strategy", "delete_strategy"),
    "getStrategyCode": ("strategy", "get_strategy_code"),
    "prepareBacktest": ("backtesting", "prepare_backtest"),
    "getPrepareStatus": ("backtesting", "get_prepare_status"),
    "executeSweep": ("backtesting", "execute_sweep"),
    "getSweepResult": ("backtesting", "get_sweep_result"),
    "cancelSweep": ("backtesting", "cancel_sweep"),
    "getSweepSensitivity": ("backtesting", "get_sweep_sensitivity"),
    "getSweepRunEquityCurve": ("backtesting", "get_sweep_run_equity_curve"),
    "executeBacktest": ("backtesting", "execute_backtest"),
    "cancelBacktest": ("backtesting", "cancel_backtest"),
    "getBacktestResult": ("backtesting", "get_backtest_result"),
    "createDataset": ("dataset", "create_dataset"),
    "listDatasets": ("dataset", "list_datasets"),
    "getDataset": ("dataset", "get_dataset"),
    "deleteDataset": ("dataset", "delete_dataset"),
    "finalizeDatasetUpload": ("dataset", "finalize_dataset_upload"),
    "getDatasetUpload": ("dataset", "get_dataset_upload"),
    "openDatasetUpload": ("dataset", "open_dataset_upload"),
}

#: Spec operations that deliberately have **no** generated module, and why.
#: Naming them is the point: an assertion that accepts 20 modules against 21
#: operations because someone typed 20 documents nothing and would swallow a
#: second disappearance. Recording the exception explicitly keeps the shortfall
#: legible and keeps every *other* operation mandatory.
GENERATOR_UNSUPPORTED: dict[str, str] = {
    "compileStrategy": (
        "POST /strategy declares a text/plain request body, which "
        "openapi-python-client does not support. Call it through the "
        "underlying httpx client until the spec is restructured."
    ),
}

#: Endpoint modules that exist in the generated tree but are **not** re-exported
#: through the public ``qtsurfer.api.client.api`` package, which this package's
#: own docstring advertises as the endpoint surface. Such a module is reachable
#: only via the private ``_generated`` tree, so it is not reachable the
#: documented way.
#:
#: **Empty, and meant to stay that way.** It last held five modules —
#: ``list_segment_instruments`` and the four sweep endpoints — which the shim had
#: never picked up, so the README documented an import that raised. Kept as an
#: explicit empty set rather than deleted, because it is checked in both
#: directions: a module dropping out of the shim fails here, and re-opening the
#: gap means writing a name into this set, which is a visible decision rather
#: than a silent omission.
SHIM_NOT_REEXPORTED: frozenset[str] = frozenset()

#: The four entry points every generated endpoint module exposes.
ENTRY_POINTS = ("sync", "sync_detailed", "asyncio", "asyncio_detailed")

_SPEC_PATH = Path(__file__).resolve().parents[1] / "openapi.yaml"


def _submodules(package_name: str, *, packages: bool) -> set[str]:
    """Names of the sub-packages (``packages=True``) or modules under ``package_name``."""
    package = importlib.import_module(package_name)
    search_path: list[str] = list(getattr(package, "__path__", []))
    return {name for _, name, is_package in pkgutil.iter_modules(search_path) if is_package is packages}


def _generated_endpoint_modules() -> set[str]:
    """Every ``"<tag>/<module>"`` endpoint the generator actually emitted."""
    return {
        f"{tag}/{module}"
        for tag in _submodules(GENERATED_API, packages=True)
        for module in _submodules(f"{GENERATED_API}.{tag}", packages=False)
    }


def test_version_string() -> None:
    assert isinstance(qac.__version__, str)
    assert qac.__version__ != "0.0.0+unknown", "package metadata missing; install editable first"


def test_public_classes_exist() -> None:
    assert callable(Client)
    assert callable(AuthenticatedClient)


def test_authenticated_client_instantiates() -> None:
    client = AuthenticatedClient(base_url="https://api.qtsurfer.com/v1", token="fake-token")
    assert client.token == "fake-token"
    assert client._base_url == "https://api.qtsurfer.com/v1"


def test_unauthenticated_client_instantiates() -> None:
    client = Client(base_url="https://api.qtsurfer.com/v1")
    assert client._base_url == "https://api.qtsurfer.com/v1"


def test_known_endpoints_are_present() -> None:
    """Every spec operation the generator supports must resolve to a working module.

    Update ``SPEC_ENDPOINTS`` deliberately whenever the spec changes — and note
    that leaving it alone is not an option: an endpoint appearing without a row
    here fails just as loudly as one disappearing.
    """
    expected = {f"{tag}/{module}" for tag, module in SPEC_ENDPOINTS.values()}
    actual = _generated_endpoint_modules()

    assert actual == expected, (
        "generated endpoint modules drifted from SPEC_ENDPOINTS — "
        f"missing={sorted(expected - actual)}, unlisted={sorted(actual - expected)}"
    )

    for tag, module in SPEC_ENDPOINTS.values():
        endpoint = importlib.import_module(f"{GENERATED_API}.{tag}.{module}")
        for entry_point in ENTRY_POINTS:
            assert callable(getattr(endpoint, entry_point, None)), f"{tag}/{module} is missing {entry_point}()"


def test_every_spec_operation_is_accounted_for() -> None:
    """Every ungenerated spec operation has a named, current reason.

    A bare count would pass for any reason at all. This pins the shortfall to a
    named operation with a stated cause, so a *second* operation going missing
    still fails, and so the exception cannot outlive the limitation that
    justifies it: if the generator grows support (or the spec restructures the
    body), the operation shows up as unlisted and this has to be revisited.
    """
    assert len(SPEC_ENDPOINTS) + len(GENERATOR_UNSUPPORTED) == SPEC_OPERATION_COUNT, (
        f"spec declares {SPEC_OPERATION_COUNT} operations but the tables account for "
        f"{len(SPEC_ENDPOINTS)} generated + {len(GENERATOR_UNSUPPORTED)} ungenerated"
    )

    generated = _generated_endpoint_modules()
    for operation_id, reason in GENERATOR_UNSUPPORTED.items():
        assert operation_id not in SPEC_ENDPOINTS, f"{operation_id} is listed as both generated and ungenerated"
        assert reason.strip(), f"{operation_id} must document why it is absent"

        module = re.sub(r"(?<!^)(?=[A-Z])", "_", operation_id).lower()
        clashes = {entry for entry in generated if entry.endswith(f"/{module}")}
        assert not clashes, (
            f"{operation_id} now generates {sorted(clashes)}; move it from GENERATOR_UNSUPPORTED into SPEC_ENDPOINTS"
        )


def test_public_api_package_reexports_generated_endpoints() -> None:
    """``qtsurfer.api.client.api`` is the documented endpoint surface — hold it to the same list.

    The package docstring points users at ``qtsurfer.api.client.api``, so an
    endpoint reachable only under ``_generated`` is not reachable the documented
    way. ``SHIM_NOT_REEXPORTED`` records the modules currently in that state;
    every other generated endpoint must be re-exported.
    """
    known_modules = {module for _, module in SPEC_ENDPOINTS.values()}
    assert known_modules >= SHIM_NOT_REEXPORTED, (
        f"SHIM_NOT_REEXPORTED names modules that do not exist: {sorted(SHIM_NOT_REEXPORTED - known_modules)}"
    )

    public = importlib.import_module(PUBLIC_API)
    assert set(getattr(public, "__all__", [])) == _submodules(GENERATED_API, packages=True)

    expected_per_tag: dict[str, set[str]] = {}
    for tag, module in SPEC_ENDPOINTS.values():
        expected_per_tag.setdefault(tag, set())
        if module not in SHIM_NOT_REEXPORTED:
            expected_per_tag[tag].add(module)

    for tag, modules in expected_per_tag.items():
        shim = importlib.import_module(f"{PUBLIC_API}.{tag}")
        exported: set[str] = set(getattr(shim, "__all__", []))
        assert exported == modules, (
            f"{PUBLIC_API}.{tag} re-exports {sorted(exported)}, expected {sorted(modules)} — "
            "update the shim and shrink SHIM_NOT_REEXPORTED accordingly"
        )
        for module in exported:
            assert getattr(shim, module) is importlib.import_module(f"{GENERATED_API}.{tag}.{module}")


def test_spec_operation_ids_match_the_tables() -> None:
    """Cross-check the tables against the spec itself.

    This catches the one drift the package-side checks structurally cannot see:
    a new spec operation that produces **no module at all**. Nothing appears, so
    no set-comparison against the generated tree notices, and the counts still
    agree — which is exactly how ``compileStrategy`` stayed invisible.

    ``openapi.yaml`` is not committed; ``scripts/regenerate.sh`` fetches it, and
    the CI ``test`` job fetches it too, so this runs there rather than skipping.
    It skips only in a checkout where nobody has fetched the spec — the
    package-side assertions above still run in that case, but this particular
    gap is open until someone does.
    """
    if not _SPEC_PATH.is_file():
        pytest.skip(f"{_SPEC_PATH.name} absent (fetched by scripts/regenerate.sh); package-side checks still ran")

    spec_operations = set(
        re.findall(r"^\s*operationId:\s*(\S+)\s*$", _SPEC_PATH.read_text(encoding="utf-8"), flags=re.MULTILINE)
    )
    accounted = set(SPEC_ENDPOINTS) | set(GENERATOR_UNSUPPORTED)

    assert spec_operations == accounted, (
        "spec operations drifted from the tables — "
        f"unaccounted={sorted(spec_operations - accounted)}, stale={sorted(accounted - spec_operations)}"
    )
    assert len(spec_operations) == SPEC_OPERATION_COUNT, (
        f"spec now declares {len(spec_operations)} operations; SPEC_OPERATION_COUNT says {SPEC_OPERATION_COUNT}"
    )


def test_models_re_export() -> None:
    from qtsurfer.api.client.models import (
        AuthTokenError,
        AuthTokenResponse,
        BacktestJobResult,
        Exchange,
        InstrumentDetail,
        JobState,
        ResponseError,
        ResultMap,
    )

    assert Exchange is not None
    assert InstrumentDetail is not None
    assert JobState is not None
    assert BacktestJobResult is not None
    assert ResultMap is not None
    assert ResponseError is not None
    assert AuthTokenResponse is not None
    assert AuthTokenError is not None
