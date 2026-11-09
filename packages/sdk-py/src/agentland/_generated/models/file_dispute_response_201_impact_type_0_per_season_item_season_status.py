from enum import StrEnum

class FileDisputeResponse201ImpactType0PerSeasonItemSeasonStatus(StrEnum):
    ACTIVE = "active"
    FINAL = "final"

    def __str__(self) -> str:
        return str(self.value)
