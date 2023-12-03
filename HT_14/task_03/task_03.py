import requests
from bs4 import BeautifulSoup
import csv



def scrape_quotes():
    csv_file = open('quotes.csv', 'w', newline='', encoding='utf-8')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Quote', 'Author', 'Tags', 'Born', 'Location', 'Description'])

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
        author_url = quote.find('a', href=True)['href']
        author_details = scrape_author_details('http://quotes.toscrape.com' + author_url)
        csv_writer.writerow([quote_text, author, tags,
                             author_details['Born'],
                             author_details['Location'],
                             author_details['Description']])
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

# def scrape_authors():
#     csv_file = open('quotes.csv', 'w', newline='', encoding='utf-8')
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(['Quote', 'Author', 'Tags', 'Born', 'Location', 'Description'])
#
#     author_urls = [
#         'http://quotes.toscrape.com/author/J-K-Rowling',
#         # Додайте інші URL-адреси авторів, якщо потрібно
#     ]
#
#     for url in author_urls:
#         response = requests.get(url)
#
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.content, 'html.parser')
#             author_name = soup.find(class_='author-title').get_text(strip=True)
#             born_date = soup.find(class_='author-born-date').get_text(strip=True)
#             born_location = soup.find(class_='author-born-location').get_text(strip=True)
#             description = soup.find(class_='author-description').get_text(strip=True)
#
#             csv_writer.writerow([author_name, born_date, born_location, description])
#
#         else:
#             print(f'Failed to fetch author page {url}')
#
#     csv_file.close()




# scrape_authors()

