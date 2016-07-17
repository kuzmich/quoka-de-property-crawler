# -*- coding: utf-8 -*-
from scrapy import Spider, Request, FormRequest


class PropertyOffersSpider(Spider):
    name = "property_offers"
    allowed_domains = ["quoka.de"]
    start_urls = (
        'http://www.quoka.de/immobilien/bueros-gewerbeflaechen/',
    )

    def apply_filters(self, response):
        return FormRequest.from_response(
            response,
            # show offers only
            formdata={'classtype': 'of'},
            callback=self.parse_list
        )
    parse = apply_filters

    def parse_list(self, response):
        # follow paginator links
        for a in response.css('ul.sem > li.pageno > a[href]'):
            yield Request(response.urljoin(a.xpath('./@href').extract_first()),
                          self.parse_list)

        # open all detail pages
        for li in response.css('ul.alist > li.hlisting'):
            yield Request(response.urljoin(li.xpath('./div/a/@href').extract_first()),
                          self.parse_page)

    def parse_page(self, response):
        pass
