from enum import Enum


class EquityCurveRequestMode(str, Enum):
    AUTO = "auto"
    NONE = "none"
    TOPN = "topN"
    TOPPCT = "topPct"

    def __str__(self) -> str:
        return str(self.value)
