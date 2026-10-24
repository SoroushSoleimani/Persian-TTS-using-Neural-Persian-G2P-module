# Persian TTS using Neural Persian G2P Module & VITS

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11-3776AB?logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org)
[![HuggingFace](https://img.shields.io/badge/🤗%20Models-MMS--TTS--FAS-FFD21E)](https://huggingface.co/facebook/mms-tts-fas)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/SoroushSoleimani/Persian-TTS-using-Neural-Persian-G2P-module?style=social)](https://github.com/SoroushSoleimani/Persian-TTS-using-Neural-Persian-G2P-module)

**یک سامانه ماژولار و پیشرفته برای تبدیل متن فارسی به گفتار با بهره‌گیری از ماژول آوایی (G2P) و معماری سنتز صوت VITS.**

[English](#english-overview) • [راهنمای فارسی](#راهنمای-فارسی) • [Architecture](docs/ARCHITECTURE.md) • [G2P Guide](docs/G2P_GUIDE.md) • [Benchmarks](docs/BENCHMARKS.md)

</div>

---

## Architecture Overview

<div align="center">
<img src="assets/architecture.jpg" alt="Persian TTS Architecture" width="100%">
</div>

The system features a decoupled, two-stage neural pipeline:
1. **Persian Text Normalizer & G2P Module:** Resolves orthographic ambiguities, short vowels, and homographs.
2. **VITS Acoustic Model & Vocoder:** End-to-end waveform generation via variational inference, normalizing flows, and HiFi-GAN adversarial decoder.

---

## English Overview

### Key Features
- **Zero Training Required for Quickstart:** Integrates pretrained checkpoint (`facebook/mms-tts-fas`) out of the box.
- **Full Research Pipeline Included:** Jupyter notebooks covering G2P neural training, text corpus analysis, acoustic feature extraction, and VITS training.
- **Modular Python Package:** Clean package structure under `src/persian_tts` with CLI and Python APIs.
- **Hardware Agnostic:** Automatic GPU (CUDA) detection with seamless CPU fallback.

### Quickstart

#### 1. Installation
```bash
git clone https://github.com/SoroushSoleimani/Persian-TTS-using-Neural-Persian-G2P-module.git
cd Persian-TTS-using-Neural-Persian-G2P-module
pip install -r requirements.txt
```

#### 2. Run Inference
```bash
# Using the convenience script
python synth.py text.txt output.wav

# Or using the package CLI
python -m persian_tts.cli --text "سلام، به دنیای هوش مصنوعی خوش آمدید." -o output.wav
```

#### 3. Python API
```python
from persian_tts import PersianTTS

tts = PersianTTS()
audio_path = tts.synthesize_to_file("این یک متن نمونه به زبان فارسی است.", "persian_speech.wav")
print(f"Saved audio: {audio_path}")
```

---

## راهنمای فارسی

### ویژگی‌های سامانه
- **آماده به کار بدون نیاز به آموزش:** امکان سنتز فوری با مدل‌های آموزش‌دیده.
- **پوشش کامل خط لوله پژوهشی:** شامل نوت‌بوک‌های آموزش مدل آوایی G2P، آنالیز متنی، تحلیل سیگنال صوتی و ترین مدل VITS در پوشه `notebooks/`.
- **نرمال‌سازی پیشرفته خط فارسی:** تصحیح حروف عربی، نیم‌فاصله (ZWNJ) و اعراب‌گذاری.
- **رابط متنی (CLI) و پایتون:** امکان استفاده مستقیم در پروژه‌های پردازش زبان طبیعی و گفتار.

### نحوه اجرا

```bash
# نصب وابستگی‌ها
pip install -r requirements.txt

# تولید صوت از فایل متنی
python synth.py text.txt output.wav

# حالت تعاملی (Interactive Mode)
python -m persian_tts.cli --interactive
```

---

## Repository Structure

```
├── assets/                  # Architecture diagrams and visual media
│   └── architecture.jpg
├── configs/                 # YAML and JSON configs for audio and G2P
│   ├── default_config.yaml
│   ├── g2p_rules.json
│   └── phoneme_map.json
├── docs/                    # Deep-dive documentation
│   ├── API_REFERENCE.md
│   ├── ARCHITECTURE.md
│   ├── BENCHMARKS.md
│   └── G2P_GUIDE.md
├── notebooks/               # Jupyter research and training notebooks
│   ├── 01_persian_g2p_research.ipynb
│   ├── 02_text_corpus_analysis.ipynb
│   ├── 03_speech_acoustic_analysis.ipynb
│   ├── 04_vits_training_and_evaluation.ipynb
│   ├── 05_dataset_preparation.ipynb
│   └── 06_inference_quickstart.ipynb
├── samples/                 # Test sentences and reference output audio
│   ├── input_texts.txt
│   └── sample_output.wav
├── src/persian_tts/         # Core Python package
│   ├── audio/               # Waveform normalization and processing
│   ├── g2p/                 # Rule-based and Neural G2P phonemizer
│   ├── models/              # VITS acoustic synthesizer wrapper
│   ├── cleaner.py           # Persian text normalization
│   ├── cli.py               # Command-line interface
│   ├── config.py            # Dataclass configurations
│   └── pipeline.py          # Unified synthesis pipeline
├── tests/                   # Automated unit and integration tests
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── setup.py
├── synth.py                 # Convenience script
└── text.txt                 # Default Persian text input
```

---

## Citation & Acknowledgments
If you find this repository useful in your academic or practical work, please cite:

```bibtex
@misc{soleimani2026persiantts,
  author = {Soleimani, Soroush},
  title = {Persian-TTS-using-Neural-Persian-G2P-module},
  year = {2026},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/SoroushSoleimani/Persian-TTS-using-Neural-Persian-G2P-module}}
}
```

## License
This project is open-source and released under the [MIT License](LICENSE).
