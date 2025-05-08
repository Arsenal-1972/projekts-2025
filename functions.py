import pytest
from deep_translator import GoogleTranslator

def translation(text, target_lang):
    translation_result = ""
    translator = GoogleTranslator(source='auto', target=target_lang)
    translated = translator.translate(text)
    detected_lang_code = translator.source
    lang_label = "krievu 🇷🇺" if target_lang == 'ru' else "latviešu 🇱🇻"
    translation_result = f"🌍 Noteiktā valoda: `{detected_lang_code}`\n\n🔄 Tulkojums {lang_label}:\n{translated}"
    return translation_result
