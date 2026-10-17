from enum import Enum


class InstrumentListMetaVenueType(str, Enum):
    CEX = "cex"

    def __str__(self) -> str:
        return str(self.value)
