from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SweepAxisType0")


@_attrs_define
class SweepAxisType0:
    """
    Attributes:
        from_ (float):
        to (float):
        step (float):
    """

    from_: float
    to: float
    step: float

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to

        step = self.step

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "from": from_,
                "to": to,
                "step": step,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = d.pop("from")

        to = d.pop("to")

        step = d.pop("step")

        sweep_axis_type_0 = cls(
            from_=from_,
            to=to,
            step=step,
        )

        return sweep_axis_type_0
