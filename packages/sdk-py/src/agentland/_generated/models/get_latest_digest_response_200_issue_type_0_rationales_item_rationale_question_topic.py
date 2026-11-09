from enum import StrEnum

class GetLatestDigestResponse200IssueType0RationalesItemRationaleQuestionTopic(StrEnum):
    CRYPTO = "crypto"
    CULTURE = "culture"
    ECONOMICS = "economics"
    FINANCE = "finance"
    OTHER = "other"
    POLITICS = "politics"
    SCIENCE_TECH = "science_tech"
    SPORTS = "sports"
    WEATHER = "weather"
    WORLD = "world"

    def __str__(self) -> str:
        return str(self.value)
