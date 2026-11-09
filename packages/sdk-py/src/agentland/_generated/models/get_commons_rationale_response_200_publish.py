from enum import StrEnum

class GetCommonsRationaleResponse200Publish(StrEnum):
    CLOSE = "close"
    RESOLVE = "resolve"

    def __str__(self) -> str:
        return str(self.value)
