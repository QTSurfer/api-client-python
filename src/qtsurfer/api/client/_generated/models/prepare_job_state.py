from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.job_state_status import JobStateStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prepare_job_state_hours_without_data_item import PrepareJobStateHoursWithoutDataItem


T = TypeVar("T", bound="PrepareJobState")


@_attrs_define
class PrepareJobState:
    """State of a single-instrument prepare job — the `JobState` shape plus a coverage summary.
    A single-instrument prepare is always terminal (`status: Completed`): the client decides
    what to do from `coverageRatio` (e.g. execute if it is at or above a chosen threshold)
    rather than polling for missing hours that may never arrive — a missing hour for one
    instrument usually means low activity, not missing data.

    **Two coverage shapes, by exchange vs. dataset.** Against a managed exchange, coverage is
    walked hour by hour: `totalHours`/`hoursWithData`/`hoursWithoutData`. Against a
    dataset-backed prepare (`exchangeId: user`), coverage is reported on the dataset's own
    cadence grid instead — hour-walking a daily dataset would report `1/24` and read as
    broken — via `cadence`/`gaps`/`largestGapSteps`; `totalHours`/`hoursWithData`/
    `hoursWithoutData` are absent in that case. `dataFrom`/`dataTo`/`coverageRatio` are present
    either way, computed accordingly.

        Attributes:
            context_id (str): Identifier for the job's execution context. Its current shape is a colon-delimited string
                encoding the data source type, an internal user id, the exchange, the job id, and the instrument — but that
                structure is not a committed contract and may change without notice. Treat it as an opaque token: store and pass
                it back, don't parse it. Example:
                jctx:ticker:76b90203-03c2-46f6-b366-9944f167e818:binance:5ikyamio8b3v9wcnfxztzg:btc/usdt:0vicnz3thzhrqvfczks1pu.
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
            data_from (datetime.datetime | None | Unset): Start of the available data range for the prepared instrument.
                Example: 2026-04-14T13:00:00Z.
            data_to (datetime.datetime | None | Unset): End of the available data range for the prepared instrument.
                Example: 2026-04-14T15:30:05Z.
            coverage_ratio (float | Unset): Against a managed exchange: `hoursWithData / totalHours` in `[0,1]` (`1.0` when
                `totalHours` is 0), the fraction of hours in the requested range that have served
                data. Against a dataset (`exchangeId: user`): `rows / expectedStepsAtCadence`
                over the dataset version's own range — echoing what ingest computed once, not
                recomputed against a narrower prepare request.
                 Example: 0.994.
            total_hours (int | Unset): Number of whole hours in the requested prepare range. Managed exchanges only —
                absent for a dataset-backed prepare.
                 Example: 168.
            hours_with_data (int | Unset): Number of hours in the range that have data. Managed exchanges only — absent for
                a dataset-backed prepare.
                 Example: 167.
            cadence (str | Unset): The dataset version's own discovered cadence (e.g. `1m`, `1h`). Only present for a
                dataset-backed prepare (`exchangeId: user`).
                 Example: 1m.
            gaps (int | Unset): Number of gaps in the dataset version at its own cadence, as discovered at ingest
                time. Only present for a dataset-backed prepare.
            largest_gap_steps (int | Unset): The largest gap in the dataset version, in units of its own cadence step. Only
                present for a dataset-backed prepare.
            hours_without_data (list[PrepareJobStateHoursWithoutDataItem] | Unset): One entry per hour in the range that has
                no data, with a rationale. Managed
                exchanges only — absent for a dataset-backed prepare.
    """

    context_id: str
    status: JobStateStatus
    size: int
    completed: int
    status_detail: None | str | Unset = UNSET
    start_time: datetime.datetime | None | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    data_from: datetime.datetime | None | Unset = UNSET
    data_to: datetime.datetime | None | Unset = UNSET
    coverage_ratio: float | Unset = UNSET
    total_hours: int | Unset = UNSET
    hours_with_data: int | Unset = UNSET
    cadence: str | Unset = UNSET
    gaps: int | Unset = UNSET
    largest_gap_steps: int | Unset = UNSET
    hours_without_data: list[PrepareJobStateHoursWithoutDataItem] | Unset = UNSET
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

        data_from: None | str | Unset
        if isinstance(self.data_from, Unset):
            data_from = UNSET
        elif isinstance(self.data_from, datetime.datetime):
            data_from = self.data_from.isoformat()
        else:
            data_from = self.data_from

        data_to: None | str | Unset
        if isinstance(self.data_to, Unset):
            data_to = UNSET
        elif isinstance(self.data_to, datetime.datetime):
            data_to = self.data_to.isoformat()
        else:
            data_to = self.data_to

        coverage_ratio = self.coverage_ratio

        total_hours = self.total_hours

        hours_with_data = self.hours_with_data

        cadence = self.cadence

        gaps = self.gaps

        largest_gap_steps = self.largest_gap_steps

        hours_without_data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hours_without_data, Unset):
            hours_without_data = []
            for hours_without_data_item_data in self.hours_without_data:
                hours_without_data_item = hours_without_data_item_data.to_dict()
                hours_without_data.append(hours_without_data_item)

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
        if data_from is not UNSET:
            field_dict["dataFrom"] = data_from
        if data_to is not UNSET:
            field_dict["dataTo"] = data_to
        if coverage_ratio is not UNSET:
            field_dict["coverageRatio"] = coverage_ratio
        if total_hours is not UNSET:
            field_dict["totalHours"] = total_hours
        if hours_with_data is not UNSET:
            field_dict["hoursWithData"] = hours_with_data
        if cadence is not UNSET:
            field_dict["cadence"] = cadence
        if gaps is not UNSET:
            field_dict["gaps"] = gaps
        if largest_gap_steps is not UNSET:
            field_dict["largestGapSteps"] = largest_gap_steps
        if hours_without_data is not UNSET:
            field_dict["hoursWithoutData"] = hours_without_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prepare_job_state_hours_without_data_item import PrepareJobStateHoursWithoutDataItem

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

        def _parse_data_from(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_from_type_0 = isoparse(data)

                return data_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        data_from = _parse_data_from(d.pop("dataFrom", UNSET))

        def _parse_data_to(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_to_type_0 = isoparse(data)

                return data_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        data_to = _parse_data_to(d.pop("dataTo", UNSET))

        coverage_ratio = d.pop("coverageRatio", UNSET)

        total_hours = d.pop("totalHours", UNSET)

        hours_with_data = d.pop("hoursWithData", UNSET)

        cadence = d.pop("cadence", UNSET)

        gaps = d.pop("gaps", UNSET)

        largest_gap_steps = d.pop("largestGapSteps", UNSET)

        _hours_without_data = d.pop("hoursWithoutData", UNSET)
        hours_without_data: list[PrepareJobStateHoursWithoutDataItem] | Unset = UNSET
        if _hours_without_data is not UNSET:
            hours_without_data = []
            for hours_without_data_item_data in _hours_without_data:
                hours_without_data_item = PrepareJobStateHoursWithoutDataItem.from_dict(hours_without_data_item_data)

                hours_without_data.append(hours_without_data_item)

        prepare_job_state = cls(
            context_id=context_id,
            status=status,
            size=size,
            completed=completed,
            status_detail=status_detail,
            start_time=start_time,
            end_time=end_time,
            data_from=data_from,
            data_to=data_to,
            coverage_ratio=coverage_ratio,
            total_hours=total_hours,
            hours_with_data=hours_with_data,
            cadence=cadence,
            gaps=gaps,
            largest_gap_steps=largest_gap_steps,
            hours_without_data=hours_without_data,
        )

        prepare_job_state.additional_properties = d
        return prepare_job_state

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
