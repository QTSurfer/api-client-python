"""Endpoints for the ``Strategy`` tag — re-exported from the generated tree.

Note: ``compileStrategy`` (``POST /strategy``) is currently absent because the
OpenAPI spec declares its request body as ``text/plain``, which the
``openapi-python-client`` generator does not yet support. Call it through
the underlying ``httpx`` client until the spec is restructured.
"""

from qtsurfer.api.client._generated.api.strategy import get_strategy

__all__ = ["get_strategy"]
