"""
VITS model synthesis wrapper with automatic device placement (CUDA/CPU).
"""

import torch
import numpy as np
from transformers import VitsModel, AutoTokenizer
from ..config import ModelConfig

class VitsSynthesizer:
    def __init__(self, config: ModelConfig = None):
        self.config = config or ModelConfig()
        self.device = self._resolve_device(self.config.device)
        self.tokenizer = None
        self.model = None

    def _resolve_device(self, dev: str) -> torch.device:
        if dev == "auto":
            return torch.device("cuda" if torch.cuda.is_available() else "cpu")
        return torch.device(dev)

    def load(self):
        if self.model is None:
            self.tokenizer = AutoTokenizer.from_pretrained(self.config.model_name_or_path)
            self.model = VitsModel.from_pretrained(self.config.model_name_or_path).to(self.device)
            if self.config.use_half_precision and self.device.type == "cuda":
                self.model = self.model.half()
            self.model.eval()

    def synthesize(self, text: str) -> np.ndarray:
        self.load()
        inputs = self.tokenizer(text, return_tensors="pt").to(self.device)
        with torch.no_grad():
            output = self.model(**inputs)
            waveform = output.waveform[0].cpu().float().numpy()
        return waveform

    @property
    def sampling_rate(self) -> int:
        self.load()
        return self.model.config.sampling_rate
