from enum import StrEnum

class ListLedgerResponse200DataItemBaselineKind(StrEnum):
    COMMUNITY = "community"
    CROWD = "crowd"
    MARKET = "market"
    UNIFORM = "uniform"

    def __str__(self) -> str:
        return str(self.value)
