from dataclasses import dataclass, field
from typing import Optional

@dataclass
class AudioConfig:
    sampling_rate: int = 16000
    trim_silence: bool = True
    normalize_volume: bool = True
    silence_threshold_db: float = -40.0

@dataclass
class ModelConfig:
    model_name_or_path: str = "facebook/mms-tts-fas"
    device: str = "auto"
    use_half_precision: bool = False

@dataclass
class TTSConfig:
    audio: AudioConfig = field(default_factory=AudioConfig)
    model: ModelConfig = field(default_factory=ModelConfig)
    clean_text: bool = True
