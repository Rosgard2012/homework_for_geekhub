# -*- coding: utf-8 -*-
import scrapy


class ExtensionsSpider(scrapy.Spider):
    name = 'extensions'
    allowed_domains = ['https://chrome.google.com/webstore/sitemap']
    start_urls = ['http://https://chrome.google.com/webstore/sitemap/']

    def parse(self, response):
        pass
