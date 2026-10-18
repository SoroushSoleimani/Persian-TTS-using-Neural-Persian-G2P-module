import unittest
from unittest.mock import MagicMock, patch
import numpy as np
from persian_tts.pipeline import PersianTTS

class TestPipeline(unittest.TestCase):
    @patch("persian_tts.models.vits.VitsModel")
    @patch("persian_tts.models.vits.AutoTokenizer")
    def test_pipeline_dry_run(self, mock_tok, mock_model):
        tts = PersianTTS()
        # Mock synthesizer output
        tts.synthesizer.synthesize = MagicMock(return_value=np.array([0.1, 0.5, -0.3], dtype=np.float32))
        res = tts.synthesize("تست سامانه سنتز گفتار")
        self.assertEqual(len(res), 3)

if __name__ == "__main__":
    unittest.main()
