import scrapy
from .factories import get_formatted_url_dates
from ..items import EpdmItem

import scrapy

class SongSpider(scrapy.Spider):
    name = 'epdm'
    start_urls = get_formatted_url_dates()

    def parse(self, response):
        items = EpdmItem()

        for item in response.css('div.item'):
            items['key'] = item.xpath('@data-key').get()
            items['name'] = item.css('div.info').css('div.name::text').get().strip()
            items['author'] = item.css('div.info').css('div.name::text').get().strip()
            items['position'] = item.css('div.info').css('p::text').get().strip()
            yield items
    