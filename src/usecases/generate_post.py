# from interface_adapters.repositories_interfaces.gpt_repo import GPTRepositoryInterface
# from interface_adapters.repositories_interfaces.post_repo import PostRepository
# from interface_adapters.repositories_interfaces.user_interest_repo import UserInterestRepository
# from interface_adapters.dtos.posts import PostDto


# class GeneratePostUseCase:
#     def __init__(
#         self,
#         gpt_repo: GPTRepositoryInterface,
#         post_repo: PostRepository,
#         interest_repo: UserInterestRepository,
#     ):
#         self.gpt_repo = gpt_repo
#         self.post_repo = post_repo
#         self.interest_repo = interest_repo

#     def execute(self, user_id: int) -> PostDto:
#         # 1. Получаем интересы пользователя
#         interests = self.interest_repo.get_interests_by_user_id(user_id)
#         interest_names = [i.interest_name for i in interests]

#         # 2. Генерация контента через GPT
#         content = self.gpt_repo.generate_post_content(interest_names)

#         # 3. Создаём пост
#         post = self.post_repo.create_post(
#             user_id=user_id,
#             content=content,
#             generated_by_gpt=True,
#             title="Сгенерированный пост",  # Можно позже генерировать отдельно
#             status="published",
#         )

#         return post
from interface_adapters.dtos.gpt_integration import GeneratePostInputDto, GeneratedPostDto
from interface_adapters.repositories_interfaces.gpt_repo import GPTRepositoryInterface
from interface_adapters.repositories_interfaces.post_repo import PostRepositoryInterface
from interface_adapters.presenters.generate_post_presenter import GeneratePostPresenter


class GeneratePostUseCase:
    def __init__(
        self,
        gpt_repo: GPTRepositoryInterface,
        post_repo: PostRepositoryInterface,
        presenter: GeneratePostPresenter
    ):
        self.gpt_repo = gpt_repo
        self.post_repo = post_repo
        self.presenter = presenter

    def execute(self, input_data: GeneratePostInputDto) -> dict:
        content = self.gpt_repo.generate_post_content(input_data.interests)
        title = content.strip().split("\n")[0].replace("#", "").strip()[:255]

        post_id = self.post_repo.create_post(
            user_id=input_data.user_id,
            content=content,
            title=title,
            generated_by_gpt=True
        )

        post_dto = GeneratedPostDto(post_id=post_id, title=title, content=content)
        return self.presenter.present(post_dto)
