"""1. Додайте до банкомату меню отримання поточного курсу валют
за допомогою requests (можна використати відкрите API ПриватБанку)
https://api.privatbank.ua/#p24/exchange
"""
import urllib.request
import json


def get_currency_exchange():
    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        for currency in data:
            print(f"{currency['ccy']}/{currency['base_ccy']} "
                  f"Buy: {currency['buy']} Sale: {currency['sale']}")


get_currency_exchange()
# завжди виводить курси про роботі банкомату - не баг а фіча