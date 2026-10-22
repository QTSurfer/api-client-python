from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.live_paper_account_equity_kind import LivePaperAccountEquityKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.live_paper_instrument import LivePaperInstrument
    from ..models.live_paper_kpi import LivePaperKpi
    from ..models.live_paper_position import LivePaperPosition


T = TypeVar("T", bound="LivePaperAccount")


@_attrs_define
class LivePaperAccount:
    """One simulated account: one per quote currency the run trades, or one per instrument when the run was started with
    `accounts: instrument`.

        Attributes:
            currency (str): The account's quote currency; every amount below is in it.
            initial_funding (float):
            equity (float): Latest recorded equity — see `equityKind`.
            realised_pnl (float): Sum of the PnL of the closed trades.
            trades (int): Closed trades.
            gaps (int): Times open positions were lost because the run was restarted with them open.
            open_positions (list[LivePaperPosition]):
            instrument (str | Unset): With `accounts: instrument`, the instrument the account is: `currency` is then its
                quote and several accounts can share it. Absent for the shared account of a currency. Such an account has no
                `instruments`, since it already is one instrument: its `unrealisedPnl` and `totalPnl` are that instrument's own.
                Its `initialFunding` is its own: never add it to another account's. Example: BTC/USDT.
            equity_at_ms (int | Unset): Market time of that value. Absent while the account holds its starting capital.
            equity_kind (LivePaperAccountEquityKind | Unset): `equity` at a closed trade, `mark` at a periodic mark-to-
                market (includes open positions at market price).
            unrealised_pnl (float | Unset): What its open positions are worth over their cost as of the last mark, in the
                account's currency: the sum of `unrealisedPnl` over `openPositions`. `0` when it holds nothing. Absent while any
                of its positions has no current mark (see `openPositions`).
            total_pnl (float | Unset): `realisedPnl` plus `unrealisedPnl`. Absent when `unrealisedPnl` is.
            kpi (LivePaperKpi | Unset): The same KPIs a backtest reports, over the trades closed so far. Absent until the
                first closed trade is recorded.
            instruments (list[LivePaperInstrument] | Unset): Only for the shared account of a currency. What the account
                realised per instrument: one entry for every instrument that has closed a trade or holds a position now, in
                instrument order. Exact for what was realised, and not how the instrument would have done on its own, since its
                entries depended on what the others had locked from the same account. The instruments' `realisedPnl` add up to
                the account's.
    """

    currency: str
    initial_funding: float
    equity: float
    realised_pnl: float
    trades: int
    gaps: int
    open_positions: list[LivePaperPosition]
    instrument: str | Unset = UNSET
    equity_at_ms: int | Unset = UNSET
    equity_kind: LivePaperAccountEquityKind | Unset = UNSET
    unrealised_pnl: float | Unset = UNSET
    total_pnl: float | Unset = UNSET
    kpi: LivePaperKpi | Unset = UNSET
    instruments: list[LivePaperInstrument] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        initial_funding = self.initial_funding

        equity = self.equity

        realised_pnl = self.realised_pnl

        trades = self.trades

        gaps = self.gaps

        open_positions = []
        for open_positions_item_data in self.open_positions:
            open_positions_item = open_positions_item_data.to_dict()
            open_positions.append(open_positions_item)

        instrument = self.instrument

        equity_at_ms = self.equity_at_ms

        equity_kind: str | Unset = UNSET
        if not isinstance(self.equity_kind, Unset):
            equity_kind = self.equity_kind.value

        unrealised_pnl = self.unrealised_pnl

        total_pnl = self.total_pnl

        kpi: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kpi, Unset):
            kpi = self.kpi.to_dict()

        instruments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.instruments, Unset):
            instruments = []
            for instruments_item_data in self.instruments:
                instruments_item = instruments_item_data.to_dict()
                instruments.append(instruments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "initialFunding": initial_funding,
                "equity": equity,
                "realisedPnl": realised_pnl,
                "trades": trades,
                "gaps": gaps,
                "openPositions": open_positions,
            }
        )
        if instrument is not UNSET:
            field_dict["instrument"] = instrument
        if equity_at_ms is not UNSET:
            field_dict["equityAtMs"] = equity_at_ms
        if equity_kind is not UNSET:
            field_dict["equityKind"] = equity_kind
        if unrealised_pnl is not UNSET:
            field_dict["unrealisedPnl"] = unrealised_pnl
        if total_pnl is not UNSET:
            field_dict["totalPnl"] = total_pnl
        if kpi is not UNSET:
            field_dict["kpi"] = kpi
        if instruments is not UNSET:
            field_dict["instruments"] = instruments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.live_paper_instrument import LivePaperInstrument
        from ..models.live_paper_kpi import LivePaperKpi
        from ..models.live_paper_position import LivePaperPosition

        d = dict(src_dict)
        currency = d.pop("currency")

        initial_funding = d.pop("initialFunding")

        equity = d.pop("equity")

        realised_pnl = d.pop("realisedPnl")

        trades = d.pop("trades")

        gaps = d.pop("gaps")

        open_positions = []
        _open_positions = d.pop("openPositions")
        for open_positions_item_data in _open_positions:
            open_positions_item = LivePaperPosition.from_dict(open_positions_item_data)

            open_positions.append(open_positions_item)

        instrument = d.pop("instrument", UNSET)

        equity_at_ms = d.pop("equityAtMs", UNSET)

        _equity_kind = d.pop("equityKind", UNSET)
        equity_kind: LivePaperAccountEquityKind | Unset
        if isinstance(_equity_kind, Unset):
            equity_kind = UNSET
        else:
            equity_kind = LivePaperAccountEquityKind(_equity_kind)

        unrealised_pnl = d.pop("unrealisedPnl", UNSET)

        total_pnl = d.pop("totalPnl", UNSET)

        _kpi = d.pop("kpi", UNSET)
        kpi: LivePaperKpi | Unset
        if isinstance(_kpi, Unset):
            kpi = UNSET
        else:
            kpi = LivePaperKpi.from_dict(_kpi)

        _instruments = d.pop("instruments", UNSET)
        instruments: list[LivePaperInstrument] | Unset = UNSET
        if _instruments is not UNSET:
            instruments = []
            for instruments_item_data in _instruments:
                instruments_item = LivePaperInstrument.from_dict(instruments_item_data)

                instruments.append(instruments_item)

        live_paper_account = cls(
            currency=currency,
            initial_funding=initial_funding,
            equity=equity,
            realised_pnl=realised_pnl,
            trades=trades,
            gaps=gaps,
            open_positions=open_positions,
            instrument=instrument,
            equity_at_ms=equity_at_ms,
            equity_kind=equity_kind,
            unrealised_pnl=unrealised_pnl,
            total_pnl=total_pnl,
            kpi=kpi,
            instruments=instruments,
        )

        live_paper_account.additional_properties = d
        return live_paper_account

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
