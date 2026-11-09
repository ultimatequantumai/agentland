from enum import StrEnum

class GetMySubmissionResponse200Queue(StrEnum):
    LAB = "lab"
    PRIORITY = "priority"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
