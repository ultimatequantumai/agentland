from enum import StrEnum

class ListCommonsRationalesResponse200DataItemPublish(StrEnum):
    CLOSE = "close"
    RESOLVE = "resolve"

    def __str__(self) -> str:
        return str(self.value)
