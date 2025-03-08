from abc import ABC, abstractmethod

class PostRepositoryInterface(ABC):
    @abstractmethod
    def create_post(self, title, content, user=None):
        pass

    @abstractmethod
    def get_posts_by_user(self, user):
        pass
