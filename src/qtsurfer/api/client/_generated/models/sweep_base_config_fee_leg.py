from enum import Enum


class SweepBaseConfigFeeLeg(str, Enum):
    BASE = "BASE"
    QUOTE = "QUOTE"
    RECEIVED = "RECEIVED"

    def __str__(self) -> str:
        return str(self.value)
