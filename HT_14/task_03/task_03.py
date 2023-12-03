import requests
from bs4 import BeautifulSoup
import csv

def scrape_quotes():
    csv_file = open('quotes.csv', 'w', newline='', encoding='utf-8')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Quote', 'Author', 'Born', 'Location', 'Description'])

    for page_num in range(1, 11):
        url = f'http://quotes.toscrape.com/page/{page_num}'
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            quotes = soup.find_all(class_='quote')

            for quote in quotes:
                quote_text = quote.find(class_='text').get_text(strip=True)
                author = quote.find(class_='author').get_text(strip=True)

                author_url = quote.find('a', href=True)['href']
                author_details = scrape_author_details('http://quotes.toscrape.com' + author_url)

                csv_writer.writerow([quote_text, author,
                                     author_details.get('Born', ''),
                                     author_details.get('Location', ''),
                                     author_details.get('Description', '')])

        else:
            print(f'Failed to fetch page {page_num}')

    csv_file.close()

def scrape_author_details(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        author_name = soup.find(class_='author-title').get_text(strip=True)
        born_date = soup.find(class_='author-born-date').get_text(strip=True)
        born_location = soup.find(class_='author-born-location').get_text(strip=True)
        description = soup.find(class_='author-description').get_text(strip=True)

        return {
            'Author': author_name,
            'Born': born_date,
            'Location': born_location,
            'Description': description
        }
    else:
        print(f'Failed to fetch author details from {url}')
        return None

scrape_quotes()
