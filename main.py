from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from googletrans import Translator

translator = Translator()

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши мне текст, и я переведу его на английский.")

# Перевод текста
async def translate_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    original_text = update.message.text
    translated = translator.translate(original_text, dest='en')  # Перевод на английский
    await update.message.reply_text(f"Перевод: {translated.text}")

# Основной блок
if __name__ == '__main__':
    import os

    TOKEN = "7544879884:AAHVkvxJ3V3axeyiGJqYEJE4u6MJOw3gZjk"  # Замените на свой токен
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_text))

    print("Бот запущен...")
    app.run_polling()
