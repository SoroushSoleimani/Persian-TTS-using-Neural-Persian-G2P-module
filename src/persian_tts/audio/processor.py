"""
Audio processing utilities for waveforms: peak normalization, silence trimming, and export.
"""

import numpy as np
import scipy.io.wavfile as wavfile
from pathlib import Path
from typing import Union

class AudioProcessor:
    @staticmethod
    def normalize_peak(waveform: np.ndarray, target_peak: float = 0.95) -> np.ndarray:
        max_val = np.max(np.abs(waveform))
        if max_val > 0:
            return waveform * (target_peak / max_val)
        return waveform

    @staticmethod
    def trim_silence(waveform: np.ndarray, threshold: float = 0.01) -> np.ndarray:
        non_silent = np.where(np.abs(waveform) > threshold)[0]
        if len(non_silent) > 0:
            return waveform[non_silent[0]:non_silent[-1] + 1]
        return waveform

    @staticmethod
    def save_wav(path: Union[str, Path], waveform: np.ndarray, sampling_rate: int):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        # Convert float [-1.0, 1.0] to int16 if needed or keep float32
        if waveform.dtype in (np.float32, np.float64):
            scaled = np.int16(np.clip(waveform, -1.0, 1.0) * 32767)
            wavfile.write(str(path), sampling_rate, scaled)
        else:
            wavfile.write(str(path), sampling_rate, waveform)
