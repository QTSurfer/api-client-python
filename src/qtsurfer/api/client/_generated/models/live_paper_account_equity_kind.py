from enum import Enum


class LivePaperAccountEquityKind(str, Enum):
    EQUITY = "equity"
    MARK = "mark"

    def __str__(self) -> str:
        return str(self.value)
