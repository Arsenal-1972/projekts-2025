import telebot
from telebot import types
from deep_translator import GoogleTranslator

TOKEN = '7544879884:AAHN6d5uOU-ELlbjFYgOJ1D2GtIxNGlfH0I'
bot = telebot.TeleBot(TOKEN)
# Saglabā lietotāja izvēlēto mērķa valodu tulkošanai pēc chat.id
user_language_preferences = {}

# Funkcija, kas tiek izsaukta, kad lietotājs ievada komandu /start
# Parāda sveicienu un piedāvā izvēlēties tulkošanas valodu
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
    
# Funkcija, kas tiek izsaukta, kad lietotājs ievada komandu /language
# Atļauj mainīt tulkošanas mērķa valodu
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

# Funkcija, kas apstrādā lietotāja izvēlēto tulkošanas valodu no pogām
# Saglabā izvēlēto valodu vārdnīcā user_language_preferences
@bot.message_handler(func=lambda message: message.text in ["🇷🇺 Tulkot krievu valodā", "🇱🇻 Tulkot latviešu valodā"])
def set_language(message):
    if "krievu" in message.text:
        user_language_preferences[message.chat.id] = 'ru'
        bot.send_message(message.chat.id, "✅ Izvēlēta tulkošanas valoda: krievu 🇷🇺")
    elif "latviešu" in message.text:
        user_language_preferences[message.chat.id] = 'lv'
        bot.send_message(message.chat.id, "✅ Izvēlēta tulkošanas valoda: latviešu 🇱🇻")


# Galvenā funkcija, kas izpilda tulkošanu, kad lietotājs nosūta jebkuru ziņu
# Ja valoda nav izvēlēta — piedāvā izvēlēties
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
# Iegūst lietotāja izvēlēto mērķa valodu
        target_lang = user_language_preferences[message.chat.id]
# Izmanto GoogleTranslator, lai noteiktu ievades valodu un pārtulkotu uz mērķa valodu
        translator = GoogleTranslator(source='auto', target=target_lang)
        translated = translator.translate(message.text)
        detected_lang_code = translator.source
        
# Lietotājam saprotama valodas nosaukuma forma
        lang_label = "krievu 🇷🇺" if target_lang == 'ru' else "latviešu 🇱🇻"
# Nosūta lietotājam atbildi ar noteikto valodu un tulkojumu
        bot.send_message(
            message.chat.id,
            f"🌍 Noteiktā valoda: `{detected_lang_code}`\n\n🔄 Tulkojums {lang_label}:\n{translated}",
            parse_mode='Markdown'
        )

    except Exception as e:
        # Ja radusies kļūda — tiek izvadīta konsolē un nosūtīts kļūdas paziņojums lietotājam
        print("Kļūda:", e)
        bot.send_message(message.chat.id, "❌ Radās kļūda tulkojot. Lūdzu, mēģini vēlreiz vēlāk.")

bot.polling() # Startē bota notikumu ciklu (gaida ziņas no lietotājiem)
