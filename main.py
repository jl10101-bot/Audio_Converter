#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import telebot
from flask import Flask
from threading import Thread
import os

TOKEN = os.environ.get('TELEGRAM_TOKEN', '8049296329:AAE0hX6QHE_BkBuTINrFrYNjfbzhrfc0H1U')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# لتجنب مشكلة الإصدارات
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

@app.route('/')
def home():
    return "☆ Bot is Running Successfully ☆"

def run_bot():
    bot.infinity_polling()

@bot.message_handler(commands=['start'])
def start_command_handler(message):
    start_message = """
_☆تم تشغيل البوت بنجاح☆_

تـم التـطــويـر بـواسـطــة :
✯ ᎷᎡｷᎫᎯᏦᎬᏞ ✯

قـم بأرسـال اي ملـف صوتـي و
سيتـم تحويلـه الى الصـيغة
المـناسـبة للـعـمل على البـوت : 
@JL_HK011101Sbot

* لتشغـيل المـلف الـصوتـي على
جهـاز الـهدف قـم بتـحويـله بشكـل 
مباشـل الـى بوت التحكـم
بعـد تشغيـل الأزرار...
"""
    bot.send_message(
        message.chat.id, 
        start_message, 
        parse_mode='Markdown'
    )

@bot.message_handler(content_types=['audio'])
def audio_handler(message):
    try:
        file_info = bot.get_file(message.audio.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        bot.send_voice(
            message.chat.id,
            downloaded_file,
            caption=message.caption,
            caption_entities=message.caption_entities
        )
    except Exception as e:
        print(f"حدث خطأ: {e}")
        bot.reply_to(message, "❌ حدث خطأ أثناء معالجة الصوت، يرجى المحاولة مرة أخرى")

if __name__ == "__main__":
    Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=8080)
