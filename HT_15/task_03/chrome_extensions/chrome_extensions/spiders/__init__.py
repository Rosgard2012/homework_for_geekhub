# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from ..items import ChromeExtensionItem

class ExtensionsSpider(scrapy.Spider):
    name = 'extensions'
    allowed_domains = ['chrome.google.com']
    start_urls = ['https://chrome.google.com/webstore/sitemap']

    def parse(self, response):
        links = response.xpath('//loc/text()').getall()

        for link in links:
            yield scrapy.Request(link, callback=self.parse_extension_page)

    def parse_extension_page(self, response):
        extension = ChromeExtensionItem()

        extension['extension_id'] = response.url.split('/')[-1]
        extension['name'] = response.xpath('//title/text()').get()
        extension['description'] = response.xpath('//meta[@name="description"]/@content').get()

        yield extension
