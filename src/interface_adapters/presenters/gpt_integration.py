from pydantic import BaseModel
from datetime import datetime
from interface_adapters.dtos.gpt_integration import GPTRequest


class GPTRequestPresenter(BaseModel):
    request_id: int
    user_id: int
    post_id: int
    got_response: bool | None
    prompt: str | None
    created_at: datetime | None

    @classmethod
    def from_dto(cls, dto: GPTRequest) -> "GPTRequestPresenter":
        return cls(
            request_id=dto.request_id,
            user_id=dto.user_id,
            post_id=dto.post_id,
            got_response=dto.got_response,
            prompt=dto.prompt,
            created_at=dto.created_at,
        )
