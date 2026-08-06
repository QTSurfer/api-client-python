"""Endpoints for the ``Strategy`` tag — re-exported from the generated tree.

Note: ``compileStrategy`` (``POST /strategy``) is currently absent because the
OpenAPI spec declares its request body as ``text/plain``, which the
``openapi-python-client`` generator does not yet support. Call it through
the underlying ``httpx`` client until the spec is restructured.

``getStrategy`` and ``validateStrategy`` have no such restriction — neither
declares a ``text/plain`` request body (``getStrategy`` is JSON-out only,
``validateStrategy`` takes no body at all) — so both generate cleanly and
are re-exported below.
"""

from qtsurfer.api.client._generated.api.strategy import get_strategy, validate_strategy

__all__ = ["get_strategy", "validate_strategy"]
