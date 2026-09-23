"""Endpoint subpackages — re-export of the generated ``_generated.api``.

Each tag in the OpenAPI spec becomes a submodule (``account``, ``exchange``,
``strategy``, ``backtesting``, ``dataset``, ``live_execution``) containing one endpoint per
file. Each endpoint module exposes ``sync``, ``sync_detailed``, ``asyncio``,
``asyncio_detailed``.
"""

from qtsurfer.api.client.api import account, auth, backtesting, dataset, exchange, live_execution, strategy

__all__ = ["account", "auth", "backtesting", "dataset", "exchange", "live_execution", "strategy"]
