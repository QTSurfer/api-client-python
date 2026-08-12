"""Endpoints for the ``Strategy`` tag — re-exported from the generated tree.

Note: ``compileStrategy`` (``POST /strategy``) is currently absent because the
OpenAPI spec declares its request body as ``text/plain``, which the
``openapi-python-client`` generator does not yet support. Call it through
the underlying ``httpx`` client until the spec is restructured.

``getStrategy`` and ``validateStrategy`` have no such restriction — neither
declares a ``text/plain`` request body (``getStrategy`` is JSON-out only,
``validateStrategy`` takes no body at all) — so both generate cleanly and
are re-exported below.

Note: ``validate_strategy`` answers ``200`` and ``202`` with the same
``StrategyState`` type, so ``sync``/``asyncio`` cannot tell them apart —
both hand back a ``StrategyState`` and the return type carries no trace of
which arrived. **The status code is the distinction**: ``200`` means a
verdict already existed and is returned as-is, ``202`` means this call
queued a check. Use ``sync_detailed``/``asyncio_detailed`` and read
``.status_code`` when that matters, because ``validation: pending`` on its
own says only that some check is outstanding — it does not say this call
started one. On ``202``, poll ``get_strategy`` until ``validation`` leaves
``pending``; on ``200`` there is nothing to wait for.
"""

from qtsurfer.api.client._generated.api.strategy import get_strategy, validate_strategy

__all__ = ["get_strategy", "validate_strategy"]
