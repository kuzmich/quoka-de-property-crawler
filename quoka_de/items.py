# -*- coding: utf-8 -*-
from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Compose, MapCompose, Join, Identity


strip = lambda s: s.strip()


class Offer(Item):
    title = Field()
    description = Field()
    price = Field()
    created = Field()
    phone = Field()
    url = Field()
    commercial = Field()
    partner_ad = Field()

class OfferLoader(ItemLoader):
    default_item_class = Offer
    default_input_processor = MapCompose(strip)
    default_output_processor = TakeFirst()

    partner_ad_in = Identity()
