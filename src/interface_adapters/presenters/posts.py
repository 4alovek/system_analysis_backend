from pydantic import BaseModel
from datetime import datetime
from interface_adapters.dtos.posts import PostDto, PostReactionDto
from abc import ABC, abstractmethod
from typing import Optional


class PostPresenterInterface(ABC):
    @abstractmethod
    def present(self, post: Optional[PostDto]) -> dict:
        """Преобразовать DTO в формат ответа"""
        pass


class NinjaPostPresenter(PostPresenterInterface):
    def present(self, post: Optional[PostDto]) -> dict:
        if post is None:
            return {"detail": "Post not found"}
        
        return {
            "post_id": post.post_id,
            "user_id": post.user_id,
            "content": post.content,
            "generated_by_gpt": post.generated_by_gpt,
            "title": post.title,
            "status": post.status,
            "created_at": post.created_at.isoformat() if post.created_at else None,
        }


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
