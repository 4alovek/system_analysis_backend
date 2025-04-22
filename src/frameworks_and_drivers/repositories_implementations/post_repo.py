from posts.models import Post
from interface_adapters.repositories_interfaces.post_repo import PostRepositoryInterface
from interface_adapters.dtos.posts import PostDto
from typing import Optional

class PostRepository(PostRepositoryInterface):
    def create_post(self, user_id: int, content: str, title: str, generated_by_gpt: bool) -> int:
        post = Post.objects.create(
            user_id=user_id,
            content=content,
            title=title or "Пост от GPT",
            generated_by_gpt=generated_by_gpt,
            status="draft"
        )
        return post.post_id

    def get_posts_by_user(self, user):
        return Post.objects.filter(user=user)

    def get_by_id(self, post_id: int) -> Optional[PostDto]:
        """Получает пост по ID через Django ORM"""
        post = Post.objects.filter(post_id=post_id).first()
        if post is None:
            return None

        return PostDto(
            post_id=post.post_id,
            user_id=post.user,
            content=post.content,
            generated_by_gpt=post.generated_by_gpt,
            title=post.title,
            status=post.status,
            created_at=post.created_at
        )
