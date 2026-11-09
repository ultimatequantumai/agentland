from enum import StrEnum

class ListSimilarLedgerResponse200DataItemBaselineKind(StrEnum):
    COMMUNITY = "community"
    CROWD = "crowd"
    MARKET = "market"
    UNIFORM = "uniform"

    def __str__(self) -> str:
        return str(self.value)
