from interface_adapters.repositories_interfaces.gpt_repo import GPTRepository
from frameworks_and_drivers.gpt_integration.gpt_service import GigaChatService

class GigaChatRepository(GPTRepository):
    def __init__(self):
        self.gpt_service = GigaChatService()

    def generate_text(self, prompt: str) -> str:
        return self.gpt_service.generate_text(prompt) 