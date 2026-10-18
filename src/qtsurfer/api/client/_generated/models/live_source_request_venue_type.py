from enum import Enum


class LiveSourceRequestVenueType(str, Enum):
    CEX = "cex"
    DEX = "dex"

    def __str__(self) -> str:
        return str(self.value)
