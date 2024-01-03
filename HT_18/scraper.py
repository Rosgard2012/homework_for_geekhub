import os
import csv
import time
import requests
from requests import Response
from fake_useragent import UserAgent


def process_data(identifier: int) -> None:
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, f"{identifier}_products.csv")
    with open(file_path, "w", encoding="utf-8", newline="") as csvfile:
        columns = ["brand", "name", "old_price", "new_price", "store"]
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()

        start_index = 1
        end_index = 200

        while True:
            response = fetch_response(start_index=start_index, end_index=end_index, identifier=identifier)

            try:
                response.raise_for_status()
            except Exception as e:
                print("Ви дійшли до кінця категорії або сталася помилка. Перевірте csv-файл.")
                print(f"Помилка: {e}")
                break

            category_items = response.json().get("items")
            for item in category_items:
                writer.writerow(
                    {
                        "brand": item.get("brandName"),
                        "name": item.get("name"),
                        "old_price": item.get("additionalAttributes").get("cutPrice"),
                        "new_price": item.get("additionalAttributes").get("displayPrice"),
                        "store": item.get("additionalAttributes").get("storeOrigin")[0],
                    }
                )
            start_index += 200
            end_index += 200
            time.sleep(2)


def fetch_response(start_index: int, end_index: int, identifier: int) -> Response:
    user_agent = UserAgent()
    headers = {
        "authority": "www.sears.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6",
        "authorization": "SEARS",
        "content-type": "application/json",
        'User-Agent': user_agent.random,
    }
    response = requests.get(
        f"https://www.sears.com/api/sal/v3/products/search?startIndex={start_index}&"
        f"endIndex={end_index}&searchType=category"
        f"&catalogId=12605&store=Sears&storeId=10153&filterValueLimit=500&catGroupId={identifier}",
        headers=headers,
    )
    return response


def start():
#    current_directory = os.path.dirname(__file__)
    category_id = input("Введіть ID категорії ( 1025184 , 1020022 ): ")
    process_data(int(category_id))
    print('Дані успішно збережено у файлі!')


start()