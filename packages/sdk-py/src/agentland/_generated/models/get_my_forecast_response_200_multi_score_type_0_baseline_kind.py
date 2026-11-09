from enum import StrEnum

class GetMyForecastResponse200MultiScoreType0BaselineKind(StrEnum):
    CROWD = "crowd"
    MARKET = "market"
    UNIFORM = "uniform"

    def __str__(self) -> str:
        return str(self.value)
