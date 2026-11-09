from enum import StrEnum

class ListTransparencyDisputesResponse200DataItemImpactType0PerSeasonItemSeasonStatus(StrEnum):
    ACTIVE = "active"
    FINAL = "final"

    def __str__(self) -> str:
        return str(self.value)
