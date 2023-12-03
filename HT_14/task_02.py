"""2. Створіть програму для отримання курсу валют за певний період.
- отримати від користувача дату (це може бути як один день так і інтервал -
початкова і кінцева дати, продумайте механізм реалізації) і назву валюти
- вивести курс по відношенню до гривні на момент вказаної дати (або за кожен
день у вказаному інтервалі)
- не забудьте перевірку на валідність введених даних
https://api.privatbank.ua/#p24/exchangeArchive
"""

import urllib.request
import json
import datetime

def get_currency_exchange_by_date(date, currencies):
    url = f'https://api.privatbank.ua/p24api/exchange_rates?date={date}'
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        for exchange_rate in data['exchangeRate']:
            if exchange_rate['currency'] in currencies:
                print(
                    f"On {date}, 1 {exchange_rate['baseCurrencyLit']} "
                    f"equals {exchange_rate['saleRate']} "
                    f"{exchange_rate['currency']} (sale rate)")

def get_currency_exchange():
    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        for currency in data:
            print(f"{currency['ccy']}/{currency['base_ccy']} Buy: {currency['buy']} Sale: {currency['sale']}")

def start():
    while True:
        print(f"\nВітаємо вас у програмі для отримання курсу валют спс пріватбанку")
        print("Виберіть потрібну вам дію")
        print("1 - Отримати курс на сьогодні")
        print("2 - Отримати курс на певну дату по валютам: USD, EUR, PLN, UAH")
        print("3 - Отримати курс валют за певний період")

        print("5 - Вийти з програми")

        choice = input("Ваш вибір: ")
        if choice == "1":
            get_currency_exchange()
        elif choice == "2":
            currencies = ['USD', 'EUR', 'PLN', 'UAH']
            date_input = input("Введіть дату (у форматі дд.мм.рррр): ")
        elif choice == "3":
            date_input = input("Введіть дату (у форматі дд.мм.рррр): ")
            currencies = ['USD', 'EUR', 'PLN', 'UAH']
            get_currency_exchange_by_date(date_input, currencies)
        elif choice == "5":
            print("До побачення!")
            exit()
        else:
            print("Неправильний вибір. Спробуйте ще раз.")
            start()

start()



    #currencies = ['USD', 'EUR', 'PLN', 'UAH']  # Ви можете змінити ці валюти на потрібні вам
    #get_currency_exchange_by_date(input_date, currencies)

    # get_currency_exchange()
    # input_date = input("Введіть дату (у форматі дд.мм.рррр): ")
    # currencies = ['USD', 'EUR', 'PLN', 'UAH']  # Ви можете змінити ці валюти на потрібні вам
    # get_currency_exchange_by_date(input_date, currencies)