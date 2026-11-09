from enum import StrEnum

class SearchTransparencyResponse200DisputesDataItemImpactType0PerSeasonItemSeasonStatus(StrEnum):
    ACTIVE = "active"
    FINAL = "final"

    def __str__(self) -> str:
        return str(self.value)
