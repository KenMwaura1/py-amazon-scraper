# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def strip_spaces(value):
    return value.strip().replace("$", "")


class AmzScraperItem(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_spaces),
        output_processor=TakeFirst()
    )
    asin = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_spaces),
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_spaces),
        output_processor=TakeFirst()
    )
    discounted = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_spaces),
        output_processor=TakeFirst()
    )
    total_reviews = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_spaces),
        output_processor=TakeFirst()
    )
