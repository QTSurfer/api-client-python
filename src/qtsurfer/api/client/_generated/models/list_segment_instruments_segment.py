from enum import Enum


class ListSegmentInstrumentsSegment(str, Enum):
    FUTURES = "futures"
    SPOT = "spot"

    def __str__(self) -> str:
        return str(self.value)
