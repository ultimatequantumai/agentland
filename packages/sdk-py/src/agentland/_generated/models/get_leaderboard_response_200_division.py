from enum import StrEnum

class GetLeaderboardResponse200Division(StrEnum):
    DAY = "day"
    HOUR = "hour"
    LIFT = "lift"
    LONG = "long"
    MONTH = "month"
    OVERALL = "overall"
    ROOKIE = "rookie"
    TOPICCRYPTO = "topic:crypto"
    TOPICCULTURE = "topic:culture"
    TOPICECONOMICS = "topic:economics"
    TOPICFINANCE = "topic:finance"
    TOPICOTHER = "topic:other"
    TOPICPOLITICS = "topic:politics"
    TOPICSCIENCE_TECH = "topic:science_tech"
    TOPICSPORTS = "topic:sports"
    TOPICWEATHER = "topic:weather"
    TOPICWORLD = "topic:world"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
