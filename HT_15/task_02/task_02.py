import csv
import random
import time
import os
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_domains() -> None:
    domain_num = 0
    max_domains = 75

    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "deleted_domains.csv")

    with open(file_path, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["domain_name"])

        while domain_num < max_domains:
            print(f"Getting domain names from {domain_num} to {domain_num + 25}")
            response = get_response(domain_num=domain_num)
            soup = BeautifulSoup(response.text, "lxml")

            if not soup.select_one(".field_domain"):
                print("End of domain list or you were blocked. Check the CSV file")
                break

            domains = soup.select(".field_domain")
            writer.writerows([[domain.text] for domain in domains])
            domain_num += 25
            time.sleep(random.uniform(5, 15))


def get_response(domain_num: int) -> requests.Response:
    user_agent = UserAgent()
    headers = {
        'User-Agent': user_agent.random
    }
    params = {"start": domain_num}
    response = requests.get(
        "https://www.expireddomains.net/deleted-domains/", params=params, headers=headers
    )
    return response


get_domains()
