from enum import Enum


class AuthTokenErrorCode(str, Enum):
    APIKEY_EXPIRED = "apikey_expired"
    APIKEY_REVOKED = "apikey_revoked"
    APIKEY_WITHOUT_SCOPES = "apikey_without_scopes"
    INVALID_APIKEY = "invalid_apikey"

    def __str__(self) -> str:
        return str(self.value)
