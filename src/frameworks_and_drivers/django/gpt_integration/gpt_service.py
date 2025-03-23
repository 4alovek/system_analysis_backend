from openai import OpenAI


class GPTService:
    def __init__(self):
        self.client = OpenAI(
            base_url = 'http://host.docker.internal:11434/v1',
            api_key='ollama-key', # required, but unused
        )

    def generate_post_content(self):
        response = self.client.chat.completions.create(
            model="llama3.1",
            messages=[
                {"role": "user", "content": "Создай креативный пост по темам в формате Markdown, темы сейчас пришлю"},
                {"role": "user", "content": "Инвестиции, Криптовалюта"}
            ]
        )
        return response.choices[0].message.content
