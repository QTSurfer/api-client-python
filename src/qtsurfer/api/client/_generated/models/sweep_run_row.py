from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.equity_curve_result import EquityCurveResult
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
        pnl_pct (float): Same units as `pnlTotalPercent` on the single-run result — percent (0-100 scale).
        cagr (float): Same units as `cagr` on the single-run result — a ratio, not a percent.
        max_dd_pct (float): Same units as `maxDrawdownPercent` on the single-run result — percent (0-100 scale).
        trades (int):
        win_rate (float): Same units as `winRate` on the single-run result — a fraction, 0.0-1.0 (a rate, not a
            percent).
        below_trade_floor (bool):
        aborted (bool):
        runtime_ms (int):
        rank (int | Unset): Present only in the `ranked` view.
        plateau_score (float | Unset): The objective of the worst run in this point's immediate neighbourhood — how well
            the region around it holds up, not how well it scored itself. Present only in the `ranked` view when plateau
            ranking applied. Always read together with `neighbourCount`.
        neighbour_count (int | Unset): How many neighbouring parameter points backed the `plateauScore`. Zero means the
            point had no neighbours in the grid, so its score is unevidenced rather than confirmed — the value alone cannot
            be distinguished from a genuinely robust one.
        deflated_sharpe (float | Unset): Probability that this run's Sharpe reflects real edge rather than the best draw
            from however many parameter vectors were tried. Above ~0.95 the result survives the multiple-testing correction;
            near 0.5 or below it is indistinguishable from the best of a pile of coin flips. Absent on aborted runs, on
            sweeps with too few trials to establish any dispersion to deflate against, on runs with fewer than 3 period
            returns, and on a degenerate (near-constant) return series — all cases where the underlying statistic isn't
            meaningfully computable, rather than genuinely zero. A present value is the computed probability, however small.
        equity_curve (EquityCurveResult | Unset): An equity curve, shaped per `meta.outMode`: `points` when `ARRAY`,
            `timestamps` + `equities` (parallel arrays) when `SHORT`. Used identically wherever a curve is returned — a
            plain backtest's inline `equityCurve` and a sweep row's `equityCurve` are the same type. `url` is present
            *instead of* any points when the curve is served by pointer rather than inline (a sweep row's top-N winners
            only): `GET` it separately to fetch this exact same shape with the points populated.
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
    plateau_score: float | Unset = UNSET
    neighbour_count: int | Unset = UNSET
    deflated_sharpe: float | Unset = UNSET
    equity_curve: EquityCurveResult | Unset = UNSET
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

        plateau_score = self.plateau_score

        neighbour_count = self.neighbour_count

        deflated_sharpe = self.deflated_sharpe

        equity_curve: dict[str, Any] | Unset = UNSET
        if not isinstance(self.equity_curve, Unset):
            equity_curve = self.equity_curve.to_dict()

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
        if plateau_score is not UNSET:
            field_dict["plateauScore"] = plateau_score
        if neighbour_count is not UNSET:
            field_dict["neighbourCount"] = neighbour_count
        if deflated_sharpe is not UNSET:
            field_dict["deflatedSharpe"] = deflated_sharpe
        if equity_curve is not UNSET:
            field_dict["equityCurve"] = equity_curve

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.equity_curve_result import EquityCurveResult
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

        plateau_score = d.pop("plateauScore", UNSET)

        neighbour_count = d.pop("neighbourCount", UNSET)

        deflated_sharpe = d.pop("deflatedSharpe", UNSET)

        _equity_curve = d.pop("equityCurve", UNSET)
        equity_curve: EquityCurveResult | Unset
        if isinstance(_equity_curve, Unset):
            equity_curve = UNSET
        else:
            equity_curve = EquityCurveResult.from_dict(_equity_curve)

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
            plateau_score=plateau_score,
            neighbour_count=neighbour_count,
            deflated_sharpe=deflated_sharpe,
            equity_curve=equity_curve,
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
