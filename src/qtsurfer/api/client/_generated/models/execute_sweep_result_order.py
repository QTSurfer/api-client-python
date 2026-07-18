from enum import Enum


class ExecuteSweepResultOrder(str, Enum):
    NATURAL = "natural"
    RANKED = "ranked"

    def __str__(self) -> str:
        return str(self.value)
