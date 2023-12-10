# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChromeExtensionItem(scrapy.Item):
    extension_id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
