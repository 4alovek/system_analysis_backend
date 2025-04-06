from interface_adapters.dtos.users import UserDto
from interface_adapters.dtos.auth import AuthResponseDto


class RegisterUserPresenter:
    def present(self, user: UserDto) -> UserDto:
        return user


class LoginUserPresenter:
    def present_success(self, user_id: int) -> AuthResponseDto:
        return AuthResponseDto(success=True, message="Login successful", user_id=user_id)

    def present_failure(self, message: str) -> AuthResponseDto:
        return AuthResponseDto(success=False, message=message)
