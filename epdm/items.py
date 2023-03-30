# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EpdmItem(scrapy.Item):
    # define the fields for your item here like:
    key = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    position = scrapy.Field()
