from enum import Enum


class SweepSpecRequestSampler(str, Enum):
    GRID = "grid"
    LHS = "lhs"
    RANDOM = "random"

    def __str__(self) -> str:
        return str(self.value)
