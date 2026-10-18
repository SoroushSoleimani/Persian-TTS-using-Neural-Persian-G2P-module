import unittest
import numpy as np
from persian_tts.audio import AudioProcessor

class TestAudioProcessor(unittest.TestCase):
    def test_normalize_peak(self):
        sig = np.array([0.1, -0.5, 0.2], dtype=np.float32)
        norm = AudioProcessor.normalize_peak(sig, target_peak=1.0)
        self.assertAlmostEqual(np.max(np.abs(norm)), 1.0, places=5)

    def test_trim_silence(self):
        sig = np.array([0.0, 0.0, 0.8, -0.5, 0.0, 0.0], dtype=np.float32)
        trimmed = AudioProcessor.trim_silence(sig, threshold=0.01)
        self.assertEqual(len(trimmed), 2)

if __name__ == "__main__":
    unittest.main()
