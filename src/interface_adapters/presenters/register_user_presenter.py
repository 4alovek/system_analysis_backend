from dataclasses import asdict

from interface_adapters.dtos.users import UserDto
from interface_adapters.dtos.auth import AuthResponseDto


class RegisterUserPresenter:
    def present(self, user: UserDto) -> dict:
        return asdict(user)


class LoginUserPresenter:
    def present_success(self, user_id: int) -> dict:
        return asdict(AuthResponseDto(success=True, message="Login successful", user_id=user_id))

    def present_failure(self, message: str) -> dict:
        return asdict(AuthResponseDto(success=False, message=message))
