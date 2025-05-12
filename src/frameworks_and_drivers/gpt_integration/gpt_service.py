import requests
import uuid
from typing import Optional

class GigaChatService:
    def __init__(self):
        self.base_url = "https://ngw.devices.sberbank.ru:9443/api/v2"
        self.auth_token = "MWQ5YmIwZmMtYTE3Mi00ODczLWJhMGItYmMzNDkzNTZhZmIwOjNlNTg3MzZiLWZhZjAtNDNlMS05MWVjLTI2ZTZlZDU5ZjIwNA=="
        self.access_token: Optional[str] = None

    def get_access_token(self) -> str:
        """Получение токена доступа GigaChat"""
        if self.access_token:
            return self.access_token

        url = f"{self.base_url}/oauth"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'RqUID': str(uuid.uuid4()),
            'Authorization': f'Basic {self.auth_token}'
        }
        payload = {
            'scope': 'GIGACHAT_API_PERS'
        }

        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        
        self.access_token = response.json()['access_token']
        return self.access_token

    def generate_text(self, prompt: str) -> str:
        """Генерация текста с помощью GigaChat"""
        url = f"{self.base_url}/chat/completions"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.get_access_token()}'
        }
        payload = {
            "model": "GigaChat:latest",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.7,
            "max_tokens": 1000
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        return response.json()['choices'][0]['message']['content'] 