import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import AmzScraperItem
from scrapy.loader import ItemLoader


class AmznspiderSpider(CrawlSpider):
    name = 'amznspider'
    allowed_domains = ['amazon.com']
    start_urls = ['https://amazon.com/s?k=laptop']

    rules = (
        Rule(LinkExtractor(allow='s?k=laptop&page=', restrict_css="a.s-pagination-next")),
        Rule(LinkExtractor(allow='/dp/'), callback='parse-item'),
    )

    def parse_item(self, response):
        l = ItemLoader(item=AmzScraperItem(), response=response)
        l.add_css("name", "span#ProductTitle")
        l.add_css("asin", "#ASIN::attr(value)")
        l.add_css("price","span.a-offscreen")
        l.add_css("discounted", "span.savingsPercentage")
        l.add_css("totalreviews", "span#acrCustomerReviewText")
        yield l.load_item()