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
``pending``; on ``200`` there is nothing to wait for. A full ``StrategyState``
(the ``200`` here, and ``get_strategy``'s response) carries an optional
``field_links`` (wire ``_links``) with a ``code`` `HalLink` pointing at
``get_strategy_code``; the ``202`` stub omits it, since a check that only
just started has nothing to link to yet.

``list_strategies`` returns every strategy you have registered and not
deleted, most recently compiled first — but deliberately without each one's
``validation`` state, so listing stays cheap no matter how many strategies
you have. Check a specific strategy's validation with ``get_strategy``.
Never ``404``s; an empty ``strategies`` list means you have none registered.

``delete_strategy`` removes a strategy from both ``get_strategy`` and
``list_strategies``. It does not undo anything that already happened:
backtests already run against this strategy are unaffected, and it only
ever removes your own registration — deleting your copy of a
shared/marketplace strategy never affects anyone else's copy. Re-submitting
the same source to ``compile_strategy`` afterwards registers a brand-new
strategy with a brand-new id; the old id stays gone.

``get_strategy_code`` returns the exact source last submitted for a
strategy id. Its ``404`` covers two cases that are deliberately
indistinguishable from the response alone: the id was never registered by
you, or it resolves only through a shared/marketplace reference that
carries no source of its own.
"""

from qtsurfer.api.client._generated.api.strategy import (
    delete_strategy,
    get_strategy,
    get_strategy_code,
    list_strategies,
    validate_strategy,
)

__all__ = ["delete_strategy", "get_strategy", "get_strategy_code", "list_strategies", "validate_strategy"]
