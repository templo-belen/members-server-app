from sqlalchemy.orm import Session

from app.database import MemberADN, MemberGiftAbility
from app.models import MemberGiftAbilityData, GiftAbilityType
from app.models.member_adn import MemberADNResponse, MemberADNData


class MemberADNService:
    def __init__(self):
        pass

    def find_by_member_id(self, member_id: int, db: Session) -> MemberADNResponse | None:
        member_adn = db.query(MemberADN).filter(MemberADN.member_id == member_id).first()
        member_adn_response = None
        if member_adn:
            member_adn_response = MemberADNData.model_validate(member_adn)

        member_abilities_list = db.query(MemberGiftAbility).filter(MemberGiftAbility.member_id == member_id).all()
        member_abilities_response = []
        if member_abilities_list:
            member_abilities_response = [MemberGiftAbilityData.model_validate(ability) for ability in member_abilities_list]

        if not member_adn_response and not member_abilities_response:
            return None

        return MemberADNResponse(
            adn=member_adn_response,
            mainGiftList= [ability for ability in member_abilities_response if ability.type == GiftAbilityType.main_gift],
            secondaryGiftList=[ability for ability in member_abilities_response if ability.type == GiftAbilityType.secondary_gift],
            acquiredSkillList=[ability for ability in member_abilities_response if ability.type == GiftAbilityType.acquired_skill],
            naturalAbilityList=[ability for ability in member_abilities_response if ability.type == GiftAbilityType.natural_ability]
        )

