"""Endpoint subpackages — re-export of the generated ``_generated.api``.

Each tag in the OpenAPI spec becomes a submodule (``exchange``,
``strategy``, ``backtesting``) containing one endpoint per file. Each
endpoint module exposes ``sync``, ``sync_detailed``, ``asyncio``,
``asyncio_detailed``.
"""

from qtsurfer.api.client.api import backtesting, exchange, strategy

__all__ = ["backtesting", "exchange", "strategy"]
