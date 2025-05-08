import pytest

from functions import translation

# def test_translate_english_to_russian():
#     translated, detected_lang = GoogleTranslator("Hello, how are you?", "ru")
#     assert detected_lang == "en"
#     assert isinstance(translated, str)
#     assert len(translated) > 0

# def test_translate_french_to_latvian():
#     translated, detected_lang = GoogleTranslator("Bonjour tout le monde", "lv")
#     assert detected_lang == "fr"
#     assert "sveiki" in translated.lower() or "labdien" in translated.lower()

# def test_single_character_input():
#     translated, detected_lang = GoogleTranslator("a", "lv")
#     assert isinstance(translated, str)
#     assert len(translated) > 0

# def test_special_characters_input():
#     translated, detected_lang = GoogleTranslator("Hallo!", "ru")
#     assert detected_lang == "de"
#     assert isinstance(translated, str)

#Hapy path tests:
def test_translation_de_to_lv():
    result = translation("der Spion", "lv")
    expected_result = """🌍 Noteiktā valoda: `auto`

🔄 Tulkojums latviešu 🇱🇻:
spiegs"""

    assert result == expected_result
def test_transaltion_fr_to_lv():
    result = translation("Потужно", "ru")
    expected_result = """🌍 Noteiktā valoda: `auto`

🔄 Tulkojums krievu 🇷🇺:
Мощно"""
    assert result == expected_result
# Use case test:
def test_translator_use_case_test():
    result = translation("Hola!!!","lv")
    expected_result = """🌍 Noteiktā valoda: `auto`

🔄 Tulkojums latviešu 🇱🇻: Labdien
"""

# Edge case test:
def test_translator_only_symbols():
    result = translation("!!!", "ru")
    expected_result = """🌍 Noteiktā valoda: `auto`
🔄 Tulkojums krievu 🇷🇺:
None"""
    assert result == expected_result
