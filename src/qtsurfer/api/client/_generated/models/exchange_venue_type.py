from enum import Enum


class ExchangeVenueType(str, Enum):
    CEX = "cex"
    DEX = "dex"

    def __str__(self) -> str:
        return str(self.value)
