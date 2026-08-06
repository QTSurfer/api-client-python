from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notice_provenance import NoticeProvenance
from ..types import UNSET, Unset

T = TypeVar("T", bound="Notice")


@_attrs_define
class Notice:
    """A diagnostic the engine raised while the strategy ran. Advisory: it describes something worth
    knowing about how the strategy is wired, not necessarily an error.

        Attributes:
            level (str): Severity as the engine classified it. Example: WARN.
            code (str): Stable identifier for the kind of finding; safe to match on. Example: indicator.bar-data-on-ticker-
                path.
            message (str): Human-readable explanation. Example: Indicator requires bar data but is on the ticker path.
            provenance (NoticeProvenance | Unset): Where it came from, which matters because the two silences differ: an
                empty list from a
                real run (`execute`) is a clean bill of health, while an empty list from
                `compile-dry-run` is only a lower bound over a bounded synthetic series.
                 Example: compile-dry-run.
    """

    level: str
    code: str
    message: str
    provenance: NoticeProvenance | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        level = self.level

        code = self.code

        message = self.message

        provenance: str | Unset = UNSET
        if not isinstance(self.provenance, Unset):
            provenance = self.provenance.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "level": level,
                "code": code,
                "message": message,
            }
        )
        if provenance is not UNSET:
            field_dict["provenance"] = provenance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        level = d.pop("level")

        code = d.pop("code")

        message = d.pop("message")

        _provenance = d.pop("provenance", UNSET)
        provenance: NoticeProvenance | Unset
        if isinstance(_provenance, Unset):
            provenance = UNSET
        else:
            provenance = NoticeProvenance(_provenance)

        notice = cls(
            level=level,
            code=code,
            message=message,
            provenance=provenance,
        )

        notice.additional_properties = d
        return notice

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
