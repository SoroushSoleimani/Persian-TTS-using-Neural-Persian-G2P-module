from abc import ABC, abstractmethod
from typing import List

class BasePhonemizer(ABC):
    @abstractmethod
    def phonemize(self, text: str) -> str:
        """Convert grapheme text into phonemic sequence."""
        pass
