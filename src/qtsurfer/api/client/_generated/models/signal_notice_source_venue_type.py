from enum import Enum


class SignalNoticeSourceVenueType(str, Enum):
    CEX = "cex"
    DEX = "dex"

    def __str__(self) -> str:
        return str(self.value)
