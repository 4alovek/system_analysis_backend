from abc import ABC, abstractmethod
from typing import List
from interface_adapters.dtos.users import UserInterestDto


class UserInterestRepository(ABC):
    @abstractmethod
    def get_interests_by_user_id(self, user_id: int) -> List[UserInterestDto]:
        pass

    @abstractmethod
    def set_interests_for_user(self, user_id: int, interests: List[str]) -> None:
        pass
