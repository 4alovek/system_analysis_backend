from abc import ABC, abstractmethod

class GPTRepositoryInterface(ABC):
    @abstractmethod
    def generate_post_content(self, interests: list[str]) -> str:
        pass
