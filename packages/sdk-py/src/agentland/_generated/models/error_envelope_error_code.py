from enum import StrEnum

class ErrorEnvelopeErrorCode(StrEnum):
    CHALLENGE_NOT_OPEN = "challenge_not_open"
    CITATION_NOT_PUBLIC = "citation_not_public"
    CONFLICT = "conflict"
    FORBIDDEN = "forbidden"
    INTERNAL = "internal"
    NOT_FOUND = "not_found"
    QUESTION_CLOSED = "question_closed"
    QUESTION_NOT_CLOSED = "question_not_closed"
    QUESTION_NOT_OPEN = "question_not_open"
    QUOTA_EXCEEDED = "quota_exceeded"
    RATE_LIMITED = "rate_limited"
    UNAUTHORIZED = "unauthorized"
    UNAVAILABLE = "unavailable"
    VALIDATION = "validation"

    def __str__(self) -> str:
        return str(self.value)
