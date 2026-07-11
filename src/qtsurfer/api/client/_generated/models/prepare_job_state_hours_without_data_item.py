from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.prepare_job_state_hours_without_data_item_rationale import PrepareJobStateHoursWithoutDataItemRationale
from ..types import UNSET, Unset

T = TypeVar("T", bound="PrepareJobStateHoursWithoutDataItem")


@_attrs_define
class PrepareJobStateHoursWithoutDataItem:
    """
    Attributes:
        hour (datetime.datetime | Unset): The hour (UTC, hour-aligned) that has no data. Example: 2026-04-14T02:00:00Z.
        expected (int | Unset): Expected row count for the hour (currently always 0; reserved for
            future use). The rationale never depends on it.
        rationale (PrepareJobStateHoursWithoutDataItemRationale | Unset): Why the hour has no data.
            `pending_conversion`: data for this hour is
            still being produced — a re-poll may fill it. `low_activity`: the
            instrument did not trade that hour. `unknown`: no data to classify by.
             Example: low_activity.
    """

    hour: datetime.datetime | Unset = UNSET
    expected: int | Unset = UNSET
    rationale: PrepareJobStateHoursWithoutDataItemRationale | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hour: str | Unset = UNSET
        if not isinstance(self.hour, Unset):
            hour = self.hour.isoformat()

        expected = self.expected

        rationale: str | Unset = UNSET
        if not isinstance(self.rationale, Unset):
            rationale = self.rationale.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hour is not UNSET:
            field_dict["hour"] = hour
        if expected is not UNSET:
            field_dict["expected"] = expected
        if rationale is not UNSET:
            field_dict["rationale"] = rationale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _hour = d.pop("hour", UNSET)
        hour: datetime.datetime | Unset
        if isinstance(_hour, Unset):
            hour = UNSET
        else:
            hour = isoparse(_hour)

        expected = d.pop("expected", UNSET)

        _rationale = d.pop("rationale", UNSET)
        rationale: PrepareJobStateHoursWithoutDataItemRationale | Unset
        if isinstance(_rationale, Unset):
            rationale = UNSET
        else:
            rationale = PrepareJobStateHoursWithoutDataItemRationale(_rationale)

        prepare_job_state_hours_without_data_item = cls(
            hour=hour,
            expected=expected,
            rationale=rationale,
        )

        prepare_job_state_hours_without_data_item.additional_properties = d
        return prepare_job_state_hours_without_data_item

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
