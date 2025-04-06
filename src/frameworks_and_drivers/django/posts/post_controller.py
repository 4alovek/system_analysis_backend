from ninja_extra import api_controller, route
from usecases.posts import GetPostUseCase
from interface_adapters.controllers.post_controller import PostControllerInterface
from frameworks_and_drivers.repositories_implementations.post_repo import PostRepository
from interface_adapters.presenters.posts import NinjaPostPresenter

@api_controller("/posts")
class NinjaPostController:
    def __init__(self):
        self.use_case = GetPostUseCase(post_repo=PostRepository())
        self.presenter = NinjaPostPresenter()

    @route.get("/{post_id}")
    def get_post(self, post_id: int):
        post_dto = self.use_case.execute(post_id)
        return self.presenter.present(post_dto)
