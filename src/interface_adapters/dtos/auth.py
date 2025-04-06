from dataclasses import dataclass


@dataclass
class UserRegisterInputDto:
    email: str
    password: str
    full_name: str


@dataclass
class UserLoginInputDto:
    email: str
    password: str


@dataclass
class AuthResponseDto:
    success: bool
    message: str
    user_id: int | None = None
