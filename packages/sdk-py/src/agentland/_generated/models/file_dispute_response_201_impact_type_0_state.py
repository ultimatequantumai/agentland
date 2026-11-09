from enum import StrEnum

class FileDisputeResponse201ImpactType0State(StrEnum):
    ACTIVE_CORRECTION_APPLIED = "active_correction_applied"
    CORRECTION_SCORING_PENDING = "correction_scoring_pending"
    HISTORICAL_SEASON_FROZEN = "historical_season_frozen"
    NO_CHANGE = "no_change"
    QUESTION_VOIDED = "question_voided"

    def __str__(self) -> str:
        return str(self.value)
