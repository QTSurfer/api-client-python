from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SignalCodesRequest")


@_attrs_define
class SignalCodesRequest:
    """
    Attributes:
        count (int):
    """

    count: int

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        signal_codes_request = cls(
            count=count,
        )

        return signal_codes_request
