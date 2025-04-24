from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from googletrans import Translator

# Инициализируем переводчик
translator = Translator()
# Обработка команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот-переводчик. Напиши мне любой текст, и я переведу его на английский язык. 🇬🇧"
    )
# Перевод текста
async def translate_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    try:
        translated = translator.translate(user_text, dest='en')  # перевод на английский
        await update.message.reply_text(f"Перевод: {translated.text}")
    except Exception as e:
        await update.message.reply_text(f"Ошибка перевода: {str(e)}")

# Основная функция запуска бота
if __name__ == '__main__':
    TOKEN = "7544879884:AAHVkvxJ3V3axeyiGJqYEJE4u6MJOw3gZjk"
    app = ApplicationBuilder().token(TOKEN).build()
    # Обработчики команд и текста
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_text))

    print("✅ Бот запущен и ждёт сообщений...")
    app.run_polling()