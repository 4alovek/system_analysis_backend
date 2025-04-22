from abc import ABC, abstractmethod
from interface_adapters.dtos.users import UserDto


class UserRepository(ABC):
    @abstractmethod
    def create_user(self, email: str, password: str, full_name: str) -> UserDto:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> UserDto | None:
        pass
