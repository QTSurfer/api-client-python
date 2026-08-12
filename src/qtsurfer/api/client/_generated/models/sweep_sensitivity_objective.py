from enum import Enum


class SweepSensitivityObjective(str, Enum):
    MAXDD = "maxdd"
    PNL = "pnl"
    SHARPE = "sharpe"
    SORTINO = "sortino"

    def __str__(self) -> str:
        return str(self.value)
