from enum import Enum


class InstrumentListMetaSegment(str, Enum):
    FUTURES = "futures"
    SPOT = "spot"

    def __str__(self) -> str:
        return str(self.value)
