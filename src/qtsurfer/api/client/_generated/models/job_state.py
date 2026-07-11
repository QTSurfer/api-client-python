from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.job_state_status import JobStateStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobState")


@_attrs_define
class JobState:
    """Information about a single job

    Attributes:
        context_id (str): Opaque context identifier for the job Example: ctx_2o8heaioicr0edvx5ybcap.
        status (JobStateStatus): Current status of the job. Treat `Completed | Aborted | Failed` as
            terminal; `New | Started` mean keep polling. A single-instrument prepare
            is always terminal (`Completed`) — decide from
            `PrepareJobState.coverageRatio`, not by polling.
             Example: Completed.
        size (int): Total size of the data being prepared Example: 100.
        completed (int): The amount of data processed so far Example: 50.
        status_detail (None | str | Unset): Detailed status information, if available Example: Job completed with error
            code 5001.
        start_time (datetime.datetime | None | Unset): Timestamp for when the preparation started Example:
            2025-01-04T14:00:00Z.
        end_time (datetime.datetime | None | Unset): Timestamp for when the preparation finished Example:
            2025-01-04T14:00:20Z.
    """

    context_id: str
    status: JobStateStatus
    size: int
    completed: int
    status_detail: None | str | Unset = UNSET
    start_time: datetime.datetime | None | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context_id = self.context_id

        status = self.status.value

        size = self.size

        completed = self.completed

        status_detail: None | str | Unset
        if isinstance(self.status_detail, Unset):
            status_detail = UNSET
        else:
            status_detail = self.status_detail

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contextId": context_id,
                "status": status,
                "size": size,
                "completed": completed,
            }
        )
        if status_detail is not UNSET:
            field_dict["statusDetail"] = status_detail
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        context_id = d.pop("contextId")

        status = JobStateStatus(d.pop("status"))

        size = d.pop("size")

        completed = d.pop("completed")

        def _parse_status_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_detail = _parse_status_detail(d.pop("statusDetail", UNSET))

        def _parse_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = isoparse(data)

                return start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_time = _parse_start_time(d.pop("startTime", UNSET))

        def _parse_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = isoparse(data)

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time = _parse_end_time(d.pop("endTime", UNSET))

        job_state = cls(
            context_id=context_id,
            status=status,
            size=size,
            completed=completed,
            status_detail=status_detail,
            start_time=start_time,
            end_time=end_time,
        )

        job_state.additional_properties = d
        return job_state

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
