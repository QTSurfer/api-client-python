from enum import Enum


class LivePaperConfigOutput(str, Enum):
    MIX = "mix"
    SEPARATE = "separate"

    def __str__(self) -> str:
        return str(self.value)
