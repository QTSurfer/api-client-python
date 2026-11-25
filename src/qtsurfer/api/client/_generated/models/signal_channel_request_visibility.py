from enum import Enum


class SignalChannelRequestVisibility(str, Enum):
    PUBLIC = "public"
    UNLISTED = "unlisted"

    def __str__(self) -> str:
        return str(self.value)
