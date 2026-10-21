# Python API Reference

### `PersianTTS`
Primary interface for text-to-speech synthesis.

```python
from persian_tts import PersianTTS, TTSConfig

tts = PersianTTS()

# Synthesize directly to numpy array
waveform = tts.synthesize("متن تستی به زبان فارسی")

# Synthesize and write directly to .wav file
tts.synthesize_to_file("متن تستی به زبان فارسی", "output.wav")
```

### `PersianTextCleaner`
Pre-processing and normalization module.

```python
from persian_tts.cleaner import PersianTextCleaner

cleaner = PersianTextCleaner(remove_diacritics=True)
cleaned = cleaner.clean("كتاب ياسمين با پنجره‌های آبی")
```
