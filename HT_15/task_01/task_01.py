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
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        f'Referer': 'https://www.sears.com/category/b-{id}',
        'Content-Type': 'application/json',
        'Authorization': 'SEARS',
        'Alt-Used': 'www.sears.com',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'User-Agent': user_agent.random
    }
    response = requests.get('https://www.sears.com/api/sal/v3/products/search', headers=headers, params=params)

    return response.json()


def write_to_csv(category_id, data):
    current_directory = os.path.dirname(__file__)
    directory = os.path.join(current_directory)
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
                'brandName': product.get('brand', ''),
                'name': product.get('name', ''),
                'Category': product.get('category', ''),
                'FinalPrice': product.get('final_price', ''),
            })


def start():
        category_id = input("введи category id (1025184): ")
        data = get_data(category_id)
        write_to_csv(category_id, data)
        print('Шалость  удалась;)')


start()



#https://www.sears.com/api/sal/v3/products/search?startIndex=1&endIndex=48&searchType=category&catalogId=12605&store=Sears&storeId=10153&zipCode=10101&bratRedirectInd=true&catPredictionInd=true&disableBundleInd=true&filterValueLimit=500&includeFiltersInd=true&shipOrDelivery=true&solrxcatRedirection=true&sortBy=ORIGINAL_SORT_ORDER&whiteListCacheLoad=false&eagerCacheLoad=true&slimResponseInd=true&catGroupId=1020314&seoURLPath=appliances-refrigerators-single-door-bottom-freezer-refrigerators/1020314