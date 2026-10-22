from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.live_paper_equity_curve_measure import LivePaperEquityCurveMeasure
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.equity_curve_meta import EquityCurveMeta
    from ..models.equity_point import EquityPoint
    from ..models.live_paper_equity_curve_links import LivePaperEquityCurveLinks


T = TypeVar("T", bound="LivePaperEquityCurve")


@_attrs_define
class LivePaperEquityCurve:
    """One paper account's equity curve: the API's one equity curve (`EquityCurveResult`, `{points|timestamps+equities,
    meta}`) with the account's `currency` and the `gaps` alongside.

        Attributes:
            meta (EquityCurveMeta): What the transform pipeline actually did, computed from the observed outcome — never a
                copy of what was requested. Lets a caller detect a forced or no-op transform (e.g. a `resample` ceiling already
                above the curve's size is a legal no-op, reported honestly as `resampled: false`).
            measure (LivePaperEquityCurveMeasure): What the values of the curve are: the account's `equity`, an instrument's
                cumulative `realisedPnl` from 0, or its `totalPnl` (the realised PnL plus the unrealised value of its open
                position). The shape names its values `equity` in every case.
            gaps (list[int]): Market times (epoch ms, oldest first) at which open positions were lost because the run was
                restarted with them open. A gap is not a point of the curve and is not counted in `meta`.
            points (list[EquityPoint] | Unset): Present when `meta.outMode` is `ARRAY` and the curve is inline (not a
                pointer).
            timestamps (list[int] | Unset): Present when `meta.outMode` is `SHORT` and the curve is inline (not a pointer).
            equities (list[float] | Unset): Present when `meta.outMode` is `SHORT` and the curve is inline (not a pointer),
                parallel to `timestamps` (same index, same point).
            url (str | Unset): Present only for a sweep row's pointer curve. `GET` this to fetch the curve itself, in this
                exact `{points|timestamps+equities, meta}` shape — `meta` there is the real, possibly size-guarded outcome; this
                outer `meta` is a raw, untransformed preview from the moment the sweep selected this trial's curve, and the two
                can legitimately differ. Example: /v1/backtest/binance/ticker/executeSweep/req-1/swp_test/runs/3/equityCurve.
            currency (str | Unset): The account's quote currency. Absent only when the run has no account yet, which gives
                an empty curve.
            instrument (str | Unset): Present when the curve is one instrument's (`measure` is `realisedPnl` or `totalPnl`)
                and, in a run started with `accounts: instrument`, when it is the curve of the account that instrument is
                (`measure` is `equity`). Example: BTC/USDT.
            field_links (LivePaperEquityCurveLinks | Unset): Present on a page of the raw curve while there is a next one.
    """

    meta: EquityCurveMeta
    measure: LivePaperEquityCurveMeasure
    gaps: list[int]
    points: list[EquityPoint] | Unset = UNSET
    timestamps: list[int] | Unset = UNSET
    equities: list[float] | Unset = UNSET
    url: str | Unset = UNSET
    currency: str | Unset = UNSET
    instrument: str | Unset = UNSET
    field_links: LivePaperEquityCurveLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta = self.meta.to_dict()

        measure = self.measure.value

        gaps = self.gaps

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

        currency = self.currency

        instrument = self.instrument

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meta": meta,
                "measure": measure,
                "gaps": gaps,
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
        if currency is not UNSET:
            field_dict["currency"] = currency
        if instrument is not UNSET:
            field_dict["instrument"] = instrument
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.equity_curve_meta import EquityCurveMeta
        from ..models.equity_point import EquityPoint
        from ..models.live_paper_equity_curve_links import LivePaperEquityCurveLinks

        d = dict(src_dict)
        meta = EquityCurveMeta.from_dict(d.pop("meta"))

        measure = LivePaperEquityCurveMeasure(d.pop("measure"))

        gaps = cast(list[int], d.pop("gaps"))

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

        currency = d.pop("currency", UNSET)

        instrument = d.pop("instrument", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: LivePaperEquityCurveLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = LivePaperEquityCurveLinks.from_dict(_field_links)

        live_paper_equity_curve = cls(
            meta=meta,
            measure=measure,
            gaps=gaps,
            points=points,
            timestamps=timestamps,
            equities=equities,
            url=url,
            currency=currency,
            instrument=instrument,
            field_links=field_links,
        )

        live_paper_equity_curve.additional_properties = d
        return live_paper_equity_curve

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
