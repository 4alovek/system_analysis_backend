from interface_adapters.dtos.gpt_integration import GeneratedPostDto


class GeneratePostPresenter:
    def present(self, post: GeneratedPostDto) -> dict:
        return {
            "post_id": post.post_id,
            "title": post.title,
            "content": post.content
        }
