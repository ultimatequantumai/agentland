from enum import StrEnum

class ListMySubmissionsStatus(StrEnum):
    ERROR = "error"
    INVALID = "invalid"
    QUEUED = "queued"
    RUNNING = "running"
    VALID = "valid"

    def __str__(self) -> str:
        return str(self.value)
