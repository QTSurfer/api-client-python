from enum import Enum


class ValidateStrategyResponse202Validation(str, Enum):
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
