"""
End-to-End Persian TTS Pipeline.
Coordinates cleaner, phonemizer, acoustic model, and audio processor.
"""

from pathlib import Path
from typing import Union, Optional
import numpy as np
from .config import TTSConfig
from .cleaner import PersianTextCleaner
from .models.vits import VitsSynthesizer
from .audio.processor import AudioProcessor

class PersianTTS:
    def __init__(self, config: Optional[TTSConfig] = None):
        self.config = config or TTSConfig()
        self.cleaner = PersianTextCleaner() if self.config.clean_text else None
        self.synthesizer = VitsSynthesizer(self.config.model)
        self.audio_processor = AudioProcessor()

    def synthesize(self, text: str) -> np.ndarray:
        if self.cleaner:
            text = self.cleaner.clean(text)
        
        waveform = self.synthesizer.synthesize(text)
        
        if self.config.audio.trim_silence:
            waveform = self.audio_processor.trim_silence(waveform)
        if self.config.audio.normalize_volume:
            waveform = self.audio_processor.normalize_peak(waveform)
            
        return waveform

    def synthesize_to_file(self, text: str, output_path: Union[str, Path]) -> Path:
        output_path = Path(output_path)
        wav = self.synthesize(text)
        self.audio_processor.save_wav(output_path, wav, self.synthesizer.sampling_rate)
        return output_path
