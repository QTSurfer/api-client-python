from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LivePaperKpi")


@_attrs_define
class LivePaperKpi:
    """The same KPIs a backtest reports, over the trades closed so far. Absent until the first closed trade is recorded.

    Attributes:
        total_trades (int | Unset):
        win_count (int | Unset):
        loss_count (int | Unset):
        win_rate (float | Unset): Ratio (0.5 = half the trades won).
        pnl_total (float | Unset):
        pnl_total_percent (float | Unset): Percent of `initialFunding` (0-100 scale).
        sharpe_ratio (float | None | Unset):
        sortino_ratio (float | None | Unset):
        cagr (float | None | Unset): Ratio (0.15 for 15%).
        max_drawdown (float | Unset):
        max_drawdown_percent (float | Unset): Percent (0-100 scale).
    """

    total_trades: int | Unset = UNSET
    win_count: int | Unset = UNSET
    loss_count: int | Unset = UNSET
    win_rate: float | Unset = UNSET
    pnl_total: float | Unset = UNSET
    pnl_total_percent: float | Unset = UNSET
    sharpe_ratio: float | None | Unset = UNSET
    sortino_ratio: float | None | Unset = UNSET
    cagr: float | None | Unset = UNSET
    max_drawdown: float | Unset = UNSET
    max_drawdown_percent: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_trades = self.total_trades

        win_count = self.win_count

        loss_count = self.loss_count

        win_rate = self.win_rate

        pnl_total = self.pnl_total

        pnl_total_percent = self.pnl_total_percent

        sharpe_ratio: float | None | Unset
        if isinstance(self.sharpe_ratio, Unset):
            sharpe_ratio = UNSET
        else:
            sharpe_ratio = self.sharpe_ratio

        sortino_ratio: float | None | Unset
        if isinstance(self.sortino_ratio, Unset):
            sortino_ratio = UNSET
        else:
            sortino_ratio = self.sortino_ratio

        cagr: float | None | Unset
        if isinstance(self.cagr, Unset):
            cagr = UNSET
        else:
            cagr = self.cagr

        max_drawdown = self.max_drawdown

        max_drawdown_percent = self.max_drawdown_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_trades is not UNSET:
            field_dict["totalTrades"] = total_trades
        if win_count is not UNSET:
            field_dict["winCount"] = win_count
        if loss_count is not UNSET:
            field_dict["lossCount"] = loss_count
        if win_rate is not UNSET:
            field_dict["winRate"] = win_rate
        if pnl_total is not UNSET:
            field_dict["pnlTotal"] = pnl_total
        if pnl_total_percent is not UNSET:
            field_dict["pnlTotalPercent"] = pnl_total_percent
        if sharpe_ratio is not UNSET:
            field_dict["sharpeRatio"] = sharpe_ratio
        if sortino_ratio is not UNSET:
            field_dict["sortinoRatio"] = sortino_ratio
        if cagr is not UNSET:
            field_dict["cagr"] = cagr
        if max_drawdown is not UNSET:
            field_dict["maxDrawdown"] = max_drawdown
        if max_drawdown_percent is not UNSET:
            field_dict["maxDrawdownPercent"] = max_drawdown_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_trades = d.pop("totalTrades", UNSET)

        win_count = d.pop("winCount", UNSET)

        loss_count = d.pop("lossCount", UNSET)

        win_rate = d.pop("winRate", UNSET)

        pnl_total = d.pop("pnlTotal", UNSET)

        pnl_total_percent = d.pop("pnlTotalPercent", UNSET)

        def _parse_sharpe_ratio(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sharpe_ratio = _parse_sharpe_ratio(d.pop("sharpeRatio", UNSET))

        def _parse_sortino_ratio(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sortino_ratio = _parse_sortino_ratio(d.pop("sortinoRatio", UNSET))

        def _parse_cagr(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cagr = _parse_cagr(d.pop("cagr", UNSET))

        max_drawdown = d.pop("maxDrawdown", UNSET)

        max_drawdown_percent = d.pop("maxDrawdownPercent", UNSET)

        live_paper_kpi = cls(
            total_trades=total_trades,
            win_count=win_count,
            loss_count=loss_count,
            win_rate=win_rate,
            pnl_total=pnl_total,
            pnl_total_percent=pnl_total_percent,
            sharpe_ratio=sharpe_ratio,
            sortino_ratio=sortino_ratio,
            cagr=cagr,
            max_drawdown=max_drawdown,
            max_drawdown_percent=max_drawdown_percent,
        )

        live_paper_kpi.additional_properties = d
        return live_paper_kpi

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
