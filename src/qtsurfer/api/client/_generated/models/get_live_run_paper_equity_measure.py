from enum import Enum


class GetLiveRunPaperEquityMeasure(str, Enum):
    REALISEDPNL = "realisedPnl"
    TOTALPNL = "totalPnl"

    def __str__(self) -> str:
        return str(self.value)
