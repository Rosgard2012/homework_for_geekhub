import scrapy
from scrapy.http import HtmlResponse

class ChromeSpider(scrapy.Spider):
    name = 'chrome_spider'
    start_urls = ['https://chrome.google.com/webstore/sitemap?shard=0',
                  'https://chrome.google.com/webstore/sitemap?shard=1']

    def parse(self, response):
        for url in response.xpath('//sitemap/loc/text()').getall():
            yield scrapy.Request(url, callback=self.parse_extension_page)

    def parse_extension_page(self, response):
        extensions = response.xpath('//loc/text()').getall()
        for extension_url in extensions:
            yield scrapy.Request(extension_url, callback=self.parse_extension)

    def parse_extension(self, response):
        extension_id = response.url.split('/')[-1]
        extension_name = response.xpath('//title/text()').get()
        extension_description = response.xpath('//meta[@name="description"]/@content').get()

        yield {
            'ID': extension_id,
            'Name': extension_name,
            'Description': extension_description
        }
