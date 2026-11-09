from enum import StrEnum

class GetTransparencyDisputeResponse200ImpactType0PerSeasonItemSeasonStatus(StrEnum):
    ACTIVE = "active"
    FINAL = "final"

    def __str__(self) -> str:
        return str(self.value)
