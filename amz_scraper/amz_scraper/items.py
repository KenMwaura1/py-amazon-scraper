# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


class AmzScraperItem(scrapy.Item):
   name = scrapy.Field(
       input_processor=MapCompose(remove_tags),
       output_processor=TakeFirst()
   )
   asin = scrapy.Field()
   price = scrapy.Field()
   discounted = scrapy.Field()
   total_reviews = scrapy.Field()