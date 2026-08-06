from enum import Enum


class StrategyStateValidation(str, Enum):
    FAILED = "failed"
    NOT_VALIDATED = "not_validated"
    PASSED = "passed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
