import telebot
import os
import time

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    print("Ошибка: BOT_TOKEN не найден!")
    exit(1)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Бот успешно запущен на Render!\n\nКоманды работают.")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "Бот работает. /start")

print("Бот запущен...")
bot.infinity_polling()
