from pydantic import BaseModel
from typing import List

from usecases.generate_post import GeneratePostUseCase
from interface_adapters.dtos.gpt_integration import GeneratePostInputDto
from frameworks_and_drivers.repositories_implementations.gpt_repo_ollama import OllamaGPTRepository
from frameworks_and_drivers.repositories_implementations.post_repo import PostRepository
from interface_adapters.presenters.generate_post_presenter import GeneratePostPresenter
from ninja_extra import api_controller, route
from ninja_extra.permissions import AllowAny
from pydantic import BaseModel
from typing import List


class GeneratePostIn(BaseModel):
    user_id: int
    interests: List[str]


@api_controller("/v1/posts", permissions=[AllowAny])
class PostsController:
    @route.post("/generate")
    def generate_post(self, data: GeneratePostIn):
        input_dto = GeneratePostInputDto(
            user_id=data.user_id,
            interests=data.interests,
        )
        usecase = GeneratePostUseCase(
            gpt_repo=OllamaGPTRepository(),
            post_repo=PostRepository(),
            presenter=GeneratePostPresenter(),
        )
        return usecase.execute(input_dto)
