import requests
import json
import telebot
from config import *

message: telebot.types.Message

class ApiException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        try:
            quote_key = keys[quote.lower()]
        except KeyError:
            #bot.send_message(message.chat.id, f"Валюта {quote} не найдена!")
            raise ApiException(f"Валюта {quote} не найдена!")
        try:
            base_key = keys[base.lower()]
        except KeyError:
            #bot.send_message(message.chat.id, f'Валюта {base} не найдена!')
            raise ApiException(f"Валюта {base} не найдена!")
        if base_key == quote_key:
            #bot.send_message(message.chat.id, f'Введены одинаковые валюты- {base}!')
            raise ApiException(f"Невозможно перевести одинаковые валюты {base}!")
        try:
            amount = float(amount)
        except ValueError:
            #bot.send_message(message.chat.id, f'Не удалось обработать количество {amount}!')
            raise ApiException(f"Не удалось обработать количество {amount}!")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_key}&tsyms={base_key}')
        total_base = json.loads(r.content)[keys[base]]
        message = f"Цена {amount} {quote} в {base} : {total_base}"
        return message

