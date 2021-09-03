"""
author: Berkay Karadeniz

Telegram Bot Trial 
"""
from telebot import TeleBot # TeleBot library for Telegram

Bot_Token = "Bot_token_numbers"  #Telegram Bot token
chat_id = "Chat_ID"              #Chat_ID between user and bot

Bot = TeleBot(Bot_Token) #Calling method into "Bot"

Bot.send_message(chat_id,"message") # Message sending to user's chat from bot
