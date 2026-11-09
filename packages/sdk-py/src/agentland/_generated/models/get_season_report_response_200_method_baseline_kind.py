from enum import StrEnum

class GetSeasonReportResponse200MethodBaselineKind(StrEnum):
    MARKET = "market"

    def __str__(self) -> str:
        return str(self.value)
