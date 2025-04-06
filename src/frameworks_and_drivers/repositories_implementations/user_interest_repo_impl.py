from typing import List
from interface_adapters.repositories_interfaces.user_interest_repo import UserInterestRepository
from interface_adapters.dtos.users import UserInterestDto
from users.models import UserInterest


class DjangoUserInterestRepository(UserInterestRepository):
    def get_interests_by_user_id(self, user_id: int) -> List[UserInterestDto]:
        interests = UserInterest.objects.filter(user_id=user_id)
        return [
            UserInterestDto(
                interest_id=i.interest_id,
                user_id=i.user_id,
                interest_name=i.interest_name,
                preference_weight=i.preference_weight,
                preference_difficulty=i.preference_difficulty,
            )
            for i in interests
        ]
    
    def set_interests_for_user(self, user_id: int, interests: List[str]) -> None:
        # Удалим старые интересы
        UserInterest.objects.filter(user_id=user_id).delete()

        # Добавим новые
        for name in interests:
            UserInterest.objects.create(
                user_id=user_id,
                interest_name=name,
                preference_weight=1.0,
                preference_difficulty=1,
            )
