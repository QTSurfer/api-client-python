from enum import Enum


class LiveSourceType(str, Enum):
    KLINE = "kline"
    TICKER = "ticker"

    def __str__(self) -> str:
        return str(self.value)
