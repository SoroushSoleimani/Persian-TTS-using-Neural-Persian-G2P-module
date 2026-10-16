import unittest
from persian_tts.cleaner import PersianTextCleaner

class TestPersianCleaner(unittest.TestCase):
    def setUp(self):
        self.cleaner = PersianTextCleaner(remove_diacritics=True)

    def test_character_normalization(self):
        raw = "كتاب ياسمين با پنجره‌های آبی"
        expected = "کتاب یاسمین با پنجره‌های آبی"
        self.assertEqual(self.cleaner.clean(raw), expected)

    def test_diacritic_removal(self):
        raw = "سَلامُ عَلَیکُم"
        expected = "سلام علیکم"
        self.assertEqual(self.cleaner.clean(raw), expected)

    def test_whitespace_and_zwnj(self):
        raw = "می‌‌‌روم    به خانه"
        res = self.cleaner.clean(raw)
        self.assertIn("می‌روم به خانه", res)

if __name__ == "__main__":
    unittest.main()
