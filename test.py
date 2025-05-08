import pytest
from main import translate_text

def test_translate_english_to_russian():
    translated, detected_lang = translate_text("Hello, how are you?", "ru")
    assert detected_lang == "en"
    assert isinstance(translated, str)
    assert len(translated) > 0

def test_translate_french_to_latvian():
    translated, detected_lang = translate_text("Bonjour tout le monde", "lv")
    assert detected_lang == "fr"
    assert "sveiki" in translated.lower() or "labdien" in translated.lower()

def test_single_character_input():
    translated, detected_lang = translate_text("a", "lv")
    assert isinstance(translated, str)
    assert len(translated) > 0

def test_special_characters_input():
    translated, detected_lang = translate_text("Hallo!", "ru")
    assert detected_lang == "de"
    assert isinstance(translated, str)
