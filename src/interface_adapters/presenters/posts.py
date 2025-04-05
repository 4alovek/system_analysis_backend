from pydantic import BaseModel
from datetime import datetime
from interface_adapters.dtos.posts import PostDto, PostReactionDto


class PostPresenter(BaseModel):
    post_id: int
    user_id: int
    content: str
    generated_by_gpt: bool
    title: str | None
    status: str
    created_at: datetime | None

    @classmethod
    def from_dto(cls, dto: PostDto) -> "PostPresenter":
        return cls(
            post_id=dto.post_id,
            user_id=dto.user_id,
            content=dto.content,
            generated_by_gpt=dto.generated_by_gpt,
            title=dto.title,
            status=dto.status,
            created_at=dto.created_at,
        )


class PostReactionPresenter(BaseModel):
    reaction_id: int
    user_id: int
    post_id: int
    reaction_type: str
    created_at: datetime | None

    @classmethod
    def from_dto(cls, dto: PostReactionDto) -> "PostReactionPresenter":
        return cls(
            reaction_id=dto.reaction_id,
            user_id=dto.user_id,
            post_id=dto.post_id,
            reaction_type=dto.reaction_type,
            created_at=dto.created_at,
        )
