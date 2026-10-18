from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_upload_state_status import DatasetUploadStateStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_version import DatasetVersion


T = TypeVar("T", bound="DatasetUploadState")


@_attrs_define
class DatasetUploadState:
    """Progress of one upload, from staged through ingest. Durably recorded once a version exists,
    so `ready`/`failed` are permanent answers; `uploading`/`ingesting` reflect in-flight state
    that can itself age out — see the `404` case on `GET .../uploads/{uploadId}`.

        Attributes:
            upload_id (str):  Example: up_1a2b3c4d5e6f7a8b.
            status (DatasetUploadStateStatus): * `uploading` — the file was PUT to the presigned URL, but `finalize` has not
                been
                  called yet.
                * `ingesting` — `finalize` was called; the worker is parsing and validating the file.
                * `ready` — ingested successfully. `version` carries the result.
                * `failed` — ingest rejected the file (e.g. bad CSV contract, mixed timestamp units, a
                  `.zip` with no file inside or more than one).
                 Example: ready.
            job_id (str | Unset): The ingest job id, while `status` is `ingesting`.
            error (str | Unset): A human-readable reason, present when `status` is `failed` (e.g. bad CSV contract,
                mixed timestamp units, a `.zip` with no file inside or more than one). Durably
                recorded alongside the failure itself, so it stays available however long after the
                fact you poll — not tied to how recently the failure happened.
                 Example: line 3: column 'close' is not a number: not-a-number.
            version (DatasetVersion | Unset): One successfully ingested upload. Cadence and timestamp unit are discovered
                from the file,
                not declared by the caller.
    """

    upload_id: str
    status: DatasetUploadStateStatus
    job_id: str | Unset = UNSET
    error: str | Unset = UNSET
    version: DatasetVersion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_id = self.upload_id

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
                "uploadId": upload_id,
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
        upload_id = d.pop("uploadId")

        status = DatasetUploadStateStatus(d.pop("status"))

        job_id = d.pop("jobId", UNSET)

        error = d.pop("error", UNSET)

        _version = d.pop("version", UNSET)
        version: DatasetVersion | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = DatasetVersion.from_dict(_version)

        dataset_upload_state = cls(
            upload_id=upload_id,
            status=status,
            job_id=job_id,
            error=error,
            version=version,
        )

        dataset_upload_state.additional_properties = d
        return dataset_upload_state

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
