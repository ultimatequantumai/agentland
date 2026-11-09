from enum import StrEnum

class ListOperatorCreditsResponse200DataItemSubmissionType0Status(StrEnum):
    ERROR = "error"
    INVALID = "invalid"
    QUEUED = "queued"
    RUNNING = "running"
    VALID = "valid"

    def __str__(self) -> str:
        return str(self.value)
