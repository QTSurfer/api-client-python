from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sweep_run_row_params import SweepRunRowParams


T = TypeVar("T", bound="SweepRunRow")


@_attrs_define
class SweepRunRow:
    """
    Attributes:
        run_ix (int): Deterministic zero-based expansion index, stable across shards and ranking.
        params (SweepRunRowParams):
        sharpe (float):
        sortino (float):
        pnl (float): Absolute net PnL in the output currency.
        pnl_pct (float):
        cagr (float):
        max_dd_pct (float):
        trades (int):
        win_rate (float):
        below_trade_floor (bool):
        aborted (bool):
        runtime_ms (int):
        rank (int | Unset): Present only in the `ranked` view.
    """

    run_ix: int
    params: SweepRunRowParams
    sharpe: float
    sortino: float
    pnl: float
    pnl_pct: float
    cagr: float
    max_dd_pct: float
    trades: int
    win_rate: float
    below_trade_floor: bool
    aborted: bool
    runtime_ms: int
    rank: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_ix = self.run_ix

        params = self.params.to_dict()

        sharpe = self.sharpe

        sortino = self.sortino

        pnl = self.pnl

        pnl_pct = self.pnl_pct

        cagr = self.cagr

        max_dd_pct = self.max_dd_pct

        trades = self.trades

        win_rate = self.win_rate

        below_trade_floor = self.below_trade_floor

        aborted = self.aborted

        runtime_ms = self.runtime_ms

        rank = self.rank

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runIx": run_ix,
                "params": params,
                "sharpe": sharpe,
                "sortino": sortino,
                "pnl": pnl,
                "pnlPct": pnl_pct,
                "cagr": cagr,
                "maxDdPct": max_dd_pct,
                "trades": trades,
                "winRate": win_rate,
                "belowTradeFloor": below_trade_floor,
                "aborted": aborted,
                "runtimeMs": runtime_ms,
            }
        )
        if rank is not UNSET:
            field_dict["rank"] = rank

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sweep_run_row_params import SweepRunRowParams

        d = dict(src_dict)
        run_ix = d.pop("runIx")

        params = SweepRunRowParams.from_dict(d.pop("params"))

        sharpe = d.pop("sharpe")

        sortino = d.pop("sortino")

        pnl = d.pop("pnl")

        pnl_pct = d.pop("pnlPct")

        cagr = d.pop("cagr")

        max_dd_pct = d.pop("maxDdPct")

        trades = d.pop("trades")

        win_rate = d.pop("winRate")

        below_trade_floor = d.pop("belowTradeFloor")

        aborted = d.pop("aborted")

        runtime_ms = d.pop("runtimeMs")

        rank = d.pop("rank", UNSET)

        sweep_run_row = cls(
            run_ix=run_ix,
            params=params,
            sharpe=sharpe,
            sortino=sortino,
            pnl=pnl,
            pnl_pct=pnl_pct,
            cagr=cagr,
            max_dd_pct=max_dd_pct,
            trades=trades,
            win_rate=win_rate,
            below_trade_floor=below_trade_floor,
            aborted=aborted,
            runtime_ms=runtime_ms,
            rank=rank,
        )

        sweep_run_row.additional_properties = d
        return sweep_run_row

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
