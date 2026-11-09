from enum import StrEnum

class ListMyForecastsResponse200DataItemScoreType0BaselineKind(StrEnum):
    COMMUNITY = "community"
    CROWD = "crowd"
    MARKET = "market"
    UNIFORM = "uniform"

    def __str__(self) -> str:
        return str(self.value)
