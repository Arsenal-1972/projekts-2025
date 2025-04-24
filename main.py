import telebot
from deep_translator import GoogleTranslator

TOKEN = '7544879884:AAHN6d5uOU-ELlbjFYgOJ1D2GtIxNGlfH0I'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "👋 Привет! Отправь текст — я определю язык и переведу его на русский 🇷🇺")

@bot.message_handler(func=lambda message: True)
def translate(message):
    try:
        # Инициализация переводчика с автоматическим определением языка
        translator = GoogleTranslator(source='auto', target='ru')
        translated = translator.translate(message.text)

        # Вытаскиваем определённый язык из внутреннего состояния переводчика
        detected_lang_code = translator.source  # это работает, т.к. deep-translator сохраняет результат auto-определения

        bot.send_message(
            message.chat.id,
            f"🌍 Обнаружен язык: `{detected_lang_code}`\n\n🔄 Перевод на русский:\n{translated}",
            parse_mode='Markdown'
        )

    except Exception as e:
        print("Ошибка:", e)
        bot.send_message(message.chat.id, "❌ Ошибка при переводе. Попробуй позже.")

bot.polling()