from enum import StrEnum

class ListMySubmissionsResponse200DataItemStatus(StrEnum):
    ERROR = "error"
    INVALID = "invalid"
    QUEUED = "queued"
    RUNNING = "running"
    VALID = "valid"

    def __str__(self) -> str:
        return str(self.value)
