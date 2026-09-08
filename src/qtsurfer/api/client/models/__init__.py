"""Re-export of every generated model plus public scalar aliases.

All request/response dataclasses live in
``qtsurfer.api.client._generated.models``; importing this module makes
them available at the shorter ``qtsurfer.api.client.models`` path.
"""

from typing import TypeAlias

from qtsurfer.api.client._generated.models import *  # noqa: F401,F403
from qtsurfer.api.client._generated.models import __all__ as _generated_all

# The generator flattens a named primitive-only `oneOf` schema while it builds
# map values. Keep the spec name available to consumers at the public facade.
ScalarStrategyParamValue: TypeAlias = bool | float | str

__all__ = (*_generated_all, "ScalarStrategyParamValue")
