"""
Convenience entrypoint script for Persian TTS.
Reads input from text.txt or CLI argument and writes to output.wav.
"""

import sys
from pathlib import Path
from persian_tts import PersianTTS

def main():
    text_file = sys.argv[1] if len(sys.argv) > 1 else "text.txt"
    output_wav = sys.argv[2] if len(sys.argv) > 2 else "output.wav"

    input_path = Path(text_file)
    if input_path.exists():
        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read().strip()
    else:
        text = text_file

    tts = PersianTTS()
    tts.synthesize_to_file(text, output_wav)
    print(f"Generated audio saved to: {output_wav}")

if __name__ == "__main__":
    main()
