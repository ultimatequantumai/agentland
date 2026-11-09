from enum import StrEnum

class GetSeasonReportResponse200ByHorizonItemHorizon(StrEnum):
    DAY = "day"
    HOUR = "hour"
    LONG = "long"
    MONTH = "month"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
