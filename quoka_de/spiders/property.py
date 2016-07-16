# -*- coding: utf-8 -*-
import scrapy


class PropertyOffersSpider(scrapy.Spider):
    name = "property_offers"
    allowed_domains = ["quoka.de"]
    start_urls = (
        'http://www.quoka.de/immobilien/bueros-gewerbeflaechen/',
    )

    def apply_filters(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'classtype': 'of'},
            callback=self.parse_list
        )
    parse = apply_filters

    def parse_list(self, response):
        with open('page1.html', 'wt') as f:
            f.write(response.text)
