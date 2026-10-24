# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2026-10-23
### Added
- Complete modular package structure under `src/persian_tts`.
- Persian text normalizer with Arabic character correction and ZWNJ handling.
- Hybrid G2P phonemizer module with rule-based heuristics and neural adapter.
- VITS acoustic model synthesis wrapper leveraging Hugging Face Transformers.
- Audio processor with peak normalization and silence trimming.
- Interactive and batch command-line interface (`persian_tts.cli`).
- Comprehensive research notebooks covering G2P, speech analysis, and VITS training.
- High-resolution neural network architecture diagram and technical docs.
- Full test suite covering cleaner, phonemizer, audio, and pipeline integration.
- Bilingual (English & Persian) README with quickstart guides.
