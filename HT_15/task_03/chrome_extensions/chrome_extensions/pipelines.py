# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os

current_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(current_file_path)

class ChromeExtensionsPipeline(object):
    # def process_item(self, item, spider):
    #     return item
    def open_spider(self, spider):
        current_file_path = os.path.abspath(__file__)
        parent_directory = os.path.dirname(current_file_path)
        file_path = os.path.join(parent_directory, 'extensions_data.csv')

        self.csv_file = open(file_path, 'w', newline='', encoding='utf-8')
        self.csv_writer = csv.DictWriter(self.csv_file, fieldnames=['ID', 'Назва', 'Опис'])
        self.csv_writer.writeheader()

    def close_spider(self, spider):
        self.csv_file.close()

    def process_item(self, item, spider):
        self.csv_writer.writerow(item)
        return item