from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.equity_curve_out_mode import EquityCurveOutMode
from ..models.equity_curve_request_mode import EquityCurveRequestMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="EquityCurveRequest")


@_attrs_define
class EquityCurveRequest:
    """Selection (`mode`/`n`/`maxPct`) plus the transform preference (`resample`/`differential`/`outMode`) applied by `GET
    .../equityCurve` whenever ITS OWN query params are absent, for a curve this sweep retained. The transform half never
    affects retention or `sweepId` — a caller can always override it per-request at read time regardless of what was
    submitted here.

        Attributes:
            resample (int | Unset): Downsample to at most this many points (extrema-preserving — the global max/min and the
                exact first/last point are always kept). Omit for no downsampling.
            differential (bool | Unset): Delta-encode both fields from the second (post-resample) point onward. Default:
                False.
            out_mode (EquityCurveOutMode | Unset): JSON shape for an equity curve's points. `ARRAY` is `[{timestamp,
                equity}, ...]`; `SHORT` is `{timestamps: [...], equities: [...]}` (parallel arrays, no repeated key text). The
                one schema shared by every place `outMode` appears, request or response, so the two cannot drift to different
                value sets. Default: EquityCurveOutMode.ARRAY.
            mode (EquityCurveRequestMode | Unset): Which trials keep their per-point equity curve. `auto` retains curves
                only while the accumulated size stays within server limits; `topN`/`topPct` retain curves for the best-ranked
                trials explicitly; `none` retains no curves. Default: EquityCurveRequestMode.AUTO.
            n (int | Unset): Trial count to retain when mode is topN.
            max_pct (float | Unset): Top percentage of trials to retain when mode is topPct.
    """

    resample: int | Unset = UNSET
    differential: bool | Unset = False
    out_mode: EquityCurveOutMode | Unset = EquityCurveOutMode.ARRAY
    mode: EquityCurveRequestMode | Unset = EquityCurveRequestMode.AUTO
    n: int | Unset = UNSET
    max_pct: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resample = self.resample

        differential = self.differential

        out_mode: str | Unset = UNSET
        if not isinstance(self.out_mode, Unset):
            out_mode = self.out_mode.value

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        n = self.n

        max_pct = self.max_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resample is not UNSET:
            field_dict["resample"] = resample
        if differential is not UNSET:
            field_dict["differential"] = differential
        if out_mode is not UNSET:
            field_dict["outMode"] = out_mode
        if mode is not UNSET:
            field_dict["mode"] = mode
        if n is not UNSET:
            field_dict["n"] = n
        if max_pct is not UNSET:
            field_dict["maxPct"] = max_pct

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

        _mode = d.pop("mode", UNSET)
        mode: EquityCurveRequestMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = EquityCurveRequestMode(_mode)

        n = d.pop("n", UNSET)

        max_pct = d.pop("maxPct", UNSET)

        equity_curve_request = cls(
            resample=resample,
            differential=differential,
            out_mode=out_mode,
            mode=mode,
            n=n,
            max_pct=max_pct,
        )

        equity_curve_request.additional_properties = d
        return equity_curve_request

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
