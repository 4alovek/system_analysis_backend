from interface_adapters.dtos.auth import UserRegisterInputDto, UserLoginInputDto
from interface_adapters.repositories_interfaces.user_repo import UserRepository
from interface_adapters.presenters.register_user_presenter import RegisterUserPresenter, LoginUserPresenter
from django.contrib.auth.hashers import check_password


class RegisterUserUseCase:
    def __init__(self, user_repo: UserRepository, presenter: RegisterUserPresenter):
        self.user_repo = user_repo
        self.presenter = presenter

    def execute(self, data: UserRegisterInputDto):
        user = self.user_repo.create_user(
            email=data.email,
            password=data.password,
            full_name=data.full_name
        )
        return self.presenter.present(user)


class LoginUserUseCase:
    def __init__(self, user_repo: UserRepository, presenter: LoginUserPresenter):
        self.user_repo = user_repo
        self.presenter = presenter

    def execute(self, data: UserLoginInputDto):
        user = self.user_repo.get_user_by_email(data.email)
        if not user:
            return self.presenter.present_failure("User not found")

        if not check_password(data.password, user.password_hash):
            return self.presenter.present_failure("Invalid password")

        return self.presenter.present_success(user.user_id)
