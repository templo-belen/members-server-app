from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict

from app.models.enum_serializer import serialized_enum_by_name
from app.models.enum_type import GiftAbilityType


class MemberADNData(BaseModel):
    member_id: int = Field(description="Member ID", alias="memberId")

    passion: Optional[str] = Field(description="What you passionately desire to do for God", alias="passion")
    mission: Optional[str] = Field(description="Mission statement", alias="mission")
    personal_prophecies: Optional[str] = Field(description="Personal prophecies and impressions", alias="personalProphecies")
    personal_values: Optional[str] = Field(description="Personal values", alias="personalValues")
    one_year_plans: Optional[str] = Field(description="One-year plans", alias="oneYearPlans")
    two_year_plans: Optional[str] = Field(description="Two-year plans", alias="twoYearPlans")
    five_year_plans: Optional[str] = Field(description="Five-year plans", alias="fiveYearPlans")
    strengths: Optional[str] = Field(description="Personal strengths", alias="strengths")
    weaknesses: Optional[str] = Field(description="Personal weaknesses", alias="weaknesses")
    improvement_areas: Optional[str] = Field(description="Areas you need to improve", alias="improvementAreas")
    mentor: Optional[str] = Field(description="Mentor's name", alias="mentor")
    mentor_frequency: Optional[str] = Field(description="Frequency of meeting with your mentors", alias="mentorFrequency")
    mentee: Optional[str] = Field(description="People you mentor", alias="mentee")
    mentee_frequency: Optional[str] = Field(description="Frequency with which you mentor", alias="menteeFrequency")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )

class MemberGiftAbilityData(BaseModel):
    id: int = Field(description="Member gift ability ID", alias="id")
    member_id: int = Field(description="Member ID", alias="memberId")

    name: str = Field(description="Gift or ability name", alias="name")
    type: serialized_enum_by_name(GiftAbilityType) = Field(description="Gift or ability type", alias="type")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )

class MemberADNResponse(BaseModel):
    adn: Optional[MemberADNData] = Field(description="Member ADN data", alias="adn")
    main_gift_list: List[MemberGiftAbilityData] = Field(description="List of main gifts", alias="mainGiftList")
    secondary_gift_list: List[MemberGiftAbilityData] = Field(description="List of secondary gifts", alias="secondaryGiftList")
    acquired_skill_list: List[MemberGiftAbilityData] = Field(description="List of acquired skills", alias="acquiredSkillList")
    natural_ability: List[MemberGiftAbilityData] = Field(description="List of natural abilities", alias="naturalAbilityList")

    model_config = ConfigDict(
        populate_by_name=True
    )
