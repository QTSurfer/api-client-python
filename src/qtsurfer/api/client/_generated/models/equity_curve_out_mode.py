from enum import Enum


class EquityCurveOutMode(str, Enum):
    ARRAY = "ARRAY"
    SHORT = "SHORT"

    def __str__(self) -> str:
        return str(self.value)
