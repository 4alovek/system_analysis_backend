from dataclasses import asdict

from interface_adapters.dtos.users import UserDto
from interface_adapters.dtos.auth import AuthResponseDto


class RegisterUserPresenter:
    def present(self, user: UserDto) -> dict:
        return asdict(user)


class LoginUserPresenter:
    def present_success(self, user) -> dict:
        return {
            "success": True,
            "message": "Login successful",
            "user_id": user.user_id,
            "access": "dummy_access_token",  # TODO: Replace with real JWT token
            "refresh": "dummy_refresh_token",  # TODO: Replace with real JWT token
            "user": {
                "id": user.user_id,
                "email": user.email,
                "full_name": user.full_name,
            }
        }

    def present_failure(self, message: str) -> dict:
        return {"success": False, "message": message}
