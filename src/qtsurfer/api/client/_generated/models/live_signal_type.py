from enum import Enum


class LiveSignalType(str, Enum):
    COMMAND = "command"
    HINT = "hint"
    INFO = "info"
    MARKER = "marker"

    def __str__(self) -> str:
        return str(self.value)
