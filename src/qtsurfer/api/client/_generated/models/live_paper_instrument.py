from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.live_paper_instrument_open_position import LivePaperInstrumentOpenPosition
    from ..models.live_paper_kpi import LivePaperKpi


T = TypeVar("T", bound="LivePaperInstrument")


@_attrs_define
class LivePaperInstrument:
    """One instrument's part of a shared paper account.

    Attributes:
        instrument (str):  Example: BTC/USDT.
        trades (int): Its closed trades.
        wins (int): Closed trades with a PnL above zero.
        losses (int): The other closed trades; a trade with a PnL of exactly zero is a loss.
        realised_pnl (float): Sum of the PnL of its closed trades, in the account's currency.
        contribution_pct (float | Unset): `realisedPnl` as a percent of the account's `initialFunding` (0-100 scale), so
            the contributions of the instruments add up to the account's realised return.
        unrealised_pnl (float | Unset): What its open position is worth over its cost as of the last mark; `0` when it
            holds nothing. Absent while its position has no current mark (see `openPosition`).
        total_pnl (float | Unset): `realisedPnl` plus `unrealisedPnl`. Absent when `unrealisedPnl` is.
        open_position (LivePaperInstrumentOpenPosition | Unset): What it holds now. Absent when it holds nothing.
        kpi (LivePaperKpi | Unset): The same KPIs a backtest reports, over the trades closed so far. Absent until the
            first closed trade is recorded.
    """

    instrument: str
    trades: int
    wins: int
    losses: int
    realised_pnl: float
    contribution_pct: float | Unset = UNSET
    unrealised_pnl: float | Unset = UNSET
    total_pnl: float | Unset = UNSET
    open_position: LivePaperInstrumentOpenPosition | Unset = UNSET
    kpi: LivePaperKpi | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instrument = self.instrument

        trades = self.trades

        wins = self.wins

        losses = self.losses

        realised_pnl = self.realised_pnl

        contribution_pct = self.contribution_pct

        unrealised_pnl = self.unrealised_pnl

        total_pnl = self.total_pnl

        open_position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.open_position, Unset):
            open_position = self.open_position.to_dict()

        kpi: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kpi, Unset):
            kpi = self.kpi.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instrument": instrument,
                "trades": trades,
                "wins": wins,
                "losses": losses,
                "realisedPnl": realised_pnl,
            }
        )
        if contribution_pct is not UNSET:
            field_dict["contributionPct"] = contribution_pct
        if unrealised_pnl is not UNSET:
            field_dict["unrealisedPnl"] = unrealised_pnl
        if total_pnl is not UNSET:
            field_dict["totalPnl"] = total_pnl
        if open_position is not UNSET:
            field_dict["openPosition"] = open_position
        if kpi is not UNSET:
            field_dict["kpi"] = kpi

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.live_paper_instrument_open_position import LivePaperInstrumentOpenPosition
        from ..models.live_paper_kpi import LivePaperKpi

        d = dict(src_dict)
        instrument = d.pop("instrument")

        trades = d.pop("trades")

        wins = d.pop("wins")

        losses = d.pop("losses")

        realised_pnl = d.pop("realisedPnl")

        contribution_pct = d.pop("contributionPct", UNSET)

        unrealised_pnl = d.pop("unrealisedPnl", UNSET)

        total_pnl = d.pop("totalPnl", UNSET)

        _open_position = d.pop("openPosition", UNSET)
        open_position: LivePaperInstrumentOpenPosition | Unset
        if isinstance(_open_position, Unset):
            open_position = UNSET
        else:
            open_position = LivePaperInstrumentOpenPosition.from_dict(_open_position)

        _kpi = d.pop("kpi", UNSET)
        kpi: LivePaperKpi | Unset
        if isinstance(_kpi, Unset):
            kpi = UNSET
        else:
            kpi = LivePaperKpi.from_dict(_kpi)

        live_paper_instrument = cls(
            instrument=instrument,
            trades=trades,
            wins=wins,
            losses=losses,
            realised_pnl=realised_pnl,
            contribution_pct=contribution_pct,
            unrealised_pnl=unrealised_pnl,
            total_pnl=total_pnl,
            open_position=open_position,
            kpi=kpi,
        )

        live_paper_instrument.additional_properties = d
        return live_paper_instrument

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
