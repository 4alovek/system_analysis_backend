from dataclasses import dataclass
from datetime import datetime
from typing import List



@dataclass
class GPTRequest:
    request_id: int
    user_id: int
    post_id: int
    got_response: bool | None
    prompt: str | None
    created_at: datetime | None


@dataclass
class GeneratePostInputDto:
    user_id: int
    interests: List[str]


@dataclass
class GeneratedPostDto:
    post_id: int
    title: str
    content: str
