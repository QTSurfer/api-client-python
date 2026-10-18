from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.live_paper_config_fee_leg import LivePaperConfigFeeLeg
from ..models.live_paper_config_output import LivePaperConfigOutput
from ..types import UNSET, Unset

T = TypeVar("T", bound="LivePaperConfig")


@_attrs_define
class LivePaperConfig:
    """Paper trading for this run: the same economics as a backtest's `baseConfig` (same fields,
    defaults and limits), plus `output`. An empty object takes every default. Each quote
    currency the run trades gets its own simulated account, opened with `initialFunding` in
    that currency; accounts are never added together. As returned on a run, the block is
    normalised: `feeRate` is resolved into `buyFeeRate`/`sellFeeRate` and defaults are filled
    in.

        Attributes:
            initial_funding (float | Unset): Starting capital of each account, in that account's own quote currency.
                Default: 100.0.
            fee_rate (float | Unset): Fee rate for both sides (0.001 = 0.1%). Accepted on start; returned resolved into the
                two fields below. Default: 0.001.
            buy_fee_rate (float | Unset): Buy-side fee rate; overrides `feeRate`.
            sell_fee_rate (float | Unset): Sell-side fee rate; overrides `feeRate`.
            fee_leg (LivePaperConfigFeeLeg | Unset): Which asset fees are charged in. Case-insensitive on start. Default:
                LivePaperConfigFeeLeg.RECEIVED.
            percent_amount_to_lock (float | Unset): Share of the account's free balance each entry locks, in percent.
                Omitted, the strategy's own setting applies, and without one 10%.
            output (LivePaperConfigOutput | Unset): `separate` keeps paper output out of the run's signals (read it with
                `GET /live/{runId}/paper`); `mix` also interleaves it into the run's signals as `type: paper`, right after the
                signal that caused it. Default: LivePaperConfigOutput.SEPARATE.
    """

    initial_funding: float | Unset = 100.0
    fee_rate: float | Unset = 0.001
    buy_fee_rate: float | Unset = UNSET
    sell_fee_rate: float | Unset = UNSET
    fee_leg: LivePaperConfigFeeLeg | Unset = LivePaperConfigFeeLeg.RECEIVED
    percent_amount_to_lock: float | Unset = UNSET
    output: LivePaperConfigOutput | Unset = LivePaperConfigOutput.SEPARATE

    def to_dict(self) -> dict[str, Any]:
        initial_funding = self.initial_funding

        fee_rate = self.fee_rate

        buy_fee_rate = self.buy_fee_rate

        sell_fee_rate = self.sell_fee_rate

        fee_leg: str | Unset = UNSET
        if not isinstance(self.fee_leg, Unset):
            fee_leg = self.fee_leg.value

        percent_amount_to_lock = self.percent_amount_to_lock

        output: str | Unset = UNSET
        if not isinstance(self.output, Unset):
            output = self.output.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if initial_funding is not UNSET:
            field_dict["initialFunding"] = initial_funding
        if fee_rate is not UNSET:
            field_dict["feeRate"] = fee_rate
        if buy_fee_rate is not UNSET:
            field_dict["buyFeeRate"] = buy_fee_rate
        if sell_fee_rate is not UNSET:
            field_dict["sellFeeRate"] = sell_fee_rate
        if fee_leg is not UNSET:
            field_dict["feeLeg"] = fee_leg
        if percent_amount_to_lock is not UNSET:
            field_dict["percentAmountToLock"] = percent_amount_to_lock
        if output is not UNSET:
            field_dict["output"] = output

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        initial_funding = d.pop("initialFunding", UNSET)

        fee_rate = d.pop("feeRate", UNSET)

        buy_fee_rate = d.pop("buyFeeRate", UNSET)

        sell_fee_rate = d.pop("sellFeeRate", UNSET)

        _fee_leg = d.pop("feeLeg", UNSET)
        fee_leg: LivePaperConfigFeeLeg | Unset
        if isinstance(_fee_leg, Unset):
            fee_leg = UNSET
        else:
            fee_leg = LivePaperConfigFeeLeg(_fee_leg)

        percent_amount_to_lock = d.pop("percentAmountToLock", UNSET)

        _output = d.pop("output", UNSET)
        output: LivePaperConfigOutput | Unset
        if isinstance(_output, Unset):
            output = UNSET
        else:
            output = LivePaperConfigOutput(_output)

        live_paper_config = cls(
            initial_funding=initial_funding,
            fee_rate=fee_rate,
            buy_fee_rate=buy_fee_rate,
            sell_fee_rate=sell_fee_rate,
            fee_leg=fee_leg,
            percent_amount_to_lock=percent_amount_to_lock,
            output=output,
        )

        return live_paper_config
