from enum import Enum


class DatasetTimestampUnit(str, Enum):
    ISO = "iso"
    MS = "ms"
    S = "s"
    US = "us"

    def __str__(self) -> str:
        return str(self.value)
