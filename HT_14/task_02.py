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


def validate_date(input_date):
    try:
        if "-" in input_date:
            input_date = input_date.replace("-", ".")
        elif "," in input_date:
            input_date = input_date.replace(",", ".")

        date = datetime.datetime.strptime(input_date, "%d.%m.%Y")
        return date.strftime("%d.%m.%Y")
    except ValueError:
        print("Неправильний формат дати. Спробуйте ще раз.")
        return None


def get_currency_exchange_by_date(date, currencies):
    url = f'https://api.privatbank.ua/p24api/exchange_rates?date={date}'
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            if 'exchangeRate' in data:
                for exchange_rate in data['exchangeRate']:
                    if exchange_rate.get('currency') in currencies:
                        if 'saleRate' in exchange_rate:
                            base_currency = exchange_rate.get('baseCurrencyLit', data.get('baseCurrency'))
                            sale_rate = exchange_rate['saleRate']
                            currency = exchange_rate['currency']
                            print(f"On {date}, 1 {base_currency} equals {sale_rate} {currency} (sale rate)")
                        else:
                            print(f"No sale rate available for {exchange_rate['currency']} on {date}")
            else:
                print("No exchange rates available for the provided date.")
    except urllib.error.URLError as e:
        print(f"Error accessing the API: {e.reason}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_currency_exchange():
    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        for currency in data:
            print(f"{currency['ccy']}/{currency['base_ccy']} Купівля: {currency['buy']} Продаж: {currency['sale']}")


def get_currency_interval_exchange():
    start_date = validate_date(input("Введіть початкову дату (у форматі дд.мм.ррррр): "))
    end_date = validate_date(input("Введіть кінцеву дату (у форматі дд.мм.ррррр): "))

    currencies_dict = {
        'USD': 'долар США',
        'EUR': 'євро',
        'CHF': 'швейцарський франк',
        'GBP': 'британський фунт',
        'PLZ': 'польський злотий',
        'SEK': 'шведська крона',
        'XAU': 'золото',
        'CAD': 'канадський долар'
    }

    print("Доступні валюти для вибору:")
    for key, value in currencies_dict.items():
        print(f"{key} - {value}")

    chosen_currency = input("Оберіть валюту з переліку: ").upper()
    while chosen_currency not in currencies_dict:
        print("Оберіть валюту з переліку!")
        chosen_currency = input("Оберіть валюту з переліку: ").upper()

    if start_date and end_date:
        current_date = start_date
        while current_date <= end_date:
            get_currency_exchange_by_date(current_date, [chosen_currency])
            current_date += datetime.timedelta(days=1)
    else:
        print("Дані введено неправильно. Перевірте формат введених даних.")



def start():
    while True:
        print(f"\nВітаємо вас у програмі для отримання курсу валют спс пріватбанку")
        print("Виберіть потрібну вам дію")
        print("1 - Отримати курс на сьогодні")
        print("2 - Отримати курс на певну дату по валютам: USD, EUR, PLN")
        print("3 - Отримати курс валют за певний період")
        print("5 - Вийти з програми")

        choice = input("Ваш вибір: ")
        if choice == "1":
            get_currency_exchange()
        elif choice == "2":
            currencies = ['USD', 'EUR', 'PLN']
            date_input = validate_date(input("Введіть дату (у форматі дд.мм.ррррр): "))
            get_currency_exchange_by_date(date_input, currencies)
        elif choice == "3":
            get_currency_interval_exchange()
        elif choice == "5":
            print("До побачення!")
            exit()
        else:
            print("Неправильний вибір. Спробуйте ще раз.")


start()


#validate_date("12-12-2012")



    #currencies = ['USD', 'EUR', 'PLN', 'UAH']  # Ви можете змінити ці валюти на потрібні вам
    #get_currency_exchange_by_date(input_date, currencies)

    # get_currency_exchange()
    # input_date = input("Введіть дату (у форматі дд.мм.рррр): ")
    # currencies = ['USD', 'EUR', 'PLN', 'UAH']  # Ви можете змінити ці валюти на потрібні вам
    # get_currency_exchange_by_date(input_date, currencies)