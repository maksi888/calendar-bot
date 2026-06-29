import telebot
import os
import time
from datetime import datetime

TOKEN = os.environ.get('BOT_TOKEN')

if not TOKEN:
    print("Ошибка: BOT_TOKEN не найден!")
    exit(1)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Бот успешно запущен!\n\nКоманды:\n/ежедневник - показать список\n/add - добавить событие")

@bot.message_handler(commands=['ежедневник', 'calendar'])
def show_calendar(message):
    calendar = """🟢 Платежи и подписки
2026.06.30 - Пополнить счёт интернет за июль (205 грн)
... (я могу сделать полный список)"""
    bot.reply_to(message, calendar, parse_mode="Markdown")

@bot.message_handler(commands=['add'])
def add_event(message):
    bot.reply_to(message, "Напиши событие в формате: дата - описание")

# Простой echo для тестирования
@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "Бот работает. Используй /ежедневник")

print("Бот запущен...")
bot.infinity_polling()
