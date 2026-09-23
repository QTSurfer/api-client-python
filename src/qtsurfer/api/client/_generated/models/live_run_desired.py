from enum import Enum


class LiveRunDesired(str, Enum):
    RUNNING = "RUNNING"
    STOPPED = "STOPPED"

    def __str__(self) -> str:
        return str(self.value)
