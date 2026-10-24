# Persian Grapheme-to-Phoneme (G2P) Guide

## Linguistic Challenges in Persian Phonology
Persian writing is an abjad-derived alphabet that normally omits short vowels. This creates significant challenges for text-to-speech synthesis:

1. **Short Vowels:** /æ/ (فَتْحه), /e/ (کَسْره), and /o/ (ضَمّه) are not explicitly written in standard text.
2. **Homographs:** Words with identical spelling but different pronunciations and meanings:
   - سِر (/ser/ - secret) vs. سَر (/sær/ - head)
   - گِل (/gel/ - mud) vs. گُل (/gol/ - flower)
3. **Ezafe Construction:** The unstressed enclitic /-e/ linking nouns and adjectives is unwritten after consonants.
4. **Silent Letters:** Silent Vav in words like خواب (/xɒːb/), خواهر (/xɒːhær/).

## G2P Pipeline Architecture
The `persian_tts.g2p` package provides a hybrid fallback:
1. **Dictionary Lookup:** Exact match for common irregular words and homograph hints.
2. **Rule-Based Heuristics:** Morphological affix patterns for prefixes (میـ / نـ) and suffixes (ـها / ـتر / ـترین).
3. **Neural Seq2Seq Fallback:** Attention-based encoder-decoder for out-of-vocabulary words.
