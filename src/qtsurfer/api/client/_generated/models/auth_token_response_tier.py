from enum import Enum


class AuthTokenResponseTier(str, Enum):
    BASIC = "basic"
    ELITE = "elite"
    FREE = "free"
    PRO = "pro"

    def __str__(self) -> str:
        return str(self.value)
