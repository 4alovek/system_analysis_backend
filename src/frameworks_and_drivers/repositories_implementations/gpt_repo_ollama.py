from interface_adapters.repositories_interfaces.gpt_repo import GPTRepositoryInterface
from openai import OpenAI


class OllamaGPTRepository(GPTRepositoryInterface):
    def __init__(self):
        self.client = OpenAI(
            base_url='http://host.docker.internal:11434/v1',
            api_key='ollama-key'
        )

    def generate_post_content(self, interests: list[str]) -> str:
        response = self.client.chat.completions.create(
            model="llama3.2:1b",
            messages=[
                {"role": "user", "content": "Создай креативный пост в формате Markdown по темам:"},
                {"role": "user", "content": ", ".join(interests)}
            ]
        )
        return response.choices[0].message.content
