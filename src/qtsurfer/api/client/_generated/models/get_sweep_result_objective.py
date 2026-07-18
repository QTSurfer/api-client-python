from enum import Enum


class GetSweepResultObjective(str, Enum):
    MAXDD = "maxdd"
    PNL = "pnl"
    SHARPE = "sharpe"
    SORTINO = "sortino"

    def __str__(self) -> str:
        return str(self.value)
