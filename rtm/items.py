# -*- coding: utf-8 -*-

import scrapy


class RtmItem(scrapy.Item):
    author_name = scrapy.Field()
    updated = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    due = scrapy.Field()
    priority = scrapy.Field()
    time_estimate = scrapy.Field()
    tags = scrapy.Field()
    location = scrapy.Field()
    postponed = scrapy.Field()
