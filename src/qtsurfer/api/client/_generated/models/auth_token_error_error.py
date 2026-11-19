from enum import Enum


class AuthTokenErrorError(str, Enum):
    APIKEY_WITHOUT_SCOPES = "apikey_without_scopes"

    def __str__(self) -> str:
        return str(self.value)
