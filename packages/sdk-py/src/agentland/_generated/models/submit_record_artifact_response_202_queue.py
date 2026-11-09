from enum import StrEnum

class SubmitRecordArtifactResponse202Queue(StrEnum):
    LAB = "lab"
    PRIORITY = "priority"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
