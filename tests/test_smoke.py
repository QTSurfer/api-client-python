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
    from qtsurfer.api.client.api.auth import auth
    from qtsurfer.api.client.api.backtesting import (
        cancel_execution,
        execute_backtesting,
        get_execution_result,
        get_preparation_status,
        prepare_backtesting,
    )
    from qtsurfer.api.client.api.exchange import (
        get_exchange_klines_hour,
        get_exchange_tickers_hour,
        get_exchanges,
        get_instruments,
    )
    from qtsurfer.api.client.api.strategy import get_strategy_status

    endpoints = [
        auth,
        get_exchanges,
        get_instruments,
        get_exchange_tickers_hour,
        get_exchange_klines_hour,
        get_strategy_status,
        prepare_backtesting,
        get_preparation_status,
        execute_backtesting,
        cancel_execution,
        get_execution_result,
    ]
    for ep in endpoints:
        # Each generated endpoint module exposes the four standard entry points.
        assert callable(ep.sync)
        assert callable(ep.sync_detailed)
        assert callable(ep.asyncio)
        assert callable(ep.asyncio_detailed)


def test_models_re_export() -> None:
    from qtsurfer.api.client.models import (
        AuthError,
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
    assert AuthError is not None
