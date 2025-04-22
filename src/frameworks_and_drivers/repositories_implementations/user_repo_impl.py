from interface_adapters.dtos.users import UserDto
from interface_adapters.repositories_interfaces.user_repo import UserRepository
from users.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


class DjangoUserRepository(UserRepository):
    def create_user(self, email: str, password: str, full_name: str) -> UserDto:
        user = User.objects.create(
            email=email,
            password_hash=make_password(password),
            full_name=full_name,
        )
        return UserDto(
            user_id=user.user_id,
            email=user.email,
            password_hash=user.password_hash,
            full_name=user.full_name,
            created_at=user.created_at,
        )

    def get_user_by_email(self, email: str) -> UserDto | None:
        try:
            user = User.objects.get(email=email)
            return UserDto(
                user_id=user.user_id,
                email=user.email,
                password_hash=user.password_hash,
                full_name=user.full_name,
                created_at=user.created_at,
            )
        except User.DoesNotExist:
            return None