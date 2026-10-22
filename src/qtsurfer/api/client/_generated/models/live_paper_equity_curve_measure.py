from enum import Enum


class LivePaperEquityCurveMeasure(str, Enum):
    EQUITY = "equity"
    REALISEDPNL = "realisedPnl"
    TOTALPNL = "totalPnl"

    def __str__(self) -> str:
        return str(self.value)
