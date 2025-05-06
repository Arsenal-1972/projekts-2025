# test_translator.py
import pytest
from translator_module import translate_text

def test_english_to_russian():
    translated, lang = translate_text("Hello")
    assert lang == "en"
    assert "Привет" in translated or "Здравствуйте" in translated

def test_french_to_russian():
    translated, lang = translate_text("Bonjour")
    assert lang == "fr"
    assert "Доброе" in translated or "Привет" in translated

def test_short_input():
    translated, lang = translate_text("a")
    assert isinstance(translated, str)
    assert len(translated) > 0

def test_special_characters():
    translated, lang = translate_text("😊 Hallo!")
    assert lang == "de"
    assert isinstance(translated, str)
