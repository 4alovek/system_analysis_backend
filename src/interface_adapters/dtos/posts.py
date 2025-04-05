from dataclasses import dataclass
from datetime import datetime


@dataclass
class PostCreateDto:
    user_id: int
    content: str
    title: str | None
    status: str
    generated_by_gpt: bool


@dataclass
class PostDto:
    post_id: int
    user_id: int
    content: str
    generated_by_gpt: bool
    title: str | None
    status: str
    created_at: datetime | None


@dataclass
class PostResponseDto:
    post_id: int
    user_id: int
    content: str
    title: str | None
    status: str
    created_at: datetime


@dataclass
class PostReactionDto:
    reaction_id: int
    user_id: int
    post_id: int
    reaction_type: str
    created_at: datetime | None
