
import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "سلام 👋\nبه ربات ما خوش اومدی!\n\nبرای شروع، پیام خودت رو برام بفرست."
    )

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(
        message,
        "پیامت دریافت شد ✅\nبه‌زودی امکانات بیشتری به ربات اضافه می‌کنیم."
    )

bot.infinity_polling()
