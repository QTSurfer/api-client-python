from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.result_map_signals_upload import ResultMapSignalsUpload
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.equity_curve_result import EquityCurveResult
    from ..models.notice import Notice
    from ..models.result_map_params import ResultMapParams


T = TypeVar("T", bound="ResultMap")


@_attrs_define
class ResultMap:
    """Execution result map. Always includes core fields (hostName, iops, strategyId, instrument). Yield metrics (pnlTotal,
    pnlTotalPercent, totalTrades, winRate, equityCurve, etc.) are present when the strategy emitted at least one trade.
    When signal storage is enabled, includes signal fields described below. `notices` carries what the run had to say
    about itself, and is absent when it had nothing.

        Attributes:
            strategy_id (str): **Not the `strategyId` you compiled with** — this is the execution context id,
                `strategy:<user>:<strategyId>`. The compiled strategy's id is the last `:`-separated
                segment; that, not this whole string, is what `GET /strategy/{strategyId}` takes.

                Take the segment after the last `:` rather than counting from the front: the shape has
                changed once already and callers that indexed a fixed position broke on it.
                 Example: strategy:00000000-0000-0000-0000-000000000000:2iyvtenlzh9dabqtxn7nbv.
            instrument (str): The instrument (currency pair) that was backtested Example: BTC/USDT.
            host_name (str | Unset): Identifier of the worker that executed the strategy. Useful when reporting issues so
                support can correlate with logs. Example: executor10.
            iops (float | Unset): Instrument operations per second throughput during execution Example: 123956.53.
            notices (list[Notice] | Unset): Diagnostics the engine raised over this run, each with `provenance: execute`.

                **Absent means nothing was raised.** This is the one surface where silence is a real
                answer: the run happened, over your data, start to finish, and the engine found nothing
                worth saying. That is not true of the compile path, where an empty list only means a
                short synthetic series reached nothing — see `GET /strategy/{strategyId}`.

                Notices are raised on failed and aborted runs too, and those are the ones most worth
                reading: a run that produced no trades often did so for a reason stated here.
            notices_truncated (int | Unset): How many notices were dropped past the cap of 50. Absent when none were. A
                large value usually means one fault repeating per instrument or per parameter vector rather than 50 distinct
                problems. Example: 3.
            pnl_total (float | Unset): Total profit and loss in the output currency Example: 42.75.
            pnl_total_percent (float | Unset): Total PnL as a percentage of the initial capital (`backtestFunding`). Zero
                when `backtestFunding` is 0. Example: 42.75.
            total_trades (int | Unset): Total number of trades executed by the strategy Example: 156.
            win_rate (float | Unset): Fraction of profitable trades, 0.0-1.0 (a rate, not a percent — multiply by 100 to
                display as one). Zero when `totalTrades` is 0. Example: 0.5833.
            sharpe_ratio (float | Unset): Risk-adjusted return ratio (mean return / standard deviation of returns) Example:
                1.245.
            sortino_ratio (float | Unset): Downside risk-adjusted return ratio (mean return / downside deviation) Example:
                1.872.
            cagr (float | Unset): Compound Annual Growth Rate (eg. 0.15 for 15%) Example: 0.1534.
            max_drawdown (float | Unset): Maximum absolute drawdown in the output currency Example: 12.5.
            max_drawdown_percent (float | Unset): Maximum percentage drawdown from peak equity Example: 8.75.
            equity_curve (EquityCurveResult | Unset): An equity curve, shaped per `meta.outMode`: `points` when `ARRAY`,
                `timestamps` + `equities` (parallel arrays) when `SHORT`. Used identically wherever a curve is returned — a
                plain backtest's inline `equityCurve` and a sweep row's `equityCurve` are the same type. `url` is present
                *instead of* any points when the curve is served by pointer rather than inline (a sweep row's top-N winners
                only): `GET` it separately to fetch this exact same shape with the points populated.
            params (ResultMapParams | Unset): The strategy properties this run was given, echoed back as sent. Absent when
                the request carried none, so its presence is what distinguishes a parameterised run from one at the declared
                defaults — a stored result cannot otherwise say which vector produced it, and this endpoint is meant to be
                called repeatedly over one prepare. Example: {'ema.fast.period': 9, 'ema.slow.period': 21}.
            signal_count (int | Unset): Number of signals emitted during strategy execution Example: 100000.
            signals_id (str | Unset): Storage key for the signals file. Treat as opaque; use signalsUrl to download.
                Example: 00000000-0000-0000-0000-000000000000/exec/binance/3vsndwikcuaatjmb83fjtl.
            signals_url (str | Unset): HTTPS URL to download the signals Parquet file. Use signalsUpload to know when it's
                ready. Example:
                https://storage.qtsurfer.com/00000000-0000-0000-0000-000000000000/exec/binance/3vsndwikcuaatjmb83fjtl.parquet.
            signals_upload (ResultMapSignalsUpload | Unset): Upload status. Done = signal file is available at signalsUrl.
                Failed = upload error (see signalsUploadReason). Skipped = no signals emitted. Example: Done.
            signals_uploaded_at (datetime.datetime | Unset): ISO 8601 timestamp of when the upload completed. Only present
                when signalsUpload is Done. Example: 2026-03-18T13:21:48.170Z.
            signals_upload_reason (str | Unset): Human-readable reason when signalsUpload is Failed or Skipped. Example:
                signal file generation failed.
    """

    strategy_id: str
    instrument: str
    host_name: str | Unset = UNSET
    iops: float | Unset = UNSET
    notices: list[Notice] | Unset = UNSET
    notices_truncated: int | Unset = UNSET
    pnl_total: float | Unset = UNSET
    pnl_total_percent: float | Unset = UNSET
    total_trades: int | Unset = UNSET
    win_rate: float | Unset = UNSET
    sharpe_ratio: float | Unset = UNSET
    sortino_ratio: float | Unset = UNSET
    cagr: float | Unset = UNSET
    max_drawdown: float | Unset = UNSET
    max_drawdown_percent: float | Unset = UNSET
    equity_curve: EquityCurveResult | Unset = UNSET
    params: ResultMapParams | Unset = UNSET
    signal_count: int | Unset = UNSET
    signals_id: str | Unset = UNSET
    signals_url: str | Unset = UNSET
    signals_upload: ResultMapSignalsUpload | Unset = UNSET
    signals_uploaded_at: datetime.datetime | Unset = UNSET
    signals_upload_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategy_id = self.strategy_id

        instrument = self.instrument

        host_name = self.host_name

        iops = self.iops

        notices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.notices, Unset):
            notices = []
            for notices_item_data in self.notices:
                notices_item = notices_item_data.to_dict()
                notices.append(notices_item)

        notices_truncated = self.notices_truncated

        pnl_total = self.pnl_total

        pnl_total_percent = self.pnl_total_percent

        total_trades = self.total_trades

        win_rate = self.win_rate

        sharpe_ratio = self.sharpe_ratio

        sortino_ratio = self.sortino_ratio

        cagr = self.cagr

        max_drawdown = self.max_drawdown

        max_drawdown_percent = self.max_drawdown_percent

        equity_curve: dict[str, Any] | Unset = UNSET
        if not isinstance(self.equity_curve, Unset):
            equity_curve = self.equity_curve.to_dict()

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        signal_count = self.signal_count

        signals_id = self.signals_id

        signals_url = self.signals_url

        signals_upload: str | Unset = UNSET
        if not isinstance(self.signals_upload, Unset):
            signals_upload = self.signals_upload.value

        signals_uploaded_at: str | Unset = UNSET
        if not isinstance(self.signals_uploaded_at, Unset):
            signals_uploaded_at = self.signals_uploaded_at.isoformat()

        signals_upload_reason = self.signals_upload_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategyId": strategy_id,
                "instrument": instrument,
            }
        )
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if iops is not UNSET:
            field_dict["iops"] = iops
        if notices is not UNSET:
            field_dict["notices"] = notices
        if notices_truncated is not UNSET:
            field_dict["noticesTruncated"] = notices_truncated
        if pnl_total is not UNSET:
            field_dict["pnlTotal"] = pnl_total
        if pnl_total_percent is not UNSET:
            field_dict["pnlTotalPercent"] = pnl_total_percent
        if total_trades is not UNSET:
            field_dict["totalTrades"] = total_trades
        if win_rate is not UNSET:
            field_dict["winRate"] = win_rate
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
        if equity_curve is not UNSET:
            field_dict["equityCurve"] = equity_curve
        if params is not UNSET:
            field_dict["params"] = params
        if signal_count is not UNSET:
            field_dict["signalCount"] = signal_count
        if signals_id is not UNSET:
            field_dict["signalsId"] = signals_id
        if signals_url is not UNSET:
            field_dict["signalsUrl"] = signals_url
        if signals_upload is not UNSET:
            field_dict["signalsUpload"] = signals_upload
        if signals_uploaded_at is not UNSET:
            field_dict["signalsUploadedAt"] = signals_uploaded_at
        if signals_upload_reason is not UNSET:
            field_dict["signalsUploadReason"] = signals_upload_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.equity_curve_result import EquityCurveResult
        from ..models.notice import Notice
        from ..models.result_map_params import ResultMapParams

        d = dict(src_dict)
        strategy_id = d.pop("strategyId")

        instrument = d.pop("instrument")

        host_name = d.pop("hostName", UNSET)

        iops = d.pop("iops", UNSET)

        _notices = d.pop("notices", UNSET)
        notices: list[Notice] | Unset = UNSET
        if _notices is not UNSET:
            notices = []
            for notices_item_data in _notices:
                notices_item = Notice.from_dict(notices_item_data)

                notices.append(notices_item)

        notices_truncated = d.pop("noticesTruncated", UNSET)

        pnl_total = d.pop("pnlTotal", UNSET)

        pnl_total_percent = d.pop("pnlTotalPercent", UNSET)

        total_trades = d.pop("totalTrades", UNSET)

        win_rate = d.pop("winRate", UNSET)

        sharpe_ratio = d.pop("sharpeRatio", UNSET)

        sortino_ratio = d.pop("sortinoRatio", UNSET)

        cagr = d.pop("cagr", UNSET)

        max_drawdown = d.pop("maxDrawdown", UNSET)

        max_drawdown_percent = d.pop("maxDrawdownPercent", UNSET)

        _equity_curve = d.pop("equityCurve", UNSET)
        equity_curve: EquityCurveResult | Unset
        if isinstance(_equity_curve, Unset):
            equity_curve = UNSET
        else:
            equity_curve = EquityCurveResult.from_dict(_equity_curve)

        _params = d.pop("params", UNSET)
        params: ResultMapParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = ResultMapParams.from_dict(_params)

        signal_count = d.pop("signalCount", UNSET)

        signals_id = d.pop("signalsId", UNSET)

        signals_url = d.pop("signalsUrl", UNSET)

        _signals_upload = d.pop("signalsUpload", UNSET)
        signals_upload: ResultMapSignalsUpload | Unset
        if isinstance(_signals_upload, Unset):
            signals_upload = UNSET
        else:
            signals_upload = ResultMapSignalsUpload(_signals_upload)

        _signals_uploaded_at = d.pop("signalsUploadedAt", UNSET)
        signals_uploaded_at: datetime.datetime | Unset
        if isinstance(_signals_uploaded_at, Unset):
            signals_uploaded_at = UNSET
        else:
            signals_uploaded_at = isoparse(_signals_uploaded_at)

        signals_upload_reason = d.pop("signalsUploadReason", UNSET)

        result_map = cls(
            strategy_id=strategy_id,
            instrument=instrument,
            host_name=host_name,
            iops=iops,
            notices=notices,
            notices_truncated=notices_truncated,
            pnl_total=pnl_total,
            pnl_total_percent=pnl_total_percent,
            total_trades=total_trades,
            win_rate=win_rate,
            sharpe_ratio=sharpe_ratio,
            sortino_ratio=sortino_ratio,
            cagr=cagr,
            max_drawdown=max_drawdown,
            max_drawdown_percent=max_drawdown_percent,
            equity_curve=equity_curve,
            params=params,
            signal_count=signal_count,
            signals_id=signals_id,
            signals_url=signals_url,
            signals_upload=signals_upload,
            signals_uploaded_at=signals_uploaded_at,
            signals_upload_reason=signals_upload_reason,
        )

        result_map.additional_properties = d
        return result_map

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
