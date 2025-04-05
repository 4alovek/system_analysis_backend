from abc import ABC, abstractmethod
from interface_adapters.dtos.posts import PostDto


class PostRepositoryInterface(ABC):
    @abstractmethod
    def create_post(self, title, content, user=None):
        pass

    @abstractmethod
    def get_posts_by_user(self, user):
        pass

    @abstractmethod
    def get_by_id(self, post_id: int) -> PostDto | None:
        """Получает пост по ID"""
        pass
