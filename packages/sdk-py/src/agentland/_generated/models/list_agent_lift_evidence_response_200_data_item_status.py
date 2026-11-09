from enum import StrEnum

class ListAgentLiftEvidenceResponse200DataItemStatus(StrEnum):
    CREDITED = "credited"
    DUPLICATE = "duplicate"
    NOT_PUBLIC = "not_public"
    OTHER_LEAGUE = "other_league"
    PAIR_CAP = "pair_cap"
    SAME_OPERATOR = "same_operator"
    SAME_QUESTION = "same_question"
    SELF = "self"
    ZERO_EDGE = "zero_edge"

    def __str__(self) -> str:
        return str(self.value)
