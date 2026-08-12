from enum import Enum


class ExecuteSweepResultRanking(str, Enum):
    PLATEAU = "plateau"
    RAW = "raw"

    def __str__(self) -> str:
        return str(self.value)
