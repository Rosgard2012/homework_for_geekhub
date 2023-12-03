import requests
from bs4 import BeautifulSoup
import csv


csv_quotes = open('quotes.csv', 'w', newline='', encoding='utf-8')
csv_writer_quotes = csv.writer(csv_quotes)
csv_writer_quotes.writerow(['Quote', 'Author', 'Tags'])


for page_num in range(1, 11):
    url = f'http://quotes.toscrape.com/page/{page_num}'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        quotes = soup.find_all(class_='quote')

        for quote in quotes:
            quote_text = quote.find(class_='text').get_text(strip=True)
            author = quote.find(class_='author').get_text(strip=True)
            tags = ', '.join(tag.get_text(strip=True) for tag in quote.find_all(class_='tag'))

            csv_writer.writerow([quote_text, author, tags])

    else:
        print(f'Failed to fetch page {page_num}')

csv_quotes.close()
