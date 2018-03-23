# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class My51JobspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    area = scrapy.Field()
    money = scrapy.Field()
    company = scrapy.Field()
    people = scrapy.Field()
    type = scrapy.Field()
    study = scrapy.Field()
    exp = scrapy.Field()
    pass
