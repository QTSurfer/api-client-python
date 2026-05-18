from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.result_map_signals_upload import ResultMapSignalsUpload
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResultMap")


@_attrs_define
class ResultMap:
    """Execution result map. Always includes core fields (hostName, iops, strategyId, instrument). Yield metrics (pnlTotal,
    totalTrades, winRate, etc.) are present when the strategy emitted at least one trade. When signal storage is
    enabled, includes signal fields described below.

        Attributes:
            strategy_id (str): Identifier of the compiled strategy that produced this result Example:
                strategy:00000000-0000-0000-0000-000000000000:ticker:2iyvtenlzh9dabqtxn7nbv.
            instrument (str): The instrument (currency pair) that was backtested Example: BTC/USDT.
            host_name (str | Unset): Identifier of the worker that executed the strategy. Useful when reporting issues so
                support can correlate with logs. Example: executor10.
            iops (float | Unset): Instrument operations per second throughput during execution Example: 123956.53.
            pnl_total (float | Unset): Total profit and loss in the output currency Example: 42.75.
            total_trades (int | Unset): Total number of trades executed by the strategy Example: 156.
            win_rate (float | Unset): Percentage of profitable trades (0-100) Example: 58.33.
            sharpe_ratio (float | Unset): Risk-adjusted return ratio (mean return / standard deviation of returns) Example:
                1.245.
            sortino_ratio (float | Unset): Downside risk-adjusted return ratio (mean return / downside deviation) Example:
                1.872.
            cagr (float | Unset): Compound Annual Growth Rate Example: 0.1534.
            max_drawdown (float | Unset): Maximum absolute drawdown in the output currency Example: 12.5.
            max_drawdown_percent (float | Unset): Maximum percentage drawdown from peak equity Example: 8.75.
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
    pnl_total: float | Unset = UNSET
    total_trades: int | Unset = UNSET
    win_rate: float | Unset = UNSET
    sharpe_ratio: float | Unset = UNSET
    sortino_ratio: float | Unset = UNSET
    cagr: float | Unset = UNSET
    max_drawdown: float | Unset = UNSET
    max_drawdown_percent: float | Unset = UNSET
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

        pnl_total = self.pnl_total

        total_trades = self.total_trades

        win_rate = self.win_rate

        sharpe_ratio = self.sharpe_ratio

        sortino_ratio = self.sortino_ratio

        cagr = self.cagr

        max_drawdown = self.max_drawdown

        max_drawdown_percent = self.max_drawdown_percent

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
        if pnl_total is not UNSET:
            field_dict["pnlTotal"] = pnl_total
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
        d = dict(src_dict)
        strategy_id = d.pop("strategyId")

        instrument = d.pop("instrument")

        host_name = d.pop("hostName", UNSET)

        iops = d.pop("iops", UNSET)

        pnl_total = d.pop("pnlTotal", UNSET)

        total_trades = d.pop("totalTrades", UNSET)

        win_rate = d.pop("winRate", UNSET)

        sharpe_ratio = d.pop("sharpeRatio", UNSET)

        sortino_ratio = d.pop("sortinoRatio", UNSET)

        cagr = d.pop("cagr", UNSET)

        max_drawdown = d.pop("maxDrawdown", UNSET)

        max_drawdown_percent = d.pop("maxDrawdownPercent", UNSET)

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
            pnl_total=pnl_total,
            total_trades=total_trades,
            win_rate=win_rate,
            sharpe_ratio=sharpe_ratio,
            sortino_ratio=sortino_ratio,
            cagr=cagr,
            max_drawdown=max_drawdown,
            max_drawdown_percent=max_drawdown_percent,
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
