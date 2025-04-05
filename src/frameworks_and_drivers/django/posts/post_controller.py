from ninja_extra import api_controller, route
from usecases.posts import GetPostUseCase
from interface_adapters.controllers.post_controller import PostControllerInterface
from frameworks_and_drivers.repositories_implementations.post_repo import PostRepository

@api_controller("/posts")
class PostController(PostControllerInterface):
    def __init__(self):
        self.use_case = GetPostUseCase(post_repo=PostRepository())

    @route.get("/{post_id}")
    def get_post(self, post_id: int):
        return self.use_case.execute(post_id)
