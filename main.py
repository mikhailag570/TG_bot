import requests
from datetime import datetime
import telebot
from token_data import token


def get_data():
    # Отправим гет-запрос
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    
    # Зададим переменную
    sell_price = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")
    
    
def telegram_bot(token):
    bot = telebot.TeleBot(token)
    
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Привет друг! Напиши "price" и получишь стоимость биткоина')
        
    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == 'price':
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                sell_price = response["btc_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Черт... Что-то пошло не так..."
                )
        else:
            bot.send_message(message.chat.id, "Что??? Проверь команду, чувак!")
    
    bot.polling()
    
if __name__ == '__main__':
    # get_data()
    telegram_bot(token)
    
    