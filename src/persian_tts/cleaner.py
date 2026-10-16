"""
Persian text cleaner and character normalizer.
Handles Arabic-to-Persian character unification, ZWNJ normalization, and punctuation.
"""

import re
import unicodedata

class PersianTextCleaner:
    ARABIC_TO_PERSIAN_MAP = {
        'ي': 'ی',
        'ى': 'ی',
        'ك': 'ک',
        'ة': 'ه',
        'ۀ': 'هٔ',
        'ؤ': 'و',
        'إ': 'ا',
        'أ': 'ا',
        'آ': 'آ',
    }

    DIACRITICS = [
        'َ',  # Fatha (a)
        'ِ',  # Kasra (e)
        'ُ',  # Damma (o)
        'ّ',  # Tashdid
        'ً',  # Tanwin Fatha
        'ٌ',  # Tanwin Damma
        'ٍ',  # Tanwin Kasra
        'ْ',  # Sukun
    ]

    ZWNJ = '‌'

    def __init__(self, remove_diacritics: bool = False):
        self.remove_diacritics = remove_diacritics

    def normalize_characters(self, text: str) -> str:
        for ar, fa in self.ARABIC_TO_PERSIAN_MAP.items():
            text = text.replace(ar, fa)
        return text

    def strip_diacritics(self, text: str) -> str:
        for dia in self.DIACRITICS:
            text = text.replace(dia, '')
        return text

    def clean(self, text: str) -> str:
        text = unicodedata.normalize('NFKC', text)
        text = self.normalize_characters(text)
        if self.remove_diacritics:
            text = self.strip_diacritics(text)
        text = re.sub(r'[\s]+', ' ', text)
        text = re.sub(r'‌{2,}', self.ZWNJ, text)
        return text.strip()
