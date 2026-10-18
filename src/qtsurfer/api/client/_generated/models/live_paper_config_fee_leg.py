from enum import Enum


class LivePaperConfigFeeLeg(str, Enum):
    BASE = "BASE"
    QUOTE = "QUOTE"
    RECEIVED = "RECEIVED"

    def __str__(self) -> str:
        return str(self.value)
