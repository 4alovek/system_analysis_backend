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
    # base_url = 'http://192.168.0.108:11434/v1',
    base_url= 'http://93.175.0.128:55555/v1',
    api_key='ollama', # required, but unused
)

response = client.chat.completions.create(
  model="gemma3:4b",
#   model="yandex/YandexGPT-5-Lite-8B-instruct-GGUF",
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

# import requests

# url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth "

# payload = {
#     'scope': 'GIGACHAT_API_PERS'
# }

# headers = {
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Accept': 'application/json',
#     'RqUID': 'd1accd09-8415-4ad6-9ae6-cc0de3621585',
#     'Authorization': 'Basic MWQ5YmIwZmMtYTE3Mi00ODczLWJhMGItYmMzNDkzNTZhZmIwOjNlNTg3MzZiLWZhZjAtNDNlMS05MWVjLTI2ZTZlZDU5ZjIwNA=='
# }

# response = requests.post(url, headers=headers, data=payload, verify=False)

# print(response.text)
# print(response)
# MWQ5YmIwZmMtYTE3Mi00ODczLWJhMGItYmMzNDkzNTZhZmIwOjNlNTg3MzZiLWZhZjAtNDNlMS05MWVjLTI2ZTZlZDU5ZjIwNA==

# import requests

# url = "https://gigachat.devices.sberbank.ru/api/v1/models"

# payload={}
# headers = {
#   'Accept': 'application/json',
#   'Authorization': 'Bearer eyJjdHkiOiJqd3QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiUlNBLU9BRVAtMjU2In0.s70V7_LZ3aMHp4XCODpkzD69KSzYBTlGBFgAQ0zNR5dYdRK92WbSE9KjXKHenzEht_ESRsPI7ik9csZfphvELW_UfHRUrjoYRKCEEu2baHlNHASj0pt-iSGIq6yFcgT-MQXk3XfmnBJqdoDv3Kvp6q0LGdcL6Zs0L5nRkMgLbfL_8Y2wb3e81BEynyGp_Dxpd_goTPk_7v_lZOa2_rrSLM0lGUVzH545Tl0oyZCV_tF0BiDODmOPvrl6GS3OJvvCjjqnq8wmaCLH9eCmtY_PCyVdRy2Lds1C7Dn-c1qzQvvYL0XXx01sOELbAiOHJaLkR0_MVh9RNWcfIC3vgHDy_w.lspG30zRqjUAUhegLra1lw.K2mwUiTYwiW-Xa33TFDLz5nUfRKUByI8-hSU3ZqGmI-O32u0nwmTM0XC3EH8sdDZqUejxgeh1ZPEpRKVN98lYlVULHShToD9eOLXBwXozOlDoIcKueh2YCpVJ7IkwZiNxZGhgwrJwXtHU2rjbBG7s5BHcYqtFVXB_Z2sMR0cR_rW_ozzJ8uQP_2zpGdpsaoDe-c_SzJiGFMpuuLHEjEJ1WypIqTZ6GrSSXvo9HV6L24yyl1tLC9i25I3y5bc1i6OhnnR2Dg_dozFlUOxoY1hLObys3ppPcz0XNCGFc2Bihh6bVW0IIj2lHbcEROeoKIMu-6ZJOgfYNt3jDlE1LD0AtCsIPNqptIOocllj0Es31Ucnti8xbK9BsnI4glmKNO-_Vuit7Bbl7PdE69WXvCBs5rRKbc-zE44Wy5EPirfXZv_sorXZKqH-1TT598pZLwAi3UVctsrLK8-YXCJKouaDPkJnhOsqzDJ4fJ-pQhWoold3x80GcMt3zsDbZj5xsrdhzs0Nxo2KroqkwfG5Kue2kLLU0L-JsbPUWvMWVCz9KnBBbsaDHWHFf42lbm5Ylrr9jBKqUv7WWjClijOb4n_66aTpMXVMY6kYtk3hjoIqRJngKkoZBvpD5wH6yQcDG4T2xQ9sbPprrsjM2bu1Pqu3Jq45phWA4XaWsj2uxT7fioi9OkWwECOrUPo4XTqwQDPj6KfW-bN0mz4Er9rxgUmT_TDlI4tmHkxBC70wBpWd2o.QKWbkY49cOLJmuaJW3gMj1Is9ymTYcu4wln02a5H4kc'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

# from gigachat import GigaChat

# giga = GigaChat(
#    credentials="eyJjdHkiOiJqd3QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiUlNBLU9BRVAtMjU2In0.s70V7_LZ3aMHp4XCODpkzD69KSzYBTlGBFgAQ0zNR5dYdRK92WbSE9KjXKHenzEht_ESRsPI7ik9csZfphvELW_UfHRUrjoYRKCEEu2baHlNHASj0pt-iSGIq6yFcgT-MQXk3XfmnBJqdoDv3Kvp6q0LGdcL6Zs0L5nRkMgLbfL_8Y2wb3e81BEynyGp_Dxpd_goTPk_7v_lZOa2_rrSLM0lGUVzH545Tl0oyZCV_tF0BiDODmOPvrl6GS3OJvvCjjqnq8wmaCLH9eCmtY_PCyVdRy2Lds1C7Dn-c1qzQvvYL0XXx01sOELbAiOHJaLkR0_MVh9RNWcfIC3vgHDy_w.lspG30zRqjUAUhegLra1lw.K2mwUiTYwiW-Xa33TFDLz5nUfRKUByI8-hSU3ZqGmI-O32u0nwmTM0XC3EH8sdDZqUejxgeh1ZPEpRKVN98lYlVULHShToD9eOLXBwXozOlDoIcKueh2YCpVJ7IkwZiNxZGhgwrJwXtHU2rjbBG7s5BHcYqtFVXB_Z2sMR0cR_rW_ozzJ8uQP_2zpGdpsaoDe-c_SzJiGFMpuuLHEjEJ1WypIqTZ6GrSSXvo9HV6L24yyl1tLC9i25I3y5bc1i6OhnnR2Dg_dozFlUOxoY1hLObys3ppPcz0XNCGFc2Bihh6bVW0IIj2lHbcEROeoKIMu-6ZJOgfYNt3jDlE1LD0AtCsIPNqptIOocllj0Es31Ucnti8xbK9BsnI4glmKNO-_Vuit7Bbl7PdE69WXvCBs5rRKbc-zE44Wy5EPirfXZv_sorXZKqH-1TT598pZLwAi3UVctsrLK8-YXCJKouaDPkJnhOsqzDJ4fJ-pQhWoold3x80GcMt3zsDbZj5xsrdhzs0Nxo2KroqkwfG5Kue2kLLU0L-JsbPUWvMWVCz9KnBBbsaDHWHFf42lbm5Ylrr9jBKqUv7WWjClijOb4n_66aTpMXVMY6kYtk3hjoIqRJngKkoZBvpD5wH6yQcDG4T2xQ9sbPprrsjM2bu1Pqu3Jq45phWA4XaWsj2uxT7fioi9OkWwECOrUPo4XTqwQDPj6KfW-bN0mz4Er9rxgUmT_TDlI4tmHkxBC70wBpWd2o.QKWbkY49cOLJmuaJW3gMj1Is9ymTYcu4wln02a5H4kc",
# )

# response = giga.chat("Расскажи про себя")

# print(response)