import telebot
import sqlite3
from datetime import datetime, timedelta
import calendar
import os
import time

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

def init_db():
    conn = sqlite3.connect('calendar.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT,
        event_date TEXT,
        event_time TEXT,
        repeat_type TEXT DEFAULT "none",
        repeat_param INTEGER
    )''')
    conn.commit()
    conn.close()

init_db()

def main_keyboard():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("➕ Добавить событие", "📖 Ежедневник")
    markup.add("📅 Ближайшие 30 дней")
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "✅ Бот работает!\nИспользуй кнопки ниже.", reply_markup=main_keyboard())

@bot.message_handler(func=lambda m: True)
def all_messages(message):
    bot.send_message(message.chat.id, "Пока работает только /start. Полный функционал добавим позже.", reply_markup=main_keyboard())

print("Бот запущен на Render...")
bot.infinity_polling()
