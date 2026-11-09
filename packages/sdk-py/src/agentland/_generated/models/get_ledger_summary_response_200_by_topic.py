from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_ledger_summary_response_200_by_topic_crypto import GetLedgerSummaryResponse200ByTopicCrypto
  from ..models.get_ledger_summary_response_200_by_topic_culture import GetLedgerSummaryResponse200ByTopicCulture
  from ..models.get_ledger_summary_response_200_by_topic_economics import GetLedgerSummaryResponse200ByTopicEconomics
  from ..models.get_ledger_summary_response_200_by_topic_finance import GetLedgerSummaryResponse200ByTopicFinance
  from ..models.get_ledger_summary_response_200_by_topic_other import GetLedgerSummaryResponse200ByTopicOther
  from ..models.get_ledger_summary_response_200_by_topic_politics import GetLedgerSummaryResponse200ByTopicPolitics
  from ..models.get_ledger_summary_response_200_by_topic_science_tech import GetLedgerSummaryResponse200ByTopicScienceTech
  from ..models.get_ledger_summary_response_200_by_topic_sports import GetLedgerSummaryResponse200ByTopicSports
  from ..models.get_ledger_summary_response_200_by_topic_weather import GetLedgerSummaryResponse200ByTopicWeather
  from ..models.get_ledger_summary_response_200_by_topic_world import GetLedgerSummaryResponse200ByTopicWorld





T = TypeVar("T", bound="GetLedgerSummaryResponse200ByTopic")



@_attrs_define
class GetLedgerSummaryResponse200ByTopic:
    """ 
        Attributes:
            finance (GetLedgerSummaryResponse200ByTopicFinance | Unset):
            crypto (GetLedgerSummaryResponse200ByTopicCrypto | Unset):
            weather (GetLedgerSummaryResponse200ByTopicWeather | Unset):
            sports (GetLedgerSummaryResponse200ByTopicSports | Unset):
            politics (GetLedgerSummaryResponse200ByTopicPolitics | Unset):
            economics (GetLedgerSummaryResponse200ByTopicEconomics | Unset):
            science_tech (GetLedgerSummaryResponse200ByTopicScienceTech | Unset):
            culture (GetLedgerSummaryResponse200ByTopicCulture | Unset):
            world (GetLedgerSummaryResponse200ByTopicWorld | Unset):
            other (GetLedgerSummaryResponse200ByTopicOther | Unset):
     """

    finance: GetLedgerSummaryResponse200ByTopicFinance | Unset = UNSET
    crypto: GetLedgerSummaryResponse200ByTopicCrypto | Unset = UNSET
    weather: GetLedgerSummaryResponse200ByTopicWeather | Unset = UNSET
    sports: GetLedgerSummaryResponse200ByTopicSports | Unset = UNSET
    politics: GetLedgerSummaryResponse200ByTopicPolitics | Unset = UNSET
    economics: GetLedgerSummaryResponse200ByTopicEconomics | Unset = UNSET
    science_tech: GetLedgerSummaryResponse200ByTopicScienceTech | Unset = UNSET
    culture: GetLedgerSummaryResponse200ByTopicCulture | Unset = UNSET
    world: GetLedgerSummaryResponse200ByTopicWorld | Unset = UNSET
    other: GetLedgerSummaryResponse200ByTopicOther | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_ledger_summary_response_200_by_topic_crypto import GetLedgerSummaryResponse200ByTopicCrypto # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic_culture import GetLedgerSummaryResponse200ByTopicCulture # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic_economics import GetLedgerSummaryResponse200ByTopicEconomics # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic_finance import GetLedgerSummaryResponse200ByTopicFinance # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic_other import GetLedgerSummaryResponse200ByTopicOther # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic_politics import GetLedgerSummaryResponse200ByTopicPolitics # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic_science_tech import GetLedgerSummaryResponse200ByTopicScienceTech # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic_sports import GetLedgerSummaryResponse200ByTopicSports # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic_weather import GetLedgerSummaryResponse200ByTopicWeather # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic_world import GetLedgerSummaryResponse200ByTopicWorld # noqa: PLC0415
        finance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.finance, Unset):
            finance = self.finance.to_dict()

        crypto: dict[str, Any] | Unset = UNSET
        if not isinstance(self.crypto, Unset):
            crypto = self.crypto.to_dict()

        weather: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weather, Unset):
            weather = self.weather.to_dict()

        sports: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sports, Unset):
            sports = self.sports.to_dict()

        politics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.politics, Unset):
            politics = self.politics.to_dict()

        economics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.economics, Unset):
            economics = self.economics.to_dict()

        science_tech: dict[str, Any] | Unset = UNSET
        if not isinstance(self.science_tech, Unset):
            science_tech = self.science_tech.to_dict()

        culture: dict[str, Any] | Unset = UNSET
        if not isinstance(self.culture, Unset):
            culture = self.culture.to_dict()

        world: dict[str, Any] | Unset = UNSET
        if not isinstance(self.world, Unset):
            world = self.world.to_dict()

        other: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other, Unset):
            other = self.other.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if finance is not UNSET:
            field_dict["finance"] = finance
        if crypto is not UNSET:
            field_dict["crypto"] = crypto
        if weather is not UNSET:
            field_dict["weather"] = weather
        if sports is not UNSET:
            field_dict["sports"] = sports
        if politics is not UNSET:
            field_dict["politics"] = politics
        if economics is not UNSET:
            field_dict["economics"] = economics
        if science_tech is not UNSET:
            field_dict["science_tech"] = science_tech
        if culture is not UNSET:
            field_dict["culture"] = culture
        if world is not UNSET:
            field_dict["world"] = world
        if other is not UNSET:
            field_dict["other"] = other

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_ledger_summary_response_200_by_topic_crypto import GetLedgerSummaryResponse200ByTopicCrypto # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic_culture import GetLedgerSummaryResponse200ByTopicCulture # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic_economics import GetLedgerSummaryResponse200ByTopicEconomics # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic_finance import GetLedgerSummaryResponse200ByTopicFinance # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic_other import GetLedgerSummaryResponse200ByTopicOther # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic_politics import GetLedgerSummaryResponse200ByTopicPolitics # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic_science_tech import GetLedgerSummaryResponse200ByTopicScienceTech # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic_sports import GetLedgerSummaryResponse200ByTopicSports # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic_weather import GetLedgerSummaryResponse200ByTopicWeather # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic_world import GetLedgerSummaryResponse200ByTopicWorld # noqa: PLC0415
        d = dict(src_dict)
        _finance = d.pop("finance", UNSET)
        finance: GetLedgerSummaryResponse200ByTopicFinance | Unset
        if isinstance(_finance,  Unset):
            finance = UNSET
        else:
            finance = GetLedgerSummaryResponse200ByTopicFinance.from_dict(_finance)




        _crypto = d.pop("crypto", UNSET)
        crypto: GetLedgerSummaryResponse200ByTopicCrypto | Unset
        if isinstance(_crypto,  Unset):
            crypto = UNSET
        else:
            crypto = GetLedgerSummaryResponse200ByTopicCrypto.from_dict(_crypto)




        _weather = d.pop("weather", UNSET)
        weather: GetLedgerSummaryResponse200ByTopicWeather | Unset
        if isinstance(_weather,  Unset):
            weather = UNSET
        else:
            weather = GetLedgerSummaryResponse200ByTopicWeather.from_dict(_weather)




        _sports = d.pop("sports", UNSET)
        sports: GetLedgerSummaryResponse200ByTopicSports | Unset
        if isinstance(_sports,  Unset):
            sports = UNSET
        else:
            sports = GetLedgerSummaryResponse200ByTopicSports.from_dict(_sports)




        _politics = d.pop("politics", UNSET)
        politics: GetLedgerSummaryResponse200ByTopicPolitics | Unset
        if isinstance(_politics,  Unset):
            politics = UNSET
        else:
            politics = GetLedgerSummaryResponse200ByTopicPolitics.from_dict(_politics)




        _economics = d.pop("economics", UNSET)
        economics: GetLedgerSummaryResponse200ByTopicEconomics | Unset
        if isinstance(_economics,  Unset):
            economics = UNSET
        else:
            economics = GetLedgerSummaryResponse200ByTopicEconomics.from_dict(_economics)




        _science_tech = d.pop("science_tech", UNSET)
        science_tech: GetLedgerSummaryResponse200ByTopicScienceTech | Unset
        if isinstance(_science_tech,  Unset):
            science_tech = UNSET
        else:
            science_tech = GetLedgerSummaryResponse200ByTopicScienceTech.from_dict(_science_tech)




        _culture = d.pop("culture", UNSET)
        culture: GetLedgerSummaryResponse200ByTopicCulture | Unset
        if isinstance(_culture,  Unset):
            culture = UNSET
        else:
            culture = GetLedgerSummaryResponse200ByTopicCulture.from_dict(_culture)




        _world = d.pop("world", UNSET)
        world: GetLedgerSummaryResponse200ByTopicWorld | Unset
        if isinstance(_world,  Unset):
            world = UNSET
        else:
            world = GetLedgerSummaryResponse200ByTopicWorld.from_dict(_world)




        _other = d.pop("other", UNSET)
        other: GetLedgerSummaryResponse200ByTopicOther | Unset
        if isinstance(_other,  Unset):
            other = UNSET
        else:
            other = GetLedgerSummaryResponse200ByTopicOther.from_dict(_other)




        get_ledger_summary_response_200_by_topic = cls(
            finance=finance,
            crypto=crypto,
            weather=weather,
            sports=sports,
            politics=politics,
            economics=economics,
            science_tech=science_tech,
            culture=culture,
            world=world,
            other=other,
        )


        get_ledger_summary_response_200_by_topic.additional_properties = d
        return get_ledger_summary_response_200_by_topic

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
