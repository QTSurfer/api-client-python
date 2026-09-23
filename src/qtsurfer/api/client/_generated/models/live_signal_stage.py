from enum import Enum


class LiveSignalStage(str, Enum):
    LIVE = "live"
    SANDBOX = "sandbox"

    def __str__(self) -> str:
        return str(self.value)
