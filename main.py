import telebot
from deep_translator import GoogleTranslator

TOKEN = '7544879884:AAHN6d5uOU-ELlbjFYgOJ1D2GtIxNGlfH0I'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "👋 Привет! Напиши мне текст, и я переведу его на английский.")

@bot.message_handler(func=lambda message: True)
def translate(message):
    try:
        translated = GoogleTranslator(source='auto', target='en').translate(message.text)
        bot.send_message(message.chat.id, f"🔄 Перевод:\n{translated}")
    except Exception as e:
        bot.send_message(message.chat.id, "❌ Ошибка при переводе. Попробуй снова позже.")

bot.polling()