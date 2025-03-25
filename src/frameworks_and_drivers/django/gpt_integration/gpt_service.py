from openai import OpenAI

client = OpenAI(
    base_url = 'http://host.docker.internal:11434/v1',
    api_key='some-key', # required, but unused
)


class GPTService:
  def __init__(self):
    pass
  
  def get_response():
    response = client.chat.completions.create(
      model="deepseek-r1:8b",
      temperature=0.3,
      messages=[
        {"role": "user", "content": "Создай креативный пост по темам в формате Markdown на 500-1000 символов, тему сейчас пришлю, постарайся думать по-минимуму"},
        {"role": "user", "content": "Инвестиции"}
      ]
    )
    return response.choices[0].message.content

# print(GPTService.get_response())