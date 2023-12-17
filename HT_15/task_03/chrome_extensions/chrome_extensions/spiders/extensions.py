import scrapy
from bs4 import BeautifulSoup
import csv


class ExtensionsSpider(scrapy.Spider):
    name = "extensions"
    allowed_domains = ["chrome.google.com"]
    start_urls = ['https://chrome.google.com/webstore/sitemap']

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        for sitemap_loc in soup.select('sitemap > loc'):
            yield scrapy.Request(url=sitemap_loc.text, callback=self.parse_urls)

    def parse_urls(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        for url_loc in soup.select('url > loc'):
            if "/detail" not in url_loc.text:
                continue
            yield scrapy.Request(url=url_loc.text, callback=self.parse_extensions)

    def parse_extensions(self, response):
        extension_id = response.css('[property="og:url"]::attr(content)').get().split('/').pop()
        extension_name = response.css('[property="og:title"]::attr(content)').get()
        extension_description = response.css('[property="og:description"]::attr(content)').get()
        extension_url = response.css('[property="og:url"]::attr(content)').get()

        yield {
            'extension_id': f'{extension_id}',
            'extension_name': extension_name,
            'extension_description': extension_description,
            'extension_url': extension_url
        }

        with open('extensions.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['extension_id', 'extension_name', 'extension_description', 'extension_url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({
                'extension_id': extension_id,
                'extension_name': extension_name,
                'extension_description': extension_description,
                'extension_url': extension_url
            })

