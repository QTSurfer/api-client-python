from enum import Enum


class GetSegmentInstrumentsSegment(str, Enum):
    FUTURES = "futures"
    SPOT = "spot"

    def __str__(self) -> str:
        return str(self.value)
