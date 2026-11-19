from enum import Enum


class AuthTokenRejectedError(str, Enum):
    INVALID_CREDENTIALS = "invalid_credentials"

    def __str__(self) -> str:
        return str(self.value)
