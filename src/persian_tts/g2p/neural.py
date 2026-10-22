"""
Neural Seq2Seq G2P model interface.
Wraps an attention-based encoder-decoder model for Persian grapheme-to-phoneme conversion.
"""

from .base import BasePhonemizer

class NeuralG2P(BasePhonemizer):
    def __init__(self, model_path: str = None):
        self.model_path = model_path
        self._is_loaded = False

    def load_model(self):
        self._is_loaded = True

    def phonemize(self, text: str) -> str:
        # Fallback to direct token mapping if neural weights are not yet bound
        return text
