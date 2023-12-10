import requests
import csv
import os
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_data(category_id):
    params = {
        'searchType': 'category',
        'store': 'Sears',
        'storeId': 10153,
        'catGroupId': category_id,
    }
    user_agent = UserAgent()
    headers = {
        'Authorization': 'SEARS',
        'User-Agent': user_agent.random
    }
    response = requests.get('https://www.sears.com/api/sal/v3/products/search', headers=headers, params=params)

    return response.json()


def write_to_csv(category_id, data):
    current_directory = os.path.dirname(__file__)
    directory = os.path.join(current_directory, '.')
    if not os.path.exists(directory):
        os.makedirs(directory)

    headers = ["BrandName", "Name", "Category", "FinalPrice"]
    csv_filename = os.path.join(directory, f'{category_id}_products.csv')

    file_exists = os.path.exists(csv_filename)

    with open(csv_filename, 'a+', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)

        if not file_exists:
            writer.writeheader()

        for product in data.get('items', []):
            writer.writerow({
                'BrandName': product.get('brand', ''),
                'Name': product.get('name', ''),
                'Category': product.get('category', ''),
                'FinalPrice': product.get('final_price', ''),
            })


def start():
        category_id = input("введи category id: ")
        data = get_data(category_id)
        write_to_csv(category_id, data)
        print('Шалость  удалась')


start()