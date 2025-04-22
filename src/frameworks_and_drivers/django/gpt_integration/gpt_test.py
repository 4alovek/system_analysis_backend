# def caesar_decipher(ciphertext, shift):
#     plaintext = ""
#     for char in ciphertext:
#         if char.isalpha():
#             ascii_offset = 65 if char.isupper() else 97
#             plaintext += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
#         else:
#             plaintext += char
#     return plaintext

# # Given ciphertext
# ciphertext = "Kxdyxi sc dro locd wkx exsdon zvkiob"

# # Corrected shift value (as per your hint earlier)
# shift = 10

# decrypted_text = caesar_decipher(ciphertext, shift) # Negative shift to decrypt

# print(decrypted_text)
from openai import OpenAI

client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)

response = client.chat.completions.create(
  # model="llama3.1",
  model="yandex/YandexGPT-5-Lite-8B-instruct-GGUF",
  messages=[
    # {"role": "system", "content": "You are a helpful assistant."},
    # {"role": "user", "content": "Who won the world series in 2020?"},
    # {"role": "assistant", "content": "The LA Dodgers won in 2020."},
    # {"role": "user", "content": "Where was it played?"}
    {"role": "user", "content": "Напиши стихотворение про кетчунез"}
  ],
  max_tokens=10000,
  temperature=0.7,
)
print(response.choices[0].message.content)

