"""Endpoints for the ``Dataset`` tag — re-exported from the generated tree.

Upload your own CSV ticker data and prepare/execute backtests against it via
the reserved ``exchangeId: user`` value on the existing ``Backtesting``
endpoints (``prepare_backtest`` / ``execute_backtest``), passing ``datasetId``
(and optionally ``datasetVersionId``) instead of ``instrument`` in the
request body.

``create_dataset`` creates a dataset and its first upload session in one
call, returning a presigned URL to ``PUT`` the CSV file to directly — no API
credentials involved in that ``PUT``. Call ``finalize_dataset_upload`` once
the upload completes to kick off ingest, then poll ``get_dataset_upload``
until ``status`` is ``ready`` or ``failed``.

``open_dataset_upload`` returns the current open upload session for an
existing dataset, or starts the next one after a finalized upload. A finalized
``upload_id`` cannot be reused: ``finalize_dataset_upload`` returns ``409``;
open a new session instead.

``import_dataset`` creates a dataset by fetching source history; poll
``get_dataset_import`` until its status is ``ready`` or ``failed``.

``list_datasets`` / ``get_dataset`` never ``404`` for "no datasets" — an
empty list, same convention as ``list_strategies``. ``delete_dataset`` is a
soft delete: the dataset stops being listed or preparable from, but a
backtest already running against one of its versions is not disrupted.
"""

from qtsurfer.api.client._generated.api.dataset import (
    create_dataset,
    delete_dataset,
    finalize_dataset_upload,
    get_dataset,
    get_dataset_import,
    get_dataset_upload,
    import_dataset,
    list_datasets,
    open_dataset_upload,
)

__all__ = [
    "create_dataset",
    "delete_dataset",
    "finalize_dataset_upload",
    "get_dataset",
    "get_dataset_import",
    "get_dataset_upload",
    "import_dataset",
    "list_datasets",
    "open_dataset_upload",
]
