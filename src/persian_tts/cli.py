"""
Command-line interface for Persian TTS.
"""

import sys
import argparse
from pathlib import Path
from .pipeline import PersianTTS
from .config import TTSConfig

def parse_args():
    parser = argparse.ArgumentParser(description="Persian Text-to-Speech (TTS) Synthesizer")
    parser.add_argument("-t", "--text", type=str, help="Persian text string to synthesize")
    parser.add_argument("-f", "--file", type=str, help="Path to UTF-8 text file containing Persian input")
    parser.add_argument("-o", "--output", type=str, default="output.wav", help="Output .wav destination")
    parser.add_argument("--cuda", action="store_true", help="Force CUDA device")
    return parser.parse_args()

def main():
    args = parse_args()
    if not args.text and not args.file:
        print("Error: Specify either --text or --file. Run with --help for details.")
        sys.exit(1)

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read().strip()
    else:
        text = args.text

    cfg = TTSConfig()
    if args.cuda:
        cfg.model.device = "cuda"

    tts = PersianTTS(cfg)
    print(f"Synthesizing: {text[:60]}...")
    out = tts.synthesize_to_file(text, args.output)
    print(f"Audio saved to: {out}")

if __name__ == "__main__":
    main()
