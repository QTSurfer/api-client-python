from enum import Enum


class LivePaperEquityPointKind(str, Enum):
    EQUITY = "equity"
    GAP = "gap"
    MARK = "mark"

    def __str__(self) -> str:
        return str(self.value)
