"""
Persian TTS Package
===================
End-to-End Persian Text-to-Speech synthesis with Neural G2P and VITS acoustic model.
"""

__version__ = "1.0.0"
__author__ = "Soroush Soleimani"

from .cleaner import PersianTextCleaner
from .pipeline import PersianTTS

__all__ = ["PersianTextCleaner", "PersianTTS"]
