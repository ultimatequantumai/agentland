from enum import StrEnum

class ListMyForecastsResponse200DataItemMultiScoreType0BaselineKind(StrEnum):
    CROWD = "crowd"
    MARKET = "market"
    UNIFORM = "uniform"

    def __str__(self) -> str:
        return str(self.value)
