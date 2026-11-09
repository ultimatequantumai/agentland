from enum import StrEnum

class ListAgentRationalesResponse200DataItemPublish(StrEnum):
    CLOSE = "close"
    RESOLVE = "resolve"

    def __str__(self) -> str:
        return str(self.value)
