"""
Hybrid Persian Phonemizer combining dictionary overrides, rule heuristics, and neural inference.
"""

from .base import BasePhonemizer
from .rule_based import RuleBasedPhonemizer
from .neural import NeuralG2P

class HybridPhonemizer(BasePhonemizer):
    def __init__(self, use_neural: bool = False, neural_model_path: str = None):
        self.rule_based = RuleBasedPhonemizer()
        self.neural = NeuralG2P(neural_model_path) if use_neural else None
        self.custom_dict = {}

    def register_word(self, word: str, phoneme: str):
        self.custom_dict[word] = phoneme

    def phonemize(self, text: str) -> str:
        words = text.split()
        resolved = []
        for w in words:
            if w in self.custom_dict:
                resolved.append(self.custom_dict[w])
            elif self.neural and self.neural._is_loaded:
                resolved.append(self.neural.phonemize(w))
            else:
                resolved.append(self.rule_based.phonemize(w))
        return " ".join(resolved)
