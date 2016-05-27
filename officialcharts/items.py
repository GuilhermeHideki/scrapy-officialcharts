# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OfficialchartsItem(scrapy.Item):
    pos = scrapy.Field()
    title = scrapy.Field()
    artist = scrapy.Field()
