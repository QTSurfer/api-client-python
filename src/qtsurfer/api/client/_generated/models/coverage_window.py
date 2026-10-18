from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CoverageWindow")


@_attrs_define
class CoverageWindow:
    """The time range of available data for a single data type

    Attributes:
        from_ (datetime.datetime | Unset): Earliest timestamp with data available Example: 2026-04-10T21:00:00Z.
        to (datetime.datetime | Unset): Latest timestamp with data available Example: 2026-07-09T20:31:08Z.
        inactive_since (datetime.datetime | Unset): If the instrument stopped producing this data type
            (delisted/inactive), the timestamp it went inactive. Optional — omitted while the instrument is active. Example:
            2026-06-30T12:00:00Z.
    """

    from_: datetime.datetime | Unset = UNSET
    to: datetime.datetime | Unset = UNSET
    inactive_since: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        inactive_since: str | Unset = UNSET
        if not isinstance(self.inactive_since, Unset):
            inactive_since = self.inactive_since.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if inactive_since is not UNSET:
            field_dict["inactiveSince"] = inactive_since

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _from_ = d.pop("from", UNSET)
        from_: datetime.datetime | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_)

        _to = d.pop("to", UNSET)
        to: datetime.datetime | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = isoparse(_to)

        _inactive_since = d.pop("inactiveSince", UNSET)
        inactive_since: datetime.datetime | Unset
        if isinstance(_inactive_since, Unset):
            inactive_since = UNSET
        else:
            inactive_since = isoparse(_inactive_since)

        coverage_window = cls(
            from_=from_,
            to=to,
            inactive_since=inactive_since,
        )

        coverage_window.additional_properties = d
        return coverage_window

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
