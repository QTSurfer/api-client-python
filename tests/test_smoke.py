"""Smoke tests — assert the package imports and the expected public surface exists.

These are guard rails for regenerate.sh: if a future spec change drops an
endpoint silently, these tests fail loudly.
"""

from __future__ import annotations

import qtsurfer.api.client as qac
from qtsurfer.api.client import AuthenticatedClient, Client


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
    """Every operationId in the OpenAPI spec we currently support must resolve.

    Update this list deliberately whenever the spec changes.
    """
    from qtsurfer.api.client.api.auth import authenticate
    from qtsurfer.api.client.api.backtesting import (
        cancel_backtest,
        execute_backtest,
        get_backtest_result,
        get_prepare_status,
        prepare_backtest,
    )
    from qtsurfer.api.client.api.exchange import (
        download_klines,
        download_tickers,
        list_exchanges,
        list_instruments,
    )
    from qtsurfer.api.client.api.strategy import get_strategy, validate_strategy

    endpoints = [
        authenticate,
        list_exchanges,
        list_instruments,
        download_tickers,
        download_klines,
        get_strategy,
        validate_strategy,
        prepare_backtest,
        get_prepare_status,
        execute_backtest,
        cancel_backtest,
        get_backtest_result,
    ]
    for ep in endpoints:
        # Each generated endpoint module exposes the four standard entry points.
        assert callable(ep.sync)
        assert callable(ep.sync_detailed)
        assert callable(ep.asyncio)
        assert callable(ep.asyncio_detailed)


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
