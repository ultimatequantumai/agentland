from enum import StrEnum

class DownloadDatasetFile(StrEnum):
    FINAL_FORECASTS_PARQUET = "final_forecasts.parquet"
    QUESTIONS_PARQUET = "questions.parquet"
    SCORES_PARQUET = "scores.parquet"
    SNAPSHOTS_PARQUET = "snapshots.parquet"

    def __str__(self) -> str:
        return str(self.value)
