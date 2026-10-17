from enum import Enum


class ErrorNextCallMethod(str, Enum):
    DELETE = "DELETE"
    GET = "GET"
    POST = "POST"
    PUT = "PUT"

    def __str__(self) -> str:
        return str(self.value)
