"""Endpoints for the ``Live Execution`` tag — re-exported from the generated tree.

Use ``get_live_run_signals`` to read recorded signals after a disconnect or
when a run did not request WebSocket relay. A ``410`` response means its cursor
expired; restart from the error's ``availableSinceMs`` value. Paper endpoints
read simulated account state and equity history; ``send_live_command`` delivers
a transient command to a running strategy over REST. ``get_live_run`` reads a
specific run, while ``rotate_live_stream`` and ``revoke_live_stream`` manage a
stream URL issued when starting a run with ``stream=True``.
"""

from qtsurfer.api.client._generated.api.live_execution import (
    get_live,
    get_live_run,
    get_live_run_paper,
    get_live_run_paper_equity,
    get_live_run_signals,
    list_live,
    list_public_live,
    mint_live_connection_token,
    revoke_live_stream,
    rotate_live_stream,
    send_live_command,
    start_live,
    stop_live,
    update_live,
    update_live_params,
)

__all__ = [
    "get_live",
    "get_live_run",
    "get_live_run_paper",
    "get_live_run_paper_equity",
    "get_live_run_signals",
    "list_live",
    "list_public_live",
    "mint_live_connection_token",
    "revoke_live_stream",
    "rotate_live_stream",
    "start_live",
    "send_live_command",
    "stop_live",
    "update_live",
    "update_live_params",
]
