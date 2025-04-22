from ninja_extra import api_controller, route
from ninja_extra.permissions import AllowAny
from pydantic import BaseModel
from typing import Optional

from interface_adapters.dtos.auth import UserRegisterInputDto
from interface_adapters.dtos.auth import UserLoginInputDto
from interface_adapters.dtos.users import UserInterestInputDto
from interface_adapters.presenters.register_user_presenter import RegisterUserPresenter, LoginUserPresenter
from interface_adapters.presenters.set_user_interests_presenter import SetUserInterestsPresenter
from frameworks_and_drivers.repositories_implementations.user_repo_impl import DjangoUserRepository
from frameworks_and_drivers.repositories_implementations.user_interest_repo_impl import DjangoUserInterestRepository
from usecases.user import RegisterUserUseCase, LoginUserUseCase
from usecases.set_user_interest import SetUserInterestsUseCase


class RegisterInputSchema(BaseModel):
    email: str
    password: str
    full_name: str


class LoginInputSchema(BaseModel):
    email: str
    password: str


class UserInterestIn(BaseModel):
    user_id: int
    interests: list[str]


@api_controller("/api/v1/auth", permissions=[AllowAny])
class AuthController:
    @route.post("/register")
    def register(self, request, data: RegisterInputSchema):
        input_dto = UserRegisterInputDto(
            email=data.email,
            password=data.password,
            full_name=data.full_name,
        )
        usecase = RegisterUserUseCase(
            user_repo=DjangoUserRepository(),
            presenter=RegisterUserPresenter(),
        )
        return usecase.execute(input_dto)

    @route.post("/login")
    def login(self, request, data: LoginInputSchema):
        input_dto = UserLoginInputDto(email=data.email, password=data.password)
        usecase = LoginUserUseCase(
            user_repo=DjangoUserRepository(),
            presenter=LoginUserPresenter()
        )
        return usecase.execute(input_dto)
    
    @route.post("/interests")
    def set_interests(self, request, data: UserInterestIn):
        input_dto = UserInterestInputDto(user_id=data.user_id, interests=data.interests)
        usecase = SetUserInterestsUseCase(
            repo=DjangoUserInterestRepository(),
            presenter=SetUserInterestsPresenter()
        )
        return usecase.execute(input_dto)
