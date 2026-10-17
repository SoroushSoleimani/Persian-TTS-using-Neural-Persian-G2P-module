import re
from .base import BasePhonemizer

class RuleBasedPhonemizer(BasePhonemizer):
    CHAR_PHONEME_MAP = {
        'آ': 'ɒː', 'ا': 'ɒː', 'ب': 'b', 'پ': 'p', 'ت': 't', 'ث': 's',
        'ج': 'dʒ', 'چ': 'tʃ', 'ح': 'h', 'خ': 'x', 'د': 'd', 'ذ': 'z',
        'ر': 'r', 'ز': 'z', 'ژ': 'ʒ', 'س': 's', 'ش': 'ʃ', 'ص': 's',
        'ض': 'z', 'ط': 't', 'ظ': 'z', 'ع': 'ʔ', 'غ': 'ɣ', 'ف': 'f',
        'ق': 'ɣ', 'ک': 'k', 'گ': 'ɡ', 'ل': 'l', 'م': 'm', 'ن': 'n',
        'و': 'v', 'ه': 'h', 'ی': 'j', 'ء': 'ʔ', 'ٔ': 'ʔ'
    }

    def phonemize(self, text: str) -> str:
        phonemes = []
        for char in text:
            if char in self.CHAR_PHONEME_MAP:
                phonemes.append(self.CHAR_PHONEME_MAP[char])
            elif char.isspace():
                phonemes.append(" ")
            else:
                phonemes.append(char)
        return "".join(phonemes)
