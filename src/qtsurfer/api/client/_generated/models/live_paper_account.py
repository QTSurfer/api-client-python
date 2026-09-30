from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.live_paper_account_equity_kind import LivePaperAccountEquityKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.live_paper_kpi import LivePaperKpi
    from ..models.live_paper_position import LivePaperPosition


T = TypeVar("T", bound="LivePaperAccount")


@_attrs_define
class LivePaperAccount:
    """One simulated account — one per quote currency the run trades.

    Attributes:
        currency (str): The account's quote currency; every amount below is in it.
        initial_funding (float):
        equity (float): Latest recorded equity — see `equityKind`.
        realised_pnl (float): Sum of the PnL of the closed trades.
        trades (int): Closed trades.
        gaps (int): Times open positions were lost because the run was restarted with them open.
        open_positions (list[LivePaperPosition]):
        equity_at_ms (int | Unset): Market time of that value. Absent while the account holds its starting capital.
        equity_kind (LivePaperAccountEquityKind | Unset): `equity` at a closed trade, `mark` at a periodic mark-to-
            market (includes open positions at market price).
        kpi (LivePaperKpi | Unset): The same KPIs a backtest reports, over the trades closed so far. Absent until the
            first closed trade is recorded.
    """

    currency: str
    initial_funding: float
    equity: float
    realised_pnl: float
    trades: int
    gaps: int
    open_positions: list[LivePaperPosition]
    equity_at_ms: int | Unset = UNSET
    equity_kind: LivePaperAccountEquityKind | Unset = UNSET
    kpi: LivePaperKpi | Unset = UNSET
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

        equity_at_ms = self.equity_at_ms

        equity_kind: str | Unset = UNSET
        if not isinstance(self.equity_kind, Unset):
            equity_kind = self.equity_kind.value

        kpi: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kpi, Unset):
            kpi = self.kpi.to_dict()

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
        if equity_at_ms is not UNSET:
            field_dict["equityAtMs"] = equity_at_ms
        if equity_kind is not UNSET:
            field_dict["equityKind"] = equity_kind
        if kpi is not UNSET:
            field_dict["kpi"] = kpi

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        equity_at_ms = d.pop("equityAtMs", UNSET)

        _equity_kind = d.pop("equityKind", UNSET)
        equity_kind: LivePaperAccountEquityKind | Unset
        if isinstance(_equity_kind, Unset):
            equity_kind = UNSET
        else:
            equity_kind = LivePaperAccountEquityKind(_equity_kind)

        _kpi = d.pop("kpi", UNSET)
        kpi: LivePaperKpi | Unset
        if isinstance(_kpi, Unset):
            kpi = UNSET
        else:
            kpi = LivePaperKpi.from_dict(_kpi)

        live_paper_account = cls(
            currency=currency,
            initial_funding=initial_funding,
            equity=equity,
            realised_pnl=realised_pnl,
            trades=trades,
            gaps=gaps,
            open_positions=open_positions,
            equity_at_ms=equity_at_ms,
            equity_kind=equity_kind,
            kpi=kpi,
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
