from enum import StrEnum

class GetMyForecastResponse200NumericScoreType0BaselineKind(StrEnum):
    CROWD = "crowd"
    UNIFORM = "uniform"

    def __str__(self) -> str:
        return str(self.value)
