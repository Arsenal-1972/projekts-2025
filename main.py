import telebot
from telebot import types
from deep_translator import GoogleTranslator

TOKEN = '7544879884:AAHN6d5uOU-ELlbjFYgOJ1D2GtIxNGlfH0I'
bot = telebot.TeleBot(TOKEN)

user_language_preferences = {}

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Tulkot krievu valodā")
    btn2 = types.KeyboardButton("🇱🇻 Tulkot latviešu valodā")
    markup.add(btn1, btn2)
    bot.send_message(
        message.chat.id,
        "👋 Sveiki! Es palīdzēšu pārtulkot jebkuru tekstu.\n\nLūdzu, izvēlies valodu, kurā vēlies tulkot. Valodu vēlāk var mainīt ar komandu /language:",
        reply_markup=markup
    )

@bot.message_handler(commands=['language'])
def choose_language(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Tulkot krievu valodā")
    btn2 = types.KeyboardButton("🇱🇻 Tulkot latviešu valodā")
    markup.add(btn1, btn2)
    bot.send_message(
        message.chat.id,
        "🌐 Lūdzu, izvēlies valodu, uz kuru vēlies tulkot ziņas:",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text in ["🇷🇺 Tulkot krievu valodā", "🇱🇻 Tulkot latviešu valodā"])
def set_language(message):
    if "krievu" in message.text:
        user_language_preferences[message.chat.id] = 'ru'
        bot.send_message(message.chat.id, "✅ Izvēlēta tulkošanas valoda: krievu 🇷🇺")
    elif "latviešu" in message.text:
        user_language_preferences[message.chat.id] = 'lv'
        bot.send_message(message.chat.id, "✅ Izvēlēta tulkošanas valoda: latviešu 🇱🇻")

@bot.message_handler(func=lambda message: True)
def translate(message):
    try:
        if message.chat.id not in user_language_preferences:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            btn1 = types.KeyboardButton("🇷🇺 Tulkot krievu valodā")
            btn2 = types.KeyboardButton("🇱🇻 Tulkot latviešu valodā")
            markup.add(btn1, btn2)
            bot.send_message(
                message.chat.id,
                "❗ Lūdzu, izvēlies tulkošanas valodu pirms sūti tekstu:",
                reply_markup=markup
            )
            return

        target_lang = user_language_preferences[message.chat.id]

        translator = GoogleTranslator(source='auto', target=target_lang)
        translated = translator.translate(message.text)
        detected_lang_code = translator.source

        lang_label = "krievu 🇷🇺" if target_lang == 'ru' else "latviešu 🇱🇻"

        bot.send_message(
            message.chat.id,
            f"🌍 Noteiktā valoda: `{detected_lang_code}`\n\n🔄 Tulkojums {lang_label}:\n{translated}",
            parse_mode='Markdown'
        )

    except Exception as e:
        print("Kļūda:", e)
        bot.send_message(message.chat.id, "❌ Radās kļūda tulkojot. Lūdzu, mēģini vēlreiz vēlāk.")

bot.polling()
