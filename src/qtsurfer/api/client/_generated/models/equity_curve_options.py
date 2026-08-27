from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.equity_curve_out_mode import EquityCurveOutMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="EquityCurveOptions")


@_attrs_define
class EquityCurveOptions:
    """Requested equity-curve transform, applied server-side in a fixed pipeline order: `resample` (point count) then
    `differential` (encoding) then `outMode` (JSON shape) — each stage assumes the previous one already ran. A server-
    side size guard can still force a smaller/deflated shape above its thresholds regardless of what is requested here —
    see `EquityCurveMeta` for what actually happened.

        Attributes:
            resample (int | Unset): Downsample to at most this many points (extrema-preserving — the global max/min and the
                exact first/last point are always kept). Omit for no downsampling.
            differential (bool | Unset): Delta-encode both fields from the second (post-resample) point onward. Default:
                False.
            out_mode (EquityCurveOutMode | Unset): JSON shape for an equity curve's points. `ARRAY` is `[{timestamp,
                equity}, ...]`; `SHORT` is `{timestamps: [...], equities: [...]}` (parallel arrays, no repeated key text). The
                one schema shared by every place `outMode` appears, request or response, so the two cannot drift to different
                value sets. Default: EquityCurveOutMode.ARRAY.
    """

    resample: int | Unset = UNSET
    differential: bool | Unset = False
    out_mode: EquityCurveOutMode | Unset = EquityCurveOutMode.ARRAY
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resample = self.resample

        differential = self.differential

        out_mode: str | Unset = UNSET
        if not isinstance(self.out_mode, Unset):
            out_mode = self.out_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resample is not UNSET:
            field_dict["resample"] = resample
        if differential is not UNSET:
            field_dict["differential"] = differential
        if out_mode is not UNSET:
            field_dict["outMode"] = out_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resample = d.pop("resample", UNSET)

        differential = d.pop("differential", UNSET)

        _out_mode = d.pop("outMode", UNSET)
        out_mode: EquityCurveOutMode | Unset
        if isinstance(_out_mode, Unset):
            out_mode = UNSET
        else:
            out_mode = EquityCurveOutMode(_out_mode)

        equity_curve_options = cls(
            resample=resample,
            differential=differential,
            out_mode=out_mode,
        )

        equity_curve_options.additional_properties = d
        return equity_curve_options

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
