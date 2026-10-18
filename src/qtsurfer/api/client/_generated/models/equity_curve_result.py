from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.equity_curve_meta import EquityCurveMeta
    from ..models.equity_point import EquityPoint


T = TypeVar("T", bound="EquityCurveResult")


@_attrs_define
class EquityCurveResult:
    """An equity curve, shaped per `meta.outMode`: `points` when `ARRAY`, `timestamps` + `equities` (parallel arrays) when
    `SHORT`. Used identically wherever a curve is returned — a plain backtest's inline `equityCurve` and a sweep row's
    `equityCurve` are the same type. `url` is present *instead of* any points when the curve is served by pointer rather
    than inline (a sweep row's top-N winners only): `GET` it separately to fetch this exact same shape with the points
    populated.

        Attributes:
            meta (EquityCurveMeta): What the transform pipeline actually did, computed from the observed outcome — never a
                copy of what was requested. Lets a caller detect a forced or no-op transform (e.g. a `resample` ceiling already
                above the curve's size is a legal no-op, reported honestly as `resampled: false`).
            points (list[EquityPoint] | Unset): Present when `meta.outMode` is `ARRAY` and the curve is inline (not a
                pointer).
            timestamps (list[int] | Unset): Present when `meta.outMode` is `SHORT` and the curve is inline (not a pointer).
            equities (list[float] | Unset): Present when `meta.outMode` is `SHORT` and the curve is inline (not a pointer),
                parallel to `timestamps` (same index, same point).
            url (str | Unset): Present only for a sweep row's pointer curve. `GET` this to fetch the curve itself, in this
                exact `{points|timestamps+equities, meta}` shape — `meta` there is the real, possibly size-guarded outcome; this
                outer `meta` is a raw, untransformed preview from the moment the sweep selected this trial's curve, and the two
                can legitimately differ. Example: /v1/backtest/binance/ticker/executeSweep/req-1/swp_test/runs/3/equityCurve.
    """

    meta: EquityCurveMeta
    points: list[EquityPoint] | Unset = UNSET
    timestamps: list[int] | Unset = UNSET
    equities: list[float] | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta = self.meta.to_dict()

        points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item = points_item_data.to_dict()
                points.append(points_item)

        timestamps: list[int] | Unset = UNSET
        if not isinstance(self.timestamps, Unset):
            timestamps = self.timestamps

        equities: list[float] | Unset = UNSET
        if not isinstance(self.equities, Unset):
            equities = self.equities

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meta": meta,
            }
        )
        if points is not UNSET:
            field_dict["points"] = points
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps
        if equities is not UNSET:
            field_dict["equities"] = equities
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.equity_curve_meta import EquityCurveMeta
        from ..models.equity_point import EquityPoint

        d = dict(src_dict)
        meta = EquityCurveMeta.from_dict(d.pop("meta"))

        _points = d.pop("points", UNSET)
        points: list[EquityPoint] | Unset = UNSET
        if _points is not UNSET:
            points = []
            for points_item_data in _points:
                points_item = EquityPoint.from_dict(points_item_data)

                points.append(points_item)

        timestamps = cast(list[int], d.pop("timestamps", UNSET))

        equities = cast(list[float], d.pop("equities", UNSET))

        url = d.pop("url", UNSET)

        equity_curve_result = cls(
            meta=meta,
            points=points,
            timestamps=timestamps,
            equities=equities,
            url=url,
        )

        equity_curve_result.additional_properties = d
        return equity_curve_result

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
