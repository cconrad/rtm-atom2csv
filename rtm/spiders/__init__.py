# -*- coding: utf-8 -*-

from scrapy.selector import XmlXPathSelector
import scrapy.spider
import scrapy.shell
from ..items import RtmItem


class RtmSpider(scrapy.spider.BaseSpider):
    name = "rtm"
    start_urls = [
        "https://www.rememberthemilk.com/atom/USER_ID/LIST_ID/?tok=TOKEN"
    ]

    def parse(self, response):
        items = []
        xxs = XmlXPathSelector(response)
        xxs.register_namespace("atom", "http://www.w3.org/2005/Atom")
        for entry in xxs.select('//atom:entry'):
            item = RtmItem()
            item["author_name"] = entry.select(".//atom:author/atom:name/text()").extract()
            item["updated"] = entry.select(".//atom:updated/text()").extract()
            item["id"] = entry.select(".//atom:id/text()").extract()
            item["title"] = entry.select(".//atom:title/text()").extract()
            item["due"] = entry.select(".//*[@class='rtm_due_value']/text()").extract()
            item["priority"] = entry.select(".//*[@class='rtm_priority_value']/text()").extract()
            item["time_estimate"] = entry.select(".//*[@class='rtm_time_estimate_value']/text()").extract()
            item["tags"] = entry.select(".//*[@class='rtm_tags_value']/text()").extract()
            item["location"] = entry.select(".//*[@class='rtm_location_value']/text()").extract()
            item["postponed"] = entry.select(".//*[@class='rtm_postponed_value']/text()").extract()
            items.append(item)
        return items
