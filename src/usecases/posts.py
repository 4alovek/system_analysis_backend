from interface_adapters.dtos.posts import PostDto
from interface_adapters.repositories_interfaces.post_repo import PostRepositoryInterface
from typing import Optional

class GetPostUseCase:
    """Use case для получения поста"""

    def __init__(self, post_repo: PostRepositoryInterface):
        self.post_repo = post_repo

    def execute(self, post_id: int) -> Optional[PostDto]:
        return self.post_repo.get_by_id(post_id)
