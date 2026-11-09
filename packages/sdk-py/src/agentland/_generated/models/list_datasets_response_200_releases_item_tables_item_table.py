from enum import StrEnum

class ListDatasetsResponse200ReleasesItemTablesItemTable(StrEnum):
    FINAL_FORECASTS = "final_forecasts"
    QUESTIONS = "questions"
    SCORES = "scores"
    SNAPSHOTS = "snapshots"

    def __str__(self) -> str:
        return str(self.value)
