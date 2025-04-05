from dataclasses import dataclass
from datetime import datetime


@dataclass
class GPTRequest:
    request_id: int
    user_id: int
    post_id: int
    got_response: bool | None
    prompt: str | None
    created_at: datetime | None
