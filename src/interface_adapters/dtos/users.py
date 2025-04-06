from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserDto:
    user_id: int
    email: str
    password_hash: str | None
    full_name: str
    created_at: datetime | None


@dataclass
class UserLoginDto:
    email: str
    password_hash: str


@dataclass
class UserInterestDto:
    interest_id: int
    user_id: int
    interest_name: str
    preference_weight: float | None
    preference_difficulty: int | None


@dataclass
class UserInterestInputDto:
    user_id: int
    interests: list[str]
