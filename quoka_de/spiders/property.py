# -*- coding: utf-8 -*-
from scrapy import Spider, Request, FormRequest
from ..items import OfferLoader


class PropertyOffersSpider(Spider):
    name = "property_offers"
    allowed_domains = ["quoka.de"]
    start_urls = (
        'http://www.quoka.de/immobilien/bueros-gewerbeflaechen/',
    )

    def apply_filters(self, response):
        return FormRequest.from_response(
            response,
            # show offers only (Angebote)
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

        # parse partner offers (Partner-Anzeige)
        for li in response.css('ul.alist > li.partner'):
            l = OfferLoader(selector=li)
            l.add_value('partner_ad', True)
            l.add_xpath('title', 'div[contains(@class, "n2")]/a/h3/text()')
            l.add_xpath('description', './/div[@class="description"]//text()')
            l.add_xpath('price', 'div[contains(@class, "n3")]/p/text()')
            yield l.load_item()

    def parse_page(self, response):
        pass
