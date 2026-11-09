from enum import StrEnum

class SearchTransparencyResponse200SourcesDataItemState(StrEnum):
    DISABLED = "disabled"
    DISABLED_BY_POLICYLINK_RULE_PENDING = "disabled_by_policy:link_rule_pending"
    ENABLED = "enabled"

    def __str__(self) -> str:
        return str(self.value)
