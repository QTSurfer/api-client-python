from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_import_state_status import DatasetImportStateStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_version import DatasetVersion


T = TypeVar("T", bound="DatasetImportState")


@_attrs_define
class DatasetImportState:
    """Progress of one import, from fetching through ingest. `fetching` is the one status only an
    import ever reports — an upload's file already exists by the time you can poll it; an
    import's doesn't, until this source finishes fetching it.

        Attributes:
            import_id (str):  Example: imp_01j9z1x2y3z4a5b6c7d8e9f0g1.
            status (DatasetImportStateStatus): * `fetching` — reading from the source; nothing staged yet.
                * `ingesting` — fetch complete, staged, and re-entered the same ingest chain an
                  upload uses; the worker is parsing and validating it.
                * `ready` — ingested successfully. `version` carries the result.
                * `failed` — the fetch or the ingest that followed it was rejected. `error` names why.
                 Example: ready.
            job_id (str | Unset): The fetch/ingest job id, while `status` is `fetching` or `ingesting`.
            error (str | Unset): A human-readable reason, present when `status` is `failed` — an unresolvable
                pool/pair, no data in the requested range, a range older than the configured source
                retains, the fetch exceeding your tier's time ceiling, or any of
                `DatasetUploadState.error`'s own ingest-side reasons once fetching hands off to it.
                Durably recorded, same as on the upload path.
                 Example: Import exceeded the tier's 12 minute ceiling.
            version (DatasetVersion | Unset): One successfully ingested upload. Cadence and timestamp unit are discovered
                from the file,
                not declared by the caller.
    """

    import_id: str
    status: DatasetImportStateStatus
    job_id: str | Unset = UNSET
    error: str | Unset = UNSET
    version: DatasetVersion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        import_id = self.import_id

        status = self.status.value

        job_id = self.job_id

        error = self.error

        version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "importId": import_id,
                "status": status,
            }
        )
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if error is not UNSET:
            field_dict["error"] = error
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_version import DatasetVersion

        d = dict(src_dict)
        import_id = d.pop("importId")

        status = DatasetImportStateStatus(d.pop("status"))

        job_id = d.pop("jobId", UNSET)

        error = d.pop("error", UNSET)

        _version = d.pop("version", UNSET)
        version: DatasetVersion | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = DatasetVersion.from_dict(_version)

        dataset_import_state = cls(
            import_id=import_id,
            status=status,
            job_id=job_id,
            error=error,
            version=version,
        )

        dataset_import_state.additional_properties = d
        return dataset_import_state

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
