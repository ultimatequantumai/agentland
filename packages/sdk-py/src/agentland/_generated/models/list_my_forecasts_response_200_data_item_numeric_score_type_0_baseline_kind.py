from enum import StrEnum

class ListMyForecastsResponse200DataItemNumericScoreType0BaselineKind(StrEnum):
    CROWD = "crowd"
    UNIFORM = "uniform"

    def __str__(self) -> str:
        return str(self.value)
