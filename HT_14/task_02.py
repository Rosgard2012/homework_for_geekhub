"""2. Створіть програму для отримання курсу валют за певний період.
- отримати від користувача дату (це може бути як один день так і інтервал -
початкова і кінцева дати, продумайте механізм реалізації) і назву валюти
- вивести курс по відношенню до гривні на момент вказаної дати (або за кожен
день у вказаному інтервалі)
- не забудьте перевірку на валідність введених даних"""

import requests
from datetime import datetime
import json


class API:
    def __init__(self, url):
        self.url = url

    def get_data(self, start_date, end_date, currency):
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        delta = end_date - start_date
        if delta.days < 0:
            raise ValueError("Start date can't be greater than end date")
        for i in range(delta.days + 1):
            date = start_date + timedelta(days=i)
            date = date.strftime('%Y-%m-%d')
            response = requests.get(f"{self.url}{date}")
            data = json.loads(response.text)
            print(f"{date}: {data['rates'][currency]}")

    def get_data_for_date(self, date, currency):
        response = requests.get(f"{self.url}{date}")
        data = json.loads(response.text)
        print(f"{date}: {data['rates'][currency]}")


api = API("https://api.exchangeratesapi.io/")
api.get_data_for_date("2021-01-01", "USD")
api.get_data("2021-01-01", "2021-01-05", "USD")
