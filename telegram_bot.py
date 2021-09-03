"""
author: Berkay Karadeniz

Telegram Bot Trial 
"""
from telebot import TeleBot 

Bot_Token = "Bot_token_numbers" 
chat_id = "Chat_ID"              

Bot = TeleBot(Bot_Token) 

Bot.send_message(chat_id,"message")
