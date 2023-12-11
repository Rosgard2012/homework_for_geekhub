# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from urllib.parse import urlparse
from scrapy.http import HtmlResponse
import csv

class ExtensionsSpider(scrapy.Spider):
    name = 'extensions'
#    allowed_domains = ['https://chrome.google.com/webstore/sitemap']
    start_urls = ['http://https://chrome.google.com/webstore/sitemap/']

    def parse(self, response):
        sitemap_urls = response.xpath('//sitemap/loc/text()').getall()
        for sitemap_url in sitemap_urls:
            yield scrapy.Request(url=sitemap_url, callback=self.parse_sitemap)
        # sitemap_links = response.css('loc::text').getall()
        # for link in sitemap_links:
        #     yield scrapy.Request(link, callback=self.parse_extension_page)

        # if 'sitemap' in response.url:
        #     # If it's a sitemap index, extract links to extension pages
        #     urls = response.xpath('//sitemap/loc/text()').getall()
        #     for url in urls:
        #         yield scrapy.Request(url, callback=self.parse_extension_page)
        # else:
        #     # If it's an extension page, extract required information
        #     extension_id = response.url.split('/')[-1]
        #     extension_name = response.xpath('//title/text()').get()
        #     extension_description = response.xpath('//meta[@name="description"]/@content').get()
        #
        #     yield {
        #         'ID': extension_id,
        #         'Name': extension_name,
        #         'Description': extension_description
        #     }
    def parse_extension_page(self, response):
        extension_id = response.url.split('/')[-1]
        extension_name = response.xpath('//title/text()').get()
        extension_description = response.xpath('//meta[@name="description"]/@content').get()

        yield {
            'ID': extension_id,
            'Name': extension_name,
            'Description': extension_description
        }


process = CrawlerProcess({
    'FEED_FORMAT': 'csv',
    'FEED_URI': 'extensions.csv'
})
process.crawl(ExtensionsSpider)
process.start()
