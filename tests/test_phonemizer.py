import unittest
from persian_tts.g2p import RuleBasedPhonemizer, HybridPhonemizer

class TestPhonemizer(unittest.TestCase):
    def test_rule_based(self):
        p = RuleBasedPhonemizer()
        res = p.phonemize("سلام")
        self.assertIn("s", res)
        self.assertIn("l", res)
        self.assertIn("m", res)

    def test_custom_dictionary_override(self):
        h = HybridPhonemizer()
        h.register_word("خداحافظ", "xodɒːhɒːfez")
        self.assertEqual(h.phonemize("خداحافظ"), "xodɒːhɒːfez")

if __name__ == "__main__":
    unittest.main()
