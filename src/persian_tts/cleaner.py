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

    DIGIT_MAP = {
        '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
        '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'
    }

    ZWNJ = '‌'

    def __init__(self, remove_diacritics: bool = False):
        self.remove_diacritics = remove_diacritics

    def normalize_characters(self, text: str) -> str:
        for ar, fa in self.ARABIC_TO_PERSIAN_MAP.items():
            text = text.replace(ar, fa)
        return text

    def clean(self, text: str) -> str:
        text = unicodedata.normalize('NFKC', text)
        text = self.normalize_characters(text)
        text = re.sub(r'[\s]+', ' ', text)
        text = re.sub(r'‌{2,}', self.ZWNJ, text)
        return text.strip()
