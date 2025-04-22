from pydantic import BaseModel
from interface_adapters.dtos.users import UserLoginDto, UserInterestDto


class UserLoginPresenter(BaseModel):
    user_id: int
    token: str

    @classmethod
    def from_dto(cls, dto: UserLoginDto) -> "UserLoginPresenter":
        return cls(user_id=dto.user_id, token=dto.token)


class UserInterestPresenter(BaseModel):
    interest_id: int
    user_id: int
    interest_name: str
    preference_weight: float | None
    preference_difficulty: int | None

    @classmethod
    def from_dto(cls, dto: UserInterestDto) -> "UserInterestPresenter":
        return cls(
            interest_id=dto.interest_id,
            user_id=dto.user_id,
            interest_name=dto.interest_name,
            preference_weight=dto.preference_weight,
            preference_difficulty=dto.preference_difficulty,
        )
