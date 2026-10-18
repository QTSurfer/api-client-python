from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.equity_curve_out_mode import EquityCurveOutMode

T = TypeVar("T", bound="EquityCurveMeta")


@_attrs_define
class EquityCurveMeta:
    """What the transform pipeline actually did, computed from the observed outcome — never a copy of what was requested.
    Lets a caller detect a forced or no-op transform (e.g. a `resample` ceiling already above the curve's size is a
    legal no-op, reported honestly as `resampled: false`).

        Attributes:
            input_point_count (int): Size of the curve the transform pipeline received. Example: 100000.
            output_point_count (int): Size after the full pipeline (resample, then differential, then outMode). Example:
                100.
            resampled (bool): True only if the resample stage actually changed the point count.
            differential (bool): True only if delta-encoding actually ran. Requesting it on a curve of 0 or 1 points has
                nothing to encode, so it does not run even if asked.
            out_mode (EquityCurveOutMode): JSON shape for an equity curve's points. `ARRAY` is `[{timestamp, equity}, ...]`;
                `SHORT` is `{timestamps: [...], equities: [...]}` (parallel arrays, no repeated key text). The one schema shared
                by every place `outMode` appears, request or response, so the two cannot drift to different value sets.
    """

    input_point_count: int
    output_point_count: int
    resampled: bool
    differential: bool
    out_mode: EquityCurveOutMode
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_point_count = self.input_point_count

        output_point_count = self.output_point_count

        resampled = self.resampled

        differential = self.differential

        out_mode = self.out_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inputPointCount": input_point_count,
                "outputPointCount": output_point_count,
                "resampled": resampled,
                "differential": differential,
                "outMode": out_mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_point_count = d.pop("inputPointCount")

        output_point_count = d.pop("outputPointCount")

        resampled = d.pop("resampled")

        differential = d.pop("differential")

        out_mode = EquityCurveOutMode(d.pop("outMode"))

        equity_curve_meta = cls(
            input_point_count=input_point_count,
            output_point_count=output_point_count,
            resampled=resampled,
            differential=differential,
            out_mode=out_mode,
        )

        equity_curve_meta.additional_properties = d
        return equity_curve_meta

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
