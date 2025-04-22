from abc import ABC, abstractmethod
from typing import Dict, Any

class PostControllerInterface(ABC):
    @abstractmethod
    def get_post(self, post_id: int) -> Dict[str, Any]:
        """ Получить пост по ID """
        pass
