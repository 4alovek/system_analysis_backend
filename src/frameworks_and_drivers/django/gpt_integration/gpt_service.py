from openai import OpenAI

client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama3.1', # required, but unused
)

response = client.chat.completions.create(
  model="llama3.1",
  messages=[
    {"role": "user", "content": "Создай креативный пост по темам в формате Markdown, темы сейчас пришлю"},
    {"role": "user", "content": "Музыка, Инвестиции, Covid-19"}
  ]
)
print(response.choices[0].message.content)
# ollama run llama3.1
