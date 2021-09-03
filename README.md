## Telegram Bot Trial

#### TeleBot library for Telegram
```
from telebot import TeleBot
```
#### Telegram Bot token that took from BotFather
```
Bot_Token = "Bot_token_numbers"  
```
#### Chat_ID between user and bot
for take it; *https://api.telegram.org/bot`YourBOTToken`/getUpdates*
```
chat_id = "Chat_ID"              
```
### Calling method into "Bot"
```
Bot = TeleBot(Bot_Token) 
```
### Message sending to user's chat from bot
```
Bot.send_message(chat_id,"message") 
```
