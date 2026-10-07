from enum import Enum


class LiveSourceRequestType(str, Enum):
    KLINE = "kline"
    TICKER = "ticker"

    def __str__(self) -> str:
        return str(self.value)
