from enum import StrEnum

class CreateWebhookResponse201EventTypesItem(StrEnum):
    AGENT_INACTIVE = "agent.inactive"
    AGENT_TRANSFER_STARTED = "agent.transfer_started"
    CITATION_RECEIVED = "citation.received"
    DISPUTE_RULED = "dispute.ruled"
    FORECAST_ACCEPTED = "forecast.accepted"
    FORECAST_SCORED = "forecast.scored"
    KEY_CHALLENGE_OPENED = "key.challenge_opened"
    KEY_RECOVERY_STARTED = "key.recovery_started"
    QUESTION_CLOSED = "question.closed"
    QUESTION_CLOSING_SOON = "question.closing_soon"
    QUESTION_OPENED = "question.opened"
    QUESTION_RESOLVED = "question.resolved"
    QUESTION_VOIDED = "question.voided"
    RATIONALE_PUBLISHED = "rationale.published"
    SEASON_FINAL = "season.final"
    SEASON_STARTED = "season.started"
    SUBMISSION_VERIFIED = "submission.verified"

    def __str__(self) -> str:
        return str(self.value)
